# coding=utf-8

from binance.BinanceAPI import *
from restful.HuobiServices import *

def CoinPairProspector():

    client = BinanceAPI('', '')

    BinanceCoinPairs = {}
    HuobiCoinPairs = {}
    LegalCoinPairs = {}

    for symbollist in client.get_exchange_info()['symbols']:
        if symbollist['status'] == 'TRADING':
            BinanceCoinPairs[symbollist['symbol']] = True

    for symbollist in get_symbols()['data']:
        HuobiCoinPairs[symbollist['symbol'].upper()] = True

    for symbol in BinanceCoinPairs:
        if symbol in HuobiCoinPairs:
            LegalCoinPairs[symbol] = True

    while(1):
        for symbol in LegalCoinPairs:
            binanceTicker = client.get_order_books(symbol,5)
            huobiTicker = get_ticker(symbol.lower())#get_depth('iotaeth', 'step0')

            binanceBidPrice = float(binanceTicker['bids'][0][0])
            binanceAskPrice = float(binanceTicker['asks'][0][0])

            huobiBidPrice = float(huobiTicker['tick']['bid'][0])#float(huobiTicker['tick']['bids'][0][0])
            huobiAskPrice = float(huobiTicker['tick']['ask'][0])#float(huobiTicker['tick']['asks'][0][0])

            ProfitH2B = (1 - 0.002 ) * huobiBidPrice   - (1 + 0.0005) * binanceAskPrice # Huobi  : sell Binance:buy
            ProfitB2H = (1 - 0.0005) * binanceBidPrice - (1 + 0.002 ) * huobiAskPrice   # Binance: sell Huobi  :buy

            if ProfitH2B > 0:
                print(symbol + ':' + ' H2B gain profit: %.8f' % ProfitH2B)
            elif ProfitB2H > 0:
                print(symbol + ':' + ' B2H gain profit: %.8f' % ProfitB2H)
            else:
                print(symbol + ':' + ' BOTH SIDE TRADES DEFICIT: H2B:%.8f  B2H:%.8f' % (ProfitH2B, ProfitB2H))


if __name__ == '__main__':
    CoinPairProspector()