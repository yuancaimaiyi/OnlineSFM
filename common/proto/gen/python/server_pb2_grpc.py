# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import server_pb2 as server__pb2


class ReconstructionServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Handshake = channel.unary_unary(
                '/ReconstructionService/Handshake',
                request_serializer=server__pb2.HandhsakeRequest.SerializeToString,
                response_deserializer=server__pb2.HandshakeResponse.FromString,
                )
        self.ReconstructionUploadImage = channel.stream_unary(
                '/ReconstructionService/ReconstructionUploadImage',
                request_serializer=server__pb2.ReconstructionUploadImageRequest.SerializeToString,
                response_deserializer=server__pb2.ReconstructionUploadImageResponse.FromString,
                )
        self.ComputeMatches = channel.unary_unary(
                '/ReconstructionService/ComputeMatches',
                request_serializer=server__pb2.ComputeMatchesRequest.SerializeToString,
                response_deserializer=server__pb2.ComputeMatchesResponse.FromString,
                )
        self.SparseReconstruct = channel.unary_unary(
                '/ReconstructionService/SparseReconstruct',
                request_serializer=server__pb2.SparseReconstructRequest.SerializeToString,
                response_deserializer=server__pb2.SparseReconstructResponse.FromString,
                )
        self.GetOBJ = channel.unary_stream(
                '/ReconstructionService/GetOBJ',
                request_serializer=server__pb2.GetOBJRequest.SerializeToString,
                response_deserializer=server__pb2.GetOBJResponse.FromString,
                )
        self.GetSparse = channel.unary_stream(
                '/ReconstructionService/GetSparse',
                request_serializer=server__pb2.GetSparseRequest.SerializeToString,
                response_deserializer=server__pb2.GetSparseResponse.FromString,
                )
        self.NewReconstruction = channel.unary_unary(
                '/ReconstructionService/NewReconstruction',
                request_serializer=server__pb2.NewReconstructionRequest.SerializeToString,
                response_deserializer=server__pb2.NewReconstructionResponse.FromString,
                )
        self.DeleteReconstruction = channel.unary_unary(
                '/ReconstructionService/DeleteReconstruction',
                request_serializer=server__pb2.DeleteReconstructionRequest.SerializeToString,
                response_deserializer=server__pb2.DeleteReconstructionResponse.FromString,
                )
        self.StartSession = channel.unary_unary(
                '/ReconstructionService/StartSession',
                request_serializer=server__pb2.StartSessionRequest.SerializeToString,
                response_deserializer=server__pb2.StartSessionResponse.FromString,
                )
        self.StopSession = channel.unary_unary(
                '/ReconstructionService/StopSession',
                request_serializer=server__pb2.StopSessionRequest.SerializeToString,
                response_deserializer=server__pb2.StopSessionResponse.FromString,
                )
        self.SessionAddImage = channel.stream_unary(
                '/ReconstructionService/SessionAddImage',
                request_serializer=server__pb2.SessionAddImageRequest.SerializeToString,
                response_deserializer=server__pb2.SessionAddImageResponse.FromString,
                )
        self.GetReconstructionConfig = channel.unary_unary(
                '/ReconstructionService/GetReconstructionConfig',
                request_serializer=server__pb2.GetReconstructionConfigRequest.SerializeToString,
                response_deserializer=server__pb2.GetReconstructionConfigResponse.FromString,
                )
        self.GetAgentConfig = channel.unary_unary(
                '/ReconstructionService/GetAgentConfig',
                request_serializer=server__pb2.GetAgentConfigRequest.SerializeToString,
                response_deserializer=server__pb2.GetAgentCOnfigResponse.FromString,
                )
        self.ReconstructionUploadImageBatch = channel.stream_unary(
                '/ReconstructionService/ReconstructionUploadImageBatch',
                request_serializer=server__pb2.ReconstructionUploadImageBatchRequest.SerializeToString,
                response_deserializer=server__pb2.ReconstructionUploadImageBatchResponse.FromString,
                )
        self.MVS = channel.unary_unary(
                '/ReconstructionService/MVS',
                request_serializer=server__pb2.MVSRequest.SerializeToString,
                response_deserializer=server__pb2.MVSResponse.FromString,
                )
        self.SetAgentConfigFields = channel.unary_unary(
                '/ReconstructionService/SetAgentConfigFields',
                request_serializer=server__pb2.SetAgentConfigFieldsRequest.SerializeToString,
                response_deserializer=server__pb2.SetAgentConfigFieldsResponse.FromString,
                )
        self.SetReconstructionConfigFields = channel.unary_unary(
                '/ReconstructionService/SetReconstructionConfigFields',
                request_serializer=server__pb2.SetReconstructionConfigFieldsRequest.SerializeToString,
                response_deserializer=server__pb2.SetReconstructionConfigFieldsResponse.FromString,
                )
        self.GetAllImages = channel.unary_unary(
                '/ReconstructionService/GetAllImages',
                request_serializer=server__pb2.GetAllImagesRequest.SerializeToString,
                response_deserializer=server__pb2.GetAllImagesResponse.FromString,
                )
        self.GetImageRegions = channel.unary_unary(
                '/ReconstructionService/GetImageRegions',
                request_serializer=server__pb2.GetImageRegionsRequest.SerializeToString,
                response_deserializer=server__pb2.GetImageRegionsResponse.FromString,
                )
        self.ScoreImages = channel.unary_unary(
                '/ReconstructionService/ScoreImages',
                request_serializer=server__pb2.ScoreImagesRequest.SerializeToString,
                response_deserializer=server__pb2.ScoreImagesResponse.FromString,
                )


class ReconstructionServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Handshake(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReconstructionUploadImage(self, request_iterator, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ComputeMatches(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SparseReconstruct(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOBJ(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSparse(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NewReconstruction(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteReconstruction(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartSession(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopSession(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SessionAddImage(self, request_iterator, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetReconstructionConfig(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAgentConfig(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReconstructionUploadImageBatch(self, request_iterator, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MVS(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAgentConfigFields(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetReconstructionConfigFields(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllImages(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetImageRegions(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ScoreImages(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReconstructionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Handshake': grpc.unary_unary_rpc_method_handler(
                    servicer.Handshake,
                    request_deserializer=server__pb2.HandhsakeRequest.FromString,
                    response_serializer=server__pb2.HandshakeResponse.SerializeToString,
            ),
            'ReconstructionUploadImage': grpc.stream_unary_rpc_method_handler(
                    servicer.ReconstructionUploadImage,
                    request_deserializer=server__pb2.ReconstructionUploadImageRequest.FromString,
                    response_serializer=server__pb2.ReconstructionUploadImageResponse.SerializeToString,
            ),
            'ComputeMatches': grpc.unary_unary_rpc_method_handler(
                    servicer.ComputeMatches,
                    request_deserializer=server__pb2.ComputeMatchesRequest.FromString,
                    response_serializer=server__pb2.ComputeMatchesResponse.SerializeToString,
            ),
            'SparseReconstruct': grpc.unary_unary_rpc_method_handler(
                    servicer.SparseReconstruct,
                    request_deserializer=server__pb2.SparseReconstructRequest.FromString,
                    response_serializer=server__pb2.SparseReconstructResponse.SerializeToString,
            ),
            'GetOBJ': grpc.unary_stream_rpc_method_handler(
                    servicer.GetOBJ,
                    request_deserializer=server__pb2.GetOBJRequest.FromString,
                    response_serializer=server__pb2.GetOBJResponse.SerializeToString,
            ),
            'GetSparse': grpc.unary_stream_rpc_method_handler(
                    servicer.GetSparse,
                    request_deserializer=server__pb2.GetSparseRequest.FromString,
                    response_serializer=server__pb2.GetSparseResponse.SerializeToString,
            ),
            'NewReconstruction': grpc.unary_unary_rpc_method_handler(
                    servicer.NewReconstruction,
                    request_deserializer=server__pb2.NewReconstructionRequest.FromString,
                    response_serializer=server__pb2.NewReconstructionResponse.SerializeToString,
            ),
            'DeleteReconstruction': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteReconstruction,
                    request_deserializer=server__pb2.DeleteReconstructionRequest.FromString,
                    response_serializer=server__pb2.DeleteReconstructionResponse.SerializeToString,
            ),
            'StartSession': grpc.unary_unary_rpc_method_handler(
                    servicer.StartSession,
                    request_deserializer=server__pb2.StartSessionRequest.FromString,
                    response_serializer=server__pb2.StartSessionResponse.SerializeToString,
            ),
            'StopSession': grpc.unary_unary_rpc_method_handler(
                    servicer.StopSession,
                    request_deserializer=server__pb2.StopSessionRequest.FromString,
                    response_serializer=server__pb2.StopSessionResponse.SerializeToString,
            ),
            'SessionAddImage': grpc.stream_unary_rpc_method_handler(
                    servicer.SessionAddImage,
                    request_deserializer=server__pb2.SessionAddImageRequest.FromString,
                    response_serializer=server__pb2.SessionAddImageResponse.SerializeToString,
            ),
            'GetReconstructionConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.GetReconstructionConfig,
                    request_deserializer=server__pb2.GetReconstructionConfigRequest.FromString,
                    response_serializer=server__pb2.GetReconstructionConfigResponse.SerializeToString,
            ),
            'GetAgentConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAgentConfig,
                    request_deserializer=server__pb2.GetAgentConfigRequest.FromString,
                    response_serializer=server__pb2.GetAgentCOnfigResponse.SerializeToString,
            ),
            'ReconstructionUploadImageBatch': grpc.stream_unary_rpc_method_handler(
                    servicer.ReconstructionUploadImageBatch,
                    request_deserializer=server__pb2.ReconstructionUploadImageBatchRequest.FromString,
                    response_serializer=server__pb2.ReconstructionUploadImageBatchResponse.SerializeToString,
            ),
            'MVS': grpc.unary_unary_rpc_method_handler(
                    servicer.MVS,
                    request_deserializer=server__pb2.MVSRequest.FromString,
                    response_serializer=server__pb2.MVSResponse.SerializeToString,
            ),
            'SetAgentConfigFields': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAgentConfigFields,
                    request_deserializer=server__pb2.SetAgentConfigFieldsRequest.FromString,
                    response_serializer=server__pb2.SetAgentConfigFieldsResponse.SerializeToString,
            ),
            'SetReconstructionConfigFields': grpc.unary_unary_rpc_method_handler(
                    servicer.SetReconstructionConfigFields,
                    request_deserializer=server__pb2.SetReconstructionConfigFieldsRequest.FromString,
                    response_serializer=server__pb2.SetReconstructionConfigFieldsResponse.SerializeToString,
            ),
            'GetAllImages': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllImages,
                    request_deserializer=server__pb2.GetAllImagesRequest.FromString,
                    response_serializer=server__pb2.GetAllImagesResponse.SerializeToString,
            ),
            'GetImageRegions': grpc.unary_unary_rpc_method_handler(
                    servicer.GetImageRegions,
                    request_deserializer=server__pb2.GetImageRegionsRequest.FromString,
                    response_serializer=server__pb2.GetImageRegionsResponse.SerializeToString,
            ),
            'ScoreImages': grpc.unary_unary_rpc_method_handler(
                    servicer.ScoreImages,
                    request_deserializer=server__pb2.ScoreImagesRequest.FromString,
                    response_serializer=server__pb2.ScoreImagesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ReconstructionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ReconstructionService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Handshake(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ReconstructionService/Handshake',
            server__pb2.HandhsakeRequest.SerializeToString,
            server__pb2.HandshakeResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReconstructionUploadImage(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/ReconstructionService/ReconstructionUploadImage',
            server__pb2.ReconstructionUploadImageRequest.SerializeToString,
            server__pb2.ReconstructionUploadImageResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ComputeMatches(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ReconstructionService/ComputeMatches',
            server__pb2.ComputeMatchesRequest.SerializeToString,
            server__pb2.ComputeMatchesResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SparseReconstruct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ReconstructionService/SparseReconstruct',
            server__pb2.SparseReconstructRequest.SerializeToString,
            server__pb2.SparseReconstructResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOBJ(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ReconstructionService/GetOBJ',
            server__pb2.GetOBJRequest.SerializeToString,
            server__pb2.GetOBJResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSparse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ReconstructionService/GetSparse',
            server__pb2.GetSparseRequest.SerializeToString,
            server__pb2.GetSparseResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NewReconstruction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ReconstructionService/NewReconstruction',
            server__pb2.NewReconstructionRequest.SerializeToString,
            server__pb2.NewReconstructionResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteReconstruction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ReconstructionService/DeleteReconstruction',
            server__pb2.DeleteReconstructionRequest.SerializeToString,
            server__pb2.DeleteReconstructionResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ReconstructionService/StartSession',
            server__pb2.StartSessionRequest.SerializeToString,
            server__pb2.StartSessionResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ReconstructionService/StopSession',
            server__pb2.StopSessionRequest.SerializeToString,
            server__pb2.StopSessionResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SessionAddImage(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/ReconstructionService/SessionAddImage',
            server__pb2.SessionAddImageRequest.SerializeToString,
            server__pb2.SessionAddImageResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetReconstructionConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ReconstructionService/GetReconstructionConfig',
            server__pb2.GetReconstructionConfigRequest.SerializeToString,
            server__pb2.GetReconstructionConfigResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAgentConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ReconstructionService/GetAgentConfig',
            server__pb2.GetAgentConfigRequest.SerializeToString,
            server__pb2.GetAgentCOnfigResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReconstructionUploadImageBatch(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/ReconstructionService/ReconstructionUploadImageBatch',
            server__pb2.ReconstructionUploadImageBatchRequest.SerializeToString,
            server__pb2.ReconstructionUploadImageBatchResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MVS(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ReconstructionService/MVS',
            server__pb2.MVSRequest.SerializeToString,
            server__pb2.MVSResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAgentConfigFields(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ReconstructionService/SetAgentConfigFields',
            server__pb2.SetAgentConfigFieldsRequest.SerializeToString,
            server__pb2.SetAgentConfigFieldsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetReconstructionConfigFields(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ReconstructionService/SetReconstructionConfigFields',
            server__pb2.SetReconstructionConfigFieldsRequest.SerializeToString,
            server__pb2.SetReconstructionConfigFieldsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllImages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ReconstructionService/GetAllImages',
            server__pb2.GetAllImagesRequest.SerializeToString,
            server__pb2.GetAllImagesResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetImageRegions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ReconstructionService/GetImageRegions',
            server__pb2.GetImageRegionsRequest.SerializeToString,
            server__pb2.GetImageRegionsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ScoreImages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ReconstructionService/ScoreImages',
            server__pb2.ScoreImagesRequest.SerializeToString,
            server__pb2.ScoreImagesResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
