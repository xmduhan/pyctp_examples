#!/usr/bin/env python
# encoding: utf-8
import os
from datetime import datetime
from time import sleep
from dateutil.relativedelta import relativedelta
from pyctp import struct


frontAddress = os.environ.get('CTP_FRONT_ADDRESS')
mdFrontAddress = os.environ.get('CTP_MD_FRONT_ADDRESS')
brokerID = os.environ.get('CTP_BROKER_ID')
userID = os.environ.get('CTP_USER_ID')
password = os.environ.get('CTP_PASSWORD')
assert frontAddress and mdFrontAddress and brokerID and userID and password


def wait(expr, second=5):
    """
    等待服务器响应
    expr 一个lambda表达式，如果表达式执行返回True则退出循环
    second 等待的时间，单位:秒
    """
    t0 = datetime.now()
    t1 = t0
    toWaitOnce = .01
    while (t1 - t0).total_seconds() < second:
        if expr():
            break
        sleep(toWaitOnce)
        t1 = datetime.now()
    else:
        raise Exception('等待超时')


def getDefaultInstrumentId(months=1):
    """
    获取一个可用的交易品种ID
    """
    return datetime.strftime(datetime.now() + relativedelta(months=months), "IF%y%m")


orderRefSeq = 0


def getOrderRef():
    '''
    获取OrderRef序列值
    '''
    global orderRefSeq
    orderRefSeq += 1
    return ('%12d' % orderRefSeq).replace(' ', '0')  # '000000000001'


def getInsertOrderField(instrumentId, direction, action, volume=1, limitPrice=0):
    """
    获取一个有效的建单数据格式
    """
    inputOrderField = struct.CThostFtdcInputOrderField()
    inputOrderField.BrokerID = brokerID
    inputOrderField.InvestorID = userID
    inputOrderField.InstrumentID = instrumentId
    inputOrderField.OrderRef = getOrderRef()
    inputOrderField.UserID = userID

    if limitPrice == 0:
        inputOrderField.OrderPriceType = '1'     # 任意价
    else:
        inputOrderField.OrderPriceType = '2'  # 限价

    # inputOrderField.Direction = '0'          # 买
    # inputOrderField.CombOffsetFlag = '0'     # 开仓
    if action == 'open':
        inputOrderField.CombOffsetFlag = '0'
        inputOrderField.Direction = {'buy': '0', 'sell': '1'}[direction]
    elif action == 'close':
        inputOrderField.CombOffsetFlag = '1'
        inputOrderField.Direction = {'buy': '1', 'sell': '0'}[direction]
    else:
        raise Exception(u'未知的操作方向')

    inputOrderField.CombHedgeFlag = '1'      # 投机
    inputOrderField.LimitPrice = limitPrice  # 限价 0表不限制
    inputOrderField.VolumeTotalOriginal = volume  # 手数

    if limitPrice == 0:
        inputOrderField.TimeCondition = '1'      # 立即完成否则撤消
    else:
        inputOrderField.TimeCondition = '3'  # 当日有效

    inputOrderField.GTDDate = ''
    inputOrderField.VolumeCondition = '1'    # 成交类型  '1' 任何数量  '2' 最小数量 '3'全部数量
    inputOrderField.MinVolume = volume       # 最小数量
    inputOrderField.ContingentCondition = '1'  # 触发类型 '1' 立即否则撤消
    inputOrderField.StopPrice = 0             # 止损价
    inputOrderField.ForceCloseReason = '0'    # 强平标识 '0'非强平
    inputOrderField.IsAutoSuspend = 0         # 自动挂起标识
    inputOrderField.BusinessUnit = ''         # 业务单元
    inputOrderField.RequestID = 1
    inputOrderField.UserForceClose = 0        # 用户强平标识
    inputOrderField.IsSwapOrder = 0           # 互换单标识
    return inputOrderField
