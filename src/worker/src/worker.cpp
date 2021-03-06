#include "worker.pb.h"
#include "worker.grpc.pb.h"

#include <grpcpp/grpcpp.h>

#include <gflags/gflags.h>
#include <glog/logging.h>

#include "reconstruction.h"
#include "sql_storage.h"
#include "config.h"
#include "util.h"
#include "grpc_service_provider.h"
#include "exceptions.h"

using grpc::Server;
using grpc::ServerBuilder;
using grpc::ServerContext;
using grpc::ServerReader;
using grpc::ServerWriter;
using grpc::Status;

std::shared_ptr<ReconstructionContext> OpenMVGReconstructionContext(const std::string &id);

class WorkerServer : public Worker::Service
{
    virtual ::grpc::Status ComputeFeatures(ServerContext *context,
                                           const WorkerComputeFeaturesRequest *request,
                                           WorkerComputeFeaturesResponse *response)
    {
        LOG(INFO) << "Computing Features: " << request->image_id();
        try
        {
            ReconstructionFetcher rf;
            auto reconstruction = rf.Fetch(OpenMVGReconstructionContext(request->reconstruction_id()));
            if (reconstruction->ComputeFeatures({request->image_id()}))
            {
                return Status::OK;
            }
            return Status::CANCELLED;
        }
        catch (const std::exception &e)
        {
            LOG(ERROR) << e.what();
            return Status::CANCELLED;
        }
    }

    virtual ::grpc::Status AddImage(ServerContext *context,
                                    const WorkerAddImageRequest *request,
                                    WorkerAddImageResponse *response)
    {
        LOG(INFO) << "Adding Image: " << request->image_id();
        try
        {
            ReconstructionFetcher rf;
            auto reconstruction = rf.Fetch(OpenMVGReconstructionContext(request->reconstruction_id()));
            bool success = reconstruction->AddImage({request->image_id()}, true);
            return Status::OK;
        }
        catch (const CameraIntrinsicNotFoundException &e)
        {
            LOG(INFO) << e.what();
            return Status::OK;
        }
        catch (const std::exception &e)
        {
            LOG(ERROR) << e.what();
            return Status::CANCELLED;
        }
    }

    virtual ::grpc::Status ComputeMatches(ServerContext *context,
                                          const WorkerComputeMatchesRequest *request,
                                          WorkerComputeMatchesResponse *response)
    {
        LOG(INFO) << "Computing Matches: " << request->image_id();
        try
        {
            ReconstructionFetcher rf;
            auto reconstruction = rf.Fetch(OpenMVGReconstructionContext(request->reconstruction_id()));
            if (reconstruction->ComputeMatches({request->image_id()}))
            {
                return Status::OK;
            }
            return Status::CANCELLED;
        }
        catch (const std::exception &e)
        {
            LOG(ERROR) << e.what();
            return Status::CANCELLED;
        }
    }

    virtual Status IncrementalSFM(ServerContext *context,
                                  const ::WorkerIncrementalSFMRequest *request,
                                  WorkerIncrementalSFMResponse *response)
    {
        LOG(INFO) << "IncrementalSFM: " << request->reconstruction_id();
        try
        {
            ReconstructionFetcher rf;
            auto reconstruction = rf.Fetch(OpenMVGReconstructionContext(request->reconstruction_id()));
            reconstruction->SparseReconstruct();
            return Status::OK;
        }
        catch (const std::exception &e)
        {
            LOG(ERROR) << e.what();
            return Status::CANCELLED;
        }
    }

    virtual Status ComputeStructure(ServerContext *context,
                                    const WorkerComputeStructureRequest *request,
                                    WorkerComputeStructureResponse *response)
    {
        LOG(INFO) << "ComputeStructure: " << request->reconstruction_id();
        try
        {
            ReconstructionFetcher rf;
            auto reconstruction = rf.Fetch(OpenMVGReconstructionContext(request->reconstruction_id()));
            reconstruction->ComputeStructure();
            return Status::OK;
        }
        catch (const std::exception &e)
        {
            LOG(ERROR) << e.what();
            return Status::CANCELLED;
        }
    }

    virtual Status MVS(ServerContext *context,
                       const WorkerMVSRequest *request,
                       WorkerMVSResponse *response)
    {
        LOG(INFO) << "MVS: " << request->reconstruction_id();
        try
        {
            ReconstructionFetcher rf;
            auto reconstruction = rf.Fetch(OpenMVGReconstructionContext(request->reconstruction_id()));
            if (reconstruction->MVS())
                return Status::OK;
            return Status::CANCELLED;
        }
        catch (const std::exception &e)
        {
            LOG(ERROR) << e.what();
            return Status::CANCELLED;
        }
    }
};

