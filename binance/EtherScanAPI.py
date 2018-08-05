#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-23
# @Author  : Lionheart117
# @QQ      : 77640674
# @github  : https://github.com/lionheart117

import time
import hashlib
import requests
import hmac

try:
    from urllib import urlencode
# python3
except ImportError:
    from urllib.parse import urlencode


class EtherScanAPI:
    BASE_URL = "https://api.etherscan.io/api"

    def __init__(self, apikeytoken):
        self.apikeytoken = apikeytoken

    def get_EthBalance4SingleAddr(self, address):
        path = "%s?module=account&action=balance&tag=latest" % self.BASE_URL
        params = {"address": address, "apikey": self.apikeytoken}
        return self._get_no_sign(path, params)

    def get_TokenSupply(self, contractaddress):
        path = "%s?module=stats&action=tokensupply" % self.BASE_URL
        params = {"contractaddress": contractaddress, "apikey": self.apikeytoken}
        return self._get_no_sign(path, params)

    def get_TokenAccountBalance(self, contractaddress, address):
        path = "%s?module=account&action=tokenbalance&tag=latest" % self.BASE_URL
        params = {"contractaddress": contractaddress, "address": address, "apikey": self.apikeytoken}
        return self._get_no_sign(path, params)

    def get_TransactionByAddress(self, address, sort, startblock, endblock):
        path = "%s?module=account&action=txlist" % self.BASE_URL
        params = {"startblock": startblock, "endblock": endblock, "sort": sort, "address": address, "apikey": self.apikeytoken}
        return self._get_no_sign(path, params)

    def get_internalTransactionByAddress(self, address, sort, startblock, endblock):
        path = "%s?module=account&action=txlistinternal" % self.BASE_URL
        params = {"startblock": startblock, "endblock": endblock, "sort": sort, "address": address, "apikey": self.apikeytoken}
        return self._get_no_sign(path, params)

    def _get_no_sign(self, path, params={}):
        query = urlencode(params)
        url = "%s&%s" % (path, query)
        return requests.get(url, timeout=120).json()

    def get_LatestBlockNum(self):
        path = "%s?module=proxy&action=eth_blockNumber" % self.BASE_URL
        params = {"apikey": self.apikeytoken}
        return self._get_no_sign(path, params)


if __name__ == '__main__':
    from binance.EtherScanKeys import ETH_SCAN_KEY

    ethscanapi = EtherScanAPI(ETH_SCAN_KEY)
    print(int(ethscanapi.get_LatestBlockNum()['result'],16))
    print(ethscanapi.get_EthBalance4SingleAddr(address="0xB3775fB83F7D12A36E0475aBdD1FCA35c091efBe"))
    print(ethscanapi.get_TokenSupply(contractaddress="0xB3775fB83F7D12A36E0475aBdD1FCA35c091efBe"))
    print(ethscanapi.get_TokenAccountBalance(contractaddress="0xB3775fB83F7D12A36E0475aBdD1FCA35c091efBe",address="0xe04f27eb70e025b78871a2ad7eabe85e61212761"))
    print(ethscanapi.get_TransactionByAddress(address="0xB3775fB83F7D12A36E0475aBdD1FCA35c091efBe", sort="desc",startblock="6039820",endblock="99999999"))
    print(ethscanapi.get_internalTransactionByAddress(address="0xB3775fB83F7D12A36E0475aBdD1FCA35c091efBe", sort="desc",startblock="6039820",endblock="99999999"))

