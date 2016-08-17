# -*- coding:utf-8 -*-
# HammerHead 锤头线 倒锤头线


import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import time
import sys
import tick
import schedule
from pymongo import MongoClient
conn = MongoClient('localhost',27017)

#-----------------------------------------------------------
#---------------------此处修改参数---------------------------

db = conn.db.data2016
start = '2015-06-01'
span = 5
data = []
datalist = []

#----------------------------------------------------------
#---------------------此处修改参数---------------------------
print('——*——*——*————*——*——*————*——*——*————*——*——*———*——*——*——')
print('当 K 线 下 行 至 MA15 以 下 时,切 勿 冲 动 买 入 !!!')
print('——*——*——*————*——*——*————*——*——*————*——*——*———*——*——*——')
print time.strftime("%Y-%m-%d", time.localtime())


datalistindex = schedule.schedule.index(start)

for i in range(datalistindex,datalistindex+span):
    datalist.append(schedule.schedule[i])

print(datalist)
count = 0
ticklen = len(tick.tick)

for ticki in tick.tick:
    for i in range(0,span):
        for item in db.find({'dt':datalist[i], 'tick':ticki}):
            data.append(item)
    for i in range(len(data)):
        # 收阳
        if data[i]['close']>data[i]['open']:
            if (data[i]['high']/data[i]['open'])/(data[i]['close']/data[i]['open'])>1.05:
                print '倒锤头线'
                print data[i]['tick'],data[i]['dt']
                print ('----------------')
            # 收阴
        if data[i]['close']<data[i]['open']:
            if (data[i]['high']/data[i]['close'])/(data[i]['open']/data[i]['close'])>1.05:
                print '倒锤头线'
                print data[i]['tick'],data[i]['dt']
                print ('----------------')

        if data[i]['close']>data[i]['open']:
            if (data[i]['open']/data[i]['low'])/(data[i]['open']/data[i]['close'])<1.04:
                print '锤头线'
                print data[i]['tick'],data[i]['dt']
                print ('----------------')

        if data[i]['close']<data[i]['open']:
            if (data[i]['close']/data[i]['low'])/(data[i]['close']/data[i]['open'])<1.04:
                print '锤头线'
                print data[i]['tick'],data[i]['dt']
                print ('----------------')
    del data[:]
    print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
    sys.stdout.flush()
