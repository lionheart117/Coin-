# coding=utf-8

from binance.client import Client
from restful.HuobiServices import *
import time

proxies = {
    'http': 'http://127.0.0.1:1080',
    'https': 'http://127.0.0.1:1080'
}

def CoinPairProspector():

    client = Client('8V1vHSkGeFt4d1LqARDZN5t3BFH7i9lGldsmqqOXCcSB1Xru9Xgltcu9lqVaibkm',
                    'ghlZnglVGeBd28pHhYxP47aj79Vp5RIKc4JRI6BZ5B2rdGL5AyIerTCbAXB85uzP', {'proxies': proxies})

    while(1):
        binanceTicker = client.get_order_book(symbol='EOSETH')
        huobiTicker = get_depth('eoseth', 'step0')

        binanceBidPrice = float(binanceTicker['bids'][0][0])
        binanceAskPrice = float(binanceTicker['asks'][0][0])

#        print(huobiTicker)
        huobiBidPrice = float(huobiTicker['tick']['bids'][0][0])
        huobiAskPrice = float(huobiTicker['tick']['asks'][0][0])

        profit = (1 - 0.002) * huobiBidPrice - (1 + 0.001) * binanceAskPrice

#        profit = 0

        if profit > 0:
            print('gain profit: %f' % profit)
        else:
            print('trade deficit: %f' % profit)

        time.sleep(1)

if __name__ == '__main__':
    CoinPairProspector()