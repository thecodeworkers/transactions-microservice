from .send_money import start_send_money_service
from .exchange import start_exchange_service

def start_all_servicers():
    start_send_money_service()
    start_exchange_service()

def start_all_emiters():
    pass
