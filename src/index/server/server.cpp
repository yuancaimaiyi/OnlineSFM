#include "index.pb.h"
#include "index.grpc.pb.h"
#include "config.h"

#include <grpcpp/grpcpp.h>
#include <grpcpp/health_check_service_interface.h>
#include <grpcpp/ext/proto_server_reflection_plugin.h>

#include <gflags/gflags.h>
#include <glog/logging.h>

#include "vocab_index.h"
#include "image_indexer.h"

using grpc::Server;
using grpc::ServerBuilder;
using grpc::ServerContext;
using grpc::Status;
using grpc::ServerReader;
using grpc::ServerWriter;

std::shared_ptr<VisualVocabularyIndex> visual_vocab_index;

class VisualIndexingServer : public VisualIndexingService::Service {
    virtual ::grpc::Status IndexImage(ServerContext* context, 
                                      const IndexImageRequest* request, 
                                      IndexImageResponse* response){
        auto image_indexer = 
            ImageIndexerFactory::GetImageIndexer(visual_vocab_index);
        LOG(INFO) << "Indexing image " << request->image_id();
        image_indexer->Index(request->image_id());
        return Status::OK;
    }

    virtual ::grpc::Status GetBagOfWords(ServerContext* context, 
                                          const GetBagOfWordsRequest* request, 
                                          GetBagOfWordsResponse* response){
        auto image_indexer = 
            ImageIndexerFactory::GetImageIndexer(visual_vocab_index);
        return Status::OK;
    }

    virtual ::grpc::Status FindAll(ServerContext* context, 
                                   const FindAllRequest* request, 
                                   FindAllResponse* response){
        auto image_indexer = 
            ImageIndexerFactory::GetImageIndexer(visual_vocab_index);
        return Status::OK;
    }
};


int main(int argc, char* argv[]){
    google::InitGoogleLogging(argv[0]);
    CONFIG_LOAD(argv[1]);
    visual_vocab_index = std::make_shared<VisualVocabularyIndex>(std::make_unique<KDTreeIndex<SIFTDistance>>());

    LOG(INFO) << "Loading index from " << argv[2];
    visual_vocab_index->Load(argv[2]);
    VisualIndexingServer service;
    std::string server_address(CONFIG_GET_STRING("index.address"));
    LOG(INFO) << "Starting server at address " << server_address; 
    grpc::EnableDefaultHealthCheckService(true);
    ServerBuilder builder;
    builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
    builder.RegisterService(&service);
    std::shared_ptr<Server> server(builder.BuildAndStart());
    LOG(INFO) << "Server waiting for connections...";
    server->Wait();

    return 1;
}