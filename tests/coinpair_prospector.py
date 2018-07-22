# coding=utf-8

from binance.BinanceAPI import *
from restful.HuobiServices import *

def CoinPairProspector():

    client = BinanceAPI('', '')

    while(1):
        binanceTicker = client.get_order_books('IOTAETH')
        huobiTicker = get_depth('iotaeth', 'step0')

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