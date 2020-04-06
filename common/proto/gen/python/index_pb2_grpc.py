# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import index_pb2 as index__pb2


class VisualIndexingServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.IndexImage = channel.unary_unary(
        '/VisualIndexingService/IndexImage',
        request_serializer=index__pb2.IndexImageRequest.SerializeToString,
        response_deserializer=index__pb2.IndexImageResponse.FromString,
        )
    self.GetBagOfWords = channel.unary_unary(
        '/VisualIndexingService/GetBagOfWords',
        request_serializer=index__pb2.GetBagOfWordsRequest.SerializeToString,
        response_deserializer=index__pb2.GetBagOfWordsResponse.FromString,
        )
    self.FindAll = channel.unary_unary(
        '/VisualIndexingService/FindAll',
        request_serializer=index__pb2.FindAllRequest.SerializeToString,
        response_deserializer=index__pb2.FindAllResponse.FromString,
        )


class VisualIndexingServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def IndexImage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBagOfWords(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindAll(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_VisualIndexingServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'IndexImage': grpc.unary_unary_rpc_method_handler(
          servicer.IndexImage,
          request_deserializer=index__pb2.IndexImageRequest.FromString,
          response_serializer=index__pb2.IndexImageResponse.SerializeToString,
      ),
      'GetBagOfWords': grpc.unary_unary_rpc_method_handler(
          servicer.GetBagOfWords,
          request_deserializer=index__pb2.GetBagOfWordsRequest.FromString,
          response_serializer=index__pb2.GetBagOfWordsResponse.SerializeToString,
      ),
      'FindAll': grpc.unary_unary_rpc_method_handler(
          servicer.FindAll,
          request_deserializer=index__pb2.FindAllRequest.FromString,
          response_serializer=index__pb2.FindAllResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'VisualIndexingService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
