from binance.client import Client
from binance.websockets import BinanceSocketManager

proxies = {
    'http': 'http://127.0.0.1:1080',
    'https': 'http://127.0.0.1:1080'
}

def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)

# ATTENTION: the key as below is only for test!
client = Client('8V1vHSkGeFt4d1LqARDZN5t3BFH7i9lGldsmqqOXCcSB1Xru9Xgltcu9lqVaibkm','ghlZnglVGeBd28pHhYxP47aj79Vp5RIKc4JRI6BZ5B2rdGL5AyIerTCbAXB85uzP', {'proxies': proxies})

print('TEST1 ====> REST API print:')
print(client.get_account())
depth = client.get_order_book(symbol='EOSETH',limit='5')
print(depth)

tickers = client.get_orderbook_ticker(symbol='EOSETH')
print(tickers)

bm=BinanceSocketManager(client)
bm.start_depth_socket('EOSETH', process_message)
bm.start()
print('TEST2 ====> WebSocket API print:')



