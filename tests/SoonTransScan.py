# coding=utf-8

from binance.EtherScanKeys import *
from binance.EtherScanAPI import *
import time

def SoonTransScan():
    ethscanapi = EtherScanAPI(ETH_SCAN_KEY)
    logfile = open('P3DTransScan' + time.strftime('_%Y_%m_%dT%H_%M_%S') + '.log', 'w')
    i = 1
    while(i):
        transNum = 0
        try:
            endblock = int(ethscanapi.get_LatestBlockNum()['result'], 16)
        except ImportError:
            endblock = endblock

        startblock = endblock - 15

        try:
            traslist = ethscanapi.get_TransactionByAddress(address="0x4e8ecF79AdE5e2C49B9e30D795517A81e0Bf00B8", sort="desc",
                                             startblock=str(startblock), endblock=str(endblock))['result']
        except ImportError:
            continue

        if i == 1:
            starttime = int(traslist[0]['timeStamp'])
            endtime = starttime - 15
        else:
            endtime = starttime
            starttime += 15

        if int(traslist[0]['timeStamp']) >= starttime:
            for trans in traslist:
                if i == 1:
                    if int(trans['timeStamp']) < endtime:
                        break
                    else:
                        transNum += 1
                else:
                    if int(trans['timeStamp']) <= endtime:
                        break
                    elif int(trans['timeStamp']) <= starttime:
                        transNum += 1

            info = time.strftime('%Y-%m-%dT%H:%M:%S') + ' : ' + 'Fomo Soon Transaction speed: %s/15s\n' % transNum
            print(info)
            logfile.write(info)
        else:
            starttime = endtime

        i += 1
        time.sleep(1)

if __name__ == '__main__':
    SoonTransScan()