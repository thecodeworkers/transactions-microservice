from google.protobuf.json_format import MessageToDict
from grpc import StatusCode
from ..bootstrap import grpc_server, service_bus
from ...protos import SendMoneyServicer, add_SendMoneyServicer_to_server, SendCryptoResponse
from ...utils import parser_context

class SendMoneyService(SendMoneyServicer):
    def send_crypto(self, request, context):
        try:
            provider_name = parser_context(context, 'provider')

            params = MessageToDict(request)
            params['provider'] = provider_name

            service_bus.init_connection()
            response = service_bus.receive('send_crypto', params);
            service_bus.stop()
            service_bus.close_connection()

            result = response['result']
            status = response['success']

            if not status: raise Exception(result)

            return SendCryptoResponse(result=result)

        except Exception as error:
            context.set_details(str(error))
            context.set_code(StatusCode.INVALID_ARGUMENT)

def start_send_money_service():
    add_SendMoneyServicer_to_server(SendMoneyService(), grpc_server)
