#include "worker.pb.h"
#include "worker.grpc.pb.h"

#include <grpcpp/grpcpp.h>

#include <gflags/gflags.h>
#include <glog/logging.h>

#include "reconstruction.h"
#include "config.h"

using grpc::Server;
using grpc::ServerBuilder;
using grpc::ServerContext;
using grpc::Status;
using grpc::ServerReader;
using grpc::ServerWriter;

std::shared_ptr<ReconstructionContext> OpenMVGReconstructionContext(const std::string& id);

class WorkerServer : public Worker::Service {
    virtual ::grpc::Status ComputeFeatures(ServerContext* context, 
                                      const WorkerComputeFeaturesRequest* request, 
                                      WorkerComputeFeaturesResponse* response){
         LOG(INFO) << "Computing Features: " << request->image_id();
         try{
            ReconstructionFetcher rf;
            auto reconstruction = rf.Fetch(OpenMVGReconstructionContext(request->reconstruction_id()));
            reconstruction->ComputeFeatures({request->image_id()});
            response->set_success(true);
            return Status::OK;
         }catch(const std::exception& e){
            LOG(ERROR) << e.what();
            return Status::CANCELLED;
        }
    }

    virtual ::grpc::Status AddImage(ServerContext* context, 
                                    const WorkerAddImageRequest* request, 
                                    WorkerAddImageResponse* response){
        LOG(INFO) << "Adding Image: " << request->image_id();
        try{
            ReconstructionFetcher rf;
            auto reconstruction = rf.Fetch(OpenMVGReconstructionContext(request->reconstruction_id()));
            reconstruction->AddImage({request->image_id()}, true);
            response->set_success(true);
            return Status::OK;
         }catch(const std::exception& e){
            LOG(ERROR) << e.what();
            return Status::CANCELLED;
        }
    }

    virtual ::grpc::Status ComputeMatches(ServerContext* context, 
                                          const WorkerComputeMatchesRequest* request, 
                                          WorkerComputeMatchesResponse* response){
         LOG(INFO) << "Computing Matches: " << request->image_id();
         try{
            ReconstructionFetcher rf;
            auto reconstruction = rf.Fetch(OpenMVGReconstructionContext(request->reconstruction_id()));
            reconstruction->ComputeMatches({request->image_id()});
            response->set_success(true);
            return Status::OK;
         }catch(const std::exception& e){
            LOG(ERROR) << e.what();
            return Status::CANCELLED;
        }
    }

    virtual Status IncrementalSFM(ServerContext* context, 
                                  const ::WorkerIncrementalSFMRequest* request, 
                                  WorkerIncrementalSFMResponse* response){
        LOG(INFO) << "IncrementalSFM: " << request->reconstruction_id();
        try{
            ReconstructionFetcher rf;
            auto reconstruction = rf.Fetch(OpenMVGReconstructionContext(request->reconstruction_id()));
            response->set_success(reconstruction->SparseReconstruct());
            return Status::OK;
         }catch(const std::exception& e){
            LOG(ERROR) << e.what();
            return Status::CANCELLED;
        }
    }

    virtual Status ComputeStructure(ServerContext* context, 
                                    const WorkerComputeStructureRequest* request, 
                                    WorkerComputeStructureResponse* response){
        LOG(INFO) << "ComputeStructure: " << request->reconstruction_id();
        try{
            ReconstructionFetcher rf;
            auto reconstruction = rf.Fetch(OpenMVGReconstructionContext(request->reconstruction_id()));
            response->set_success(reconstruction->ComputeStructure());
            return Status::OK;
         }catch(const std::exception& e){
            LOG(ERROR) << e.what();
            return Status::CANCELLED;
        }
    }
};

int main(int argc, char* argv[]){
    google::InitGoogleLogging(argv[0]);
    CONFIG_LOAD(argv[1]);
    WorkerServer service;
    std::string server_address(CONFIG_GET_STRING("worker.address"));
    LOG(INFO) << "Starting server at address " << server_address; 
    grpc::EnableDefaultHealthCheckService(true);
    ServerBuilder builder;
    builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
    builder.RegisterService(&service);
    std::shared_ptr<Server> server(builder.BuildAndStart());
    
    LOG(INFO) << "Registering self with pool manager ...";
    WorkerPoolManager::Stub manager = WorkerPoolManager::Stub(grpc::CreateChannel(CONFIG_GET_STRING("worker_pool.address"),
                             grpc::InsecureChannelCredentials()));
    grpc::ClientContext ctx;
    RegisterWorkerRequest req;
    RegisterWorkerResponse resp;
    req.set_address(server_address);
    req.set_cores(CONFIG_GET_INT("worker.cores"));
    manager.Register(&ctx, req, &resp);
    LOG(INFO) << "Server waiting for connections...";
    server->Wait();
    return 1;
}