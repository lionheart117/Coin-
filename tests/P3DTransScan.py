# coding=utf-8

from binance.EtherScanKeys import *
from binance.EtherScanAPI import *
import time

def P3DTransScan():
    ethscanapi = EtherScanAPI(ETH_SCAN_KEY)
    logfile = open('P3DTransScan' + time.strftime('_%Y_%m_%dT%H_%M_%S') + '.log', 'w')
    i = 1
    while(i):
        transNum = 0
        endblock = 99999999
        try:
            endblock = int(ethscanapi.get_LatestBlockNum()['result'], 16)
        except ImportError:
            endblock = endblock

        startblock = endblock - 15

        try:
            traslist = ethscanapi.get_TransactionByAddress(address="0xB3775fB83F7D12A36E0475aBdD1FCA35c091efBe", sort="desc",
                                             startblock=str(startblock), endblock=str(endblock))['result']
        except ImportError:
            continue

        if i == 1:
            starttime = int(traslist[0]['timeStamp'])
            endtime = starttime - 60
        else:
            endtime = starttime
            starttime += 60

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

            info = time.strftime('%Y-%m-%dT%H:%M:%S') + ' : ' + 'P3D Transaction speed: %s/minute\n' % transNum
            print(info)
            logfile.write(info)
        else:
            starttime = endtime

        i += 1
        time.sleep(1)

if __name__ == '__main__':
    P3DTransScan()