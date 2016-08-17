# -*- coding:utf-8 -*-
# 高位并排阳线 跳空上扬形(第三根K线不分阴阳)

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

db = conn.db.data2016
start = '2016-06-10'
span = 15
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
    for i in range(len(data)-1):
        if (1-round(data[i]['close']/data[i]['open'],2))>0.03 and\
                data[i+1]['low']>data[i]['high'] and data[i+2]['low']<data[i]['high'] and \
                    data[i+1]['close']>data[i+1]['open']:
                        print ''
                        print data[i]['tick'],data[i]['dt']
                        print ('----------------')
    del data[:]
    print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
    sys.stdout.flush()
