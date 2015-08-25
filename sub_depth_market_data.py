#!/usr/bin/env python
# encoding: utf-8

import os
from pyctp import Md, callback
from time import sleep


def main():
    """
    """
    # 读取环境变量
    frontAddress = os.environ.get('CTP_FRONT_ADDRESS')
    mdFrontAddress = os.environ.get('CTP_MD_FRONT_ADDRESS')
    brokerID = os.environ.get('CTP_BROKER_ID')
    userID = os.environ.get('CTP_USER_ID')
    password = os.environ.get('CTP_PASSWORD')
    assert frontAddress and mdFrontAddress and brokerID and userID and password

    # 定义回调函数
    def OnRspSubMarketData(**kwargs):
        Data = kwargs['Data']
        ErrorID = kwargs['RspInfo']['ErrorID']
        ErrorMsg = kwargs['RspInfo']['ErrorMsg']
        print u'订阅%s:(%d,%s)' % (Data['InstrumentID'], ErrorID, ErrorMsg)

    def OnRtnDepthMarketData(**kwargs):
        Data = kwargs['Data']
        print '%s : Ask=%.1f, Bid=%.1f, Volume=%d' % (Data['InstrumentID'], Data['AskPrice1'], Data['BidPrice1'], Data['Volume'])
    # 订阅行情
    instrumentIDList = ['IF1509', 'IF1510']
    md = Md(mdFrontAddress, brokerID, userID, password)
    md.bind(callback.OnRspSubMarketData, OnRspSubMarketData)
    md.bind(callback.OnRtnDepthMarketData, OnRtnDepthMarketData)
    md.SubscribeMarketData(instrumentIDList)
    while True:
        sleep(1)

if __name__ == "__main__":
    main()
