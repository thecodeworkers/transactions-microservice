from google.protobuf.json_format import MessageToDict
from grpc import StatusCode
from ..bootstrap import grpc_server
from ...protos import ExchangeServicer, add_ExchangeServicer_to_server, ExchangeResponse

class ExchangeService(ExchangeServicer):
    def simple_exchange(self, request, context):
        # calculate fee
        # valid min amount
        # valid max amount

        out_currency = request.out_currency
        in_currency = request.in_currency
        out_amount = request.out_amount

        ## Esperar la api correspondiente para procesar todo el intercambio

        # Guardar un primer registro con la moneda que sale
        # Guardar un segundo registro con la moneda que entra con la relacion del registro que tiene la moneda que sale
        #Actualizar el primer registor relacionandolo al segundo registro

        return ExchangeResponse(result=outCurrency)


def start_exchange_service():
    add_ExchangeServicer_to_server(ExchangeService(), grpc_server)
