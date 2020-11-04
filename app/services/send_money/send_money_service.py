from google.protobuf.json_format import MessageToDict
from grpc import StatusCode
from ..bootstrap import grpc_server, service_bus
from ...protos import SendMoneyServicer, add_SendMoneyServicer_to_server, WithdrawResponse, SentResponse
from ...utils import parser_context
from ...models import Balances, Operations, Amounts

class SendMoneyService(SendMoneyServicer):
    def withdraw(self, request, context):
        try:
            # auth_token = parser_context(context, 'auth_token')
            # is_auth(auth_token, '06_send_money_withdraw')

            provider_name = parser_context(context, 'provider')

            params = MessageToDict(request)
            params['provider'] = provider_name

            service_bus.init_connection()
            response = service_bus.receive('send_crypto', params)
            service_bus.stop()
            service_bus.close_connection()

            result = response['result']
            status = response['success']

            if not status: raise Exception(result)

            return WithdrawResponse(result=result)

        except Exception as error:
            context.set_details(str(error))
            context.set_code(StatusCode.INVALID_ARGUMENT)

    def sent(self, request, context):
        # auth_token = parser_context(context, 'auth_token')
        # is_auth(auth_token, '06_send_money_sent')

        currency = request.currency
        account = request.account
        amount = request.amount

        # get user id

        # rest fee
        # valid min amount
        # valid max amount

        # get current balance
        # validate availability

        # valid if account exist

        ## process operation

        # Actualizar en tiempo real la operacion de recepcion que recibe el otro usuario al que se le envia el dinero

        return SentResponse(result='Money has be sent')


def start_send_money_service():
    add_SendMoneyServicer_to_server(SendMoneyService(), grpc_server)
