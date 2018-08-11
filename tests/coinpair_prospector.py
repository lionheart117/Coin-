# coding=utf-8

from binance.BinanceAPI import *
from restful.HuobiServices import *

def CoinPairProspector(baseCoinList, quoteCoinList):

    client = BinanceAPI('', '', 10)

    BinanceCoinPairs = {}
    HuobiCoinPairs = {}
    LegalCoinPairs = {}

    while(1):
        try:
            binanceSymbolList = client.get_exchange_info()['symbols']
            huobiSymbolList = get_symbols()['data']
            break
        except requests.exceptions.ConnectionError as e:
            print(e)
            print('Please wait 3 seconds')
            time.sleep(3)

    if baseCoinList:

        for symbollist in binanceSymbolList:
            for quoteCoin in quoteCoinList:
                for baseCoin in baseCoinList:
                    if symbollist['baseAsset'] == baseCoin and symbollist['quoteAsset'] == quoteCoin:
                        BinanceCoinPairs[symbollist['symbol']] = True

        for symbollist in huobiSymbolList:
            for quoteCoin in quoteCoinList:
                for baseCoin in baseCoinList:
                    if symbollist['base-currency'] == baseCoin.lower() and symbollist['quote-currency'] == quoteCoin.lower():
                        HuobiCoinPairs[symbollist['symbol'].upper()] = True

        for symbol in BinanceCoinPairs:
            if symbol in HuobiCoinPairs:
                LegalCoinPairs[symbol] = True
    else:
        for symbollist in binanceSymbolList:
            for quoteCoin in quoteCoinList:
                if symbollist['quoteAsset'] == quoteCoin:
                    BinanceCoinPairs[symbollist['symbol']] = True

        for symbollist in huobiSymbolList:
            for quoteCoin in quoteCoinList:
                if symbollist['quote-currency'] == quoteCoin.lower():
                    HuobiCoinPairs[symbollist['symbol'].upper()] = True

        for symbol in BinanceCoinPairs:
            if symbol in HuobiCoinPairs:
                LegalCoinPairs[symbol] = True

    logfile = open('CoinPairProspector' + time.strftime('_%Y_%m_%dT%H_%M_%S') + '.log', 'w')

    while(1):
        for symbol in LegalCoinPairs:
            try:
                binanceTicker = client.get_order_books(symbol,5)
                huobiTicker = get_ticker(symbol.lower())#get_depth('iotaeth', 'step0')
                if (not binanceTicker['bids']) or (not binanceTicker['asks']) or (not huobiTicker['tick']['bid']) or (not huobiTicker['tick']['ask']):
                    continue
            except requests.exceptions.ConnectionError as e:
                print(e)
                continue

            binanceBidPrice = float(binanceTicker['bids'][0][0])
            binanceAskPrice = float(binanceTicker['asks'][0][0])

            huobiBidPrice = float(huobiTicker['tick']['bid'][0])#float(huobiTicker['tick']['bids'][0][0])
            huobiAskPrice = float(huobiTicker['tick']['ask'][0])#float(huobiTicker['tick']['asks'][0][0])

            ProfitH2B = (1 - 0.002 ) * huobiBidPrice   - (1 + 0.0005) * binanceAskPrice # Huobi  : sell Binance:buy
            ProfitB2H = (1 - 0.0005) * binanceBidPrice - (1 + 0.002 ) * huobiAskPrice   # Binance: sell Huobi  :buy

            if ProfitH2B > 0 or ProfitB2H > 0:
                info = time.strftime('%Y-%m-%dT%H:%M:%S') + ': ' + symbol + ':' + ' ONE  SIDE TRADE GAIN PROFIT: H2B:%.8f  B2H:%.8f' % (ProfitH2B, ProfitB2H)
                print(info),
                logfile.write(info + '\n')
            else:
                print(time.strftime('%Y-%m-%dT%H:%M:%S') + ': ' + symbol + ':' + ' BOTH SIDE TRADES DEFICIT: H2B:%.8f  B2H:%.8f' % (ProfitH2B, ProfitB2H)),


if __name__ == '__main__':
    CoinPairProspector([],['ETH'])