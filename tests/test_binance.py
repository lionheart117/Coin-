from binance.client import Client
from binance.websockets import BinanceSocketManager

def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)

client = Client('8V1vHSkGeFt4d1LqARDZN5t3BFH7i9lGldsmqqOXCcSB1Xru9Xgltcu9lqVaibkm','ghlZnglVGeBd28pHhYxP47aj79Vp5RIKc4JRI6BZ5B2rdGL5AyIerTCbAXB85uzP')

print('TEST1 ====> REST API print:')
depth = client.get_order_book(symbol='BNBBTC')
print(depth)

bm=BinanceSocketManager(client)
bm.start_aggtrade_socket('BNBBTC', process_message)
bm.start()
print('TEST2 ====> WebSocket API print:')



