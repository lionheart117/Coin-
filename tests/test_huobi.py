#!/usr/bin/env python
# -*- coding: utf-8 -*-

from restful.HuobiServices import *

print("火币API测试---------------")
print("火币API分为3类：")
print("1.市场数据类(Market Data API)----行情查询")
print("2.交易/账户类(Trade/Account API)----对账户的查询，下单，撤单等操作")
print("3.借贷类(Margin API)----此类API涉及杠杆交易暂时用不到")

print("常用API如下：")
test_symbol = 'btcusdt'
test_order_id = 12345
print("--------市场数据类(Market Data API)--------")
print("1. 获取K线数据（以btc/usdt,日线为例）")
# print(get_kline(test_symbol, '1day'))

print("2. 获取市场深度（以btc/usdt, step0为例）")
# print(get_depth(test_symbol, 'step0'))

print("3. 获取交易细节（以获取btc/usdt交易细节为例）")
# print(get_trade(test_symbol))

print("4. 获取交易历史（以获取10条btc/usdt历史交易为例）")
# todo 暂时不清楚和第三条有什么区别
# print(get_trade_history(test_symbol, 10))

print("5. 获取聚合行情（ticker）（以btc/usdt为例）")
# print(get_ticker(testest_symboltSymbol))

print("6. 获取24小时成交量数据 （以btc/usdt为例）")
# print(get_detail(test_symbol))

print("--------交易/账户类(Trade/Account API)--------")
print("1. 获取账户列表")
# print(get_accounts())

print("2. 获取当前账户资产")
# print(get_balance())

print("3. 创建下单 ！！确认后执行！！")
# print(send_order())

print("4. 撤销订单 ！！确认后执行！！")
# print(cancel_order(test_order_id))

print("5. 查询订单信息")
# print(order_info(test_order_id))

print("6. 查询订单明细")
# print(order_match_results(test_order_id))

print("7. 查询当前委托、历史委托")
# print(orders_list())

print("8. 查询当前成交、历史成交")
# print(orders_match_results())


