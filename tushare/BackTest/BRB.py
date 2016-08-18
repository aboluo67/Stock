# -*- coding:utf-8 -*-
# 两红夹一黑

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

#----------------------------------------------------------
#---------------------此处修改参数---------------------------

db = conn.db.data08
start = '2016-08-08'
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
    for i in range(len(data)-3):
        if data[i]['ma10'] != None and data[i]['ma20'] != None:
            if data[i]['close']>((data[i]['ma20']+data[i]['ma10'])*1.0/2):
                if data[i]['open']<data[i]['close'] and data[i+1]['open']>data[i+1]['close'] and data[i+2]['open']<data[i+2]['close']:
                    if data[i]['close']>data[i+1]['open'] and data[i+1]['open']<data[i+2]['close']:
                        if data[i]['open'] < (data[i + 1]['close']) and (data[i + 1]['close']) > data[i + 2]['open']:
                            count += 1
                            print ''
                            print 'No.', count
                            print data[i]['tick'], data[i]['dt'],data[i+3]['price_change']
                            print ('----------------')
    del data[:]
    print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
    sys.stdout.flush()
