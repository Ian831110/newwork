# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 14:45:30 2021

@author: user
"""

#line 權杖:i3AFMbAsERoo5VWUzI8h0uYzQyIrDEoYtQuLEcOtvD3
import time,ccxt,datetime
import urllib.request as request
import requests
today = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
now=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
print(now[8:12])
#K_time = datetime.datetime.strptime( today+'000500','%Y%m%d%H%M%S' )
#print(K_time)

#LineNotify
def linenotifymessage(token,msg):
    headers={
        "Authorization":"Bearer"+token,
        "Content-Type":"application/x-www-form-urlencoded"
        }
    payload={'message':msg}
    r=requests.post("https://notify-api.line.me/api/notify",headers=headers,params=payload)
def message(mes):
    if __name__== "__main__":
        token='i3AFMbAsERoo5VWUzI8h0uYzQyIrDEoYtQuLEcOtvD3'
        message=("\n"+mes)
        linenotifymessage(token,message)
price="427"
product="BNB"
i=0
def standard(close,note):
    global i
    global std
    global price
    if i == 0:
        i+=1
    elif str(close) <= price:
        message(note)
    std=close
k=0
while k == 0:
    import ccxt,time
#申明okex交易所
    today = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    now=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    exchange=ccxt.binance()
#獲取最新tick數據
    data=exchange.fetchTicker(symbol='LTC/USDT')
#獲取最新K線數據 日線 小時線
#print(data)
    a='BNB/USDT'
    b='1m'
    data=exchange.fetch_ohlcv(symbol=a,timeframe=b,limit=1)
    for i in data:
        open=i[1]
        high=i[2]
        low=i[3]
        close=i[4]
        volume=i[5]
        change=round((float(i[4])-float(i[1])),3)
        changerate=round((float(i[4])-float(i[1]))/float(i[1]),3)
        s1=a+'\n'+b+'\n'+'開盤:'+str(open)+'\n'+'最高價:'+str(high)+'\n'+'最低價:'+str(low)+'\n'+'收盤價:'+str(close)+'\n'+'成交量:'+str(volume)+'\n'+'漲跌:'+str(change)+'\n'+'時間:'+str(now)
        note=s1
        standard(close,note)
        #print(s1)
        time.sleep(60)