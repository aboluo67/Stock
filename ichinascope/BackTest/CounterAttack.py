# -*- coding:utf-8 -*-
# 好友反攻

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
start = '2016-06-03'
span = 2
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
        if (1-round(data[i]['open']/data[i]['close'],2)) < -0.03 and\
            (1-round(data[i+1]['open']/data[i+1]['close'],2))> 0.02 and \
                (data[i]['close']*0.98<data[i+1]['close']<data[i]['close']*1.01):
                    print ''
                    print data[i+1]['tick'],data[i+1]['dt']
                    print ('----------------')
    del data[:]
    print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
    sys.stdout.flush()

#300187 2016-06-02

# 2016-08-11
# ['2016-06-03', '2016-06-06']
# 进度 : 1300 / 2886
# 002635 2016-06-06
# ----------------
# 进度 : 2591 / 2886
# 600095 2016-06-06
# ----------------
# 进度 : 2818 / 2886
# 603996 2016-06-06
# ----------------
# 进度 : 2885 / 2886