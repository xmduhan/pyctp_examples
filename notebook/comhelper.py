#!/usr/bin/env python
# encoding: utf-8
from datetime import datetime
from time import sleep
from dateutil.relativedelta import relativedelta


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


def getDefaultInstrumentID(months=1):
    """
    获取一个可用的交易品种ID
    """
    return datetime.strftime(datetime.now() + relativedelta(months=months), "IF%y%m")
