#!/usr/bin/env python
# encoding: utf-8

# 程序功能：查询交易账户信息
## 读取frontAddress brokerID userID password信息。
## 这些信息放在环境变量中，以避免出现在程序中。
import os
frontAddress = os.environ.get('CTP_FRONT_ADDRESS')
brokerID = os.environ.get('CTP_BROKER_ID')
userID = os.environ.get('CTP_USER_ID')
password = os.environ.get('CTP_PASSWORD')
assert frontAddress and brokerID and userID and password
## 导入pyctp相关的模块
##   Trader 交易员接口封装
##   Md 行情接口封装
##   struct 所有CTP结构体定义
##   callback 所有CTP的回调函数名称
from pyctp import Trader,Md,struct,callback
from time import sleep
## 创建交易员接口对象
trader = Trader(frontAddress,brokerID,userID,password)
## 定义回调函数
result = []
def OnRspQryInvestor (**kwargs):   # 注意：方法名称可以自由定义
    result.append(kwargs)
## 绑定回调函数到交易员接口
trader.bind(callback.OnRspQryInvestor, OnRspQryInvestor)
## 准备请求数据表单
requestData = struct.CThostFtdcQryInvestorField()
requestData.BrokerID = brokerID
requestData. InvestorID = userID
## 调用请求API
trader.ReqQryInvestor(requestData)
## 等待回调被调用
while len(result) == 0 : sleep(.01)
## 查看返回数据结果
for k,v in result[0]['Data'].iteritems(): print k,':',v