#include "capacity_bounded_job_queue_decorator.h"
#include "ampq_job_queue.h"
#include "static_job_cost_provider.h"
#include "jobs.h"
int main(int argc, char *argv[])
{
    google::InitGoogleLogging(argv[0]);
    CONFIG_LOAD(argv[1]);
    SQLStorage::InitConnectionPool(10);
    ElasticDumper::Init(CONFIG_GET_LIST("elastic.hosts"),
                        CONFIG_GET_INT("elastic.timer_interval"));
    ElasticDumper::Instance()->Start();
    WorkerServer service;
    std::string server_address(argv[2]);
    LOG(INFO) << "Starting server at address " << server_address;
    grpc::EnableDefaultHealthCheckService(true);
    ServerBuilder builder;
    builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
    builder.RegisterService(&service);
    std::shared_ptr<Server> server(builder.BuildAndStart());

    LOG(INFO) << "Registering self with pool manager ...";
    auto manager = GRPC_PROVIDER->Get<WorkerPoolManager>(CONFIG_GET_STRING("worker_pool.address"));

    grpc::ClientContext ctx;
    RegisterWorkerRequest req;
    RegisterWorkerResponse resp;
    req.set_address(server_address);
    req.set_cores(CONFIG_GET_INT("worker.cores"));
    manager->Register(&ctx, req, &resp);
    LOG(INFO) << "Server waiting for connections...";

    auto cost_provider = std::make_shared<StaticJobCostProvider>();
    cost_provider->Load(CONFIG_GET_STRING("jobs.cost_file"));
    JobCost resources;
    resources.exclusive_cores = 10;
    resources.ram_usage = 1000000 * 10;
    auto job_queue = std::make_shared<CapacityBoundedJobQueueDecorator>(std::make_shared<AMQPJobExchange>(event_base_new(),
                                                                                                          "amqp://user:bitnami@localhost:5672",
                                                                                                          "job_exchange",
                                                                                                          "my_key"),
                                                                        cost_provider,
                                                                        resources);

    job_queue->Consume<ComputeFeaturesJob>([](ComputeFeaturesJob &j, JobResult &jr) {
        try
        {
            ReconstructionFetcher rf;
            auto reconstruction = rf.Fetch(OpenMVGReconstructionContext(j.reconstruction_id));
            jr.status = reconstruction->ComputeFeatures({j.image_id});
        }
        catch (const std::exception &e)
        {
            jr.status = false;
            jr.info = e.what();
            LOG(ERROR) << e.what();
        }
        return true;
    });

    job_queue->Consume<AddImageJob>([](AddImageJob &j, JobResult &jr) {
        try
        {
            ReconstructionFetcher rf;
            auto reconstruction = rf.Fetch(OpenMVGReconstructionContext(j.reconstruction_id));
            jr.status = reconstruction->AddImage(j.image_id, true);
        }
        catch (const std::exception &e)
        {
            jr.status = false;
            jr.info = e.what();
            LOG(ERROR) << e.what();
        }
        return true;
    });

    job_queue->Consume<ComputeMatchesJob>([](ComputeMatchesJob &j, JobResult &jr) {
        try
        {
            ReconstructionFetcher rf;
            auto reconstruction = rf.Fetch(OpenMVGReconstructionContext(j.reconstruction_id));
            jr.status = reconstruction->ComputeMatches(std::set<std::string>{j.image_id});
        }
        catch (const std::exception &e)
        {
            jr.status = false;
            jr.info = e.what();
            LOG(ERROR) << e.what();
        }
        return true;
    });

    job_queue->Consume<SparseReconstructionJob>([](SparseReconstructionJob &j, JobResult &jr) {
        try
        {
            ReconstructionFetcher rf;
            auto reconstruction = rf.Fetch(OpenMVGReconstructionContext(j.reconstruction_id));
            jr.status = reconstruction->SparseReconstruct();
        }
        catch (const std::exception &e)
        {
            jr.status = false;
            jr.info = e.what();
            LOG(ERROR) << e.what();
        }
        return true;
    });

    job_queue->Consume<ComputeStructureJob>([](ComputeStructureJob &j, JobResult &jr) {
        try
        {
            ReconstructionFetcher rf;
            auto reconstruction = rf.Fetch(OpenMVGReconstructionContext(j.reconstruction_id));
            jr.status = reconstruction->ComputeStructure();
        }
        catch (const std::exception &e)
        {
            jr.status = false;
            jr.info = e.what();
            LOG(ERROR) << e.what();
        }
        return true;
    });

    job_queue->Consume<MVSJob>([](MVSJob &j, JobResult &jr) {
        try
        {
            ReconstructionFetcher rf;
            auto reconstruction = rf.Fetch(OpenMVGReconstructionContext(j.reconstruction_id));
            jr.status = reconstruction->MVS();
        }
        catch (const std::exception &e)
        {
            jr.status = false;
            jr.info = e.what();
            LOG(ERROR) << e.what();
        }
        return true;
    });

    server->Wait();
    return 1;
}