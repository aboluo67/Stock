# -*- coding:utf-8 -*-
# 跳空下跌三颗星(kankong)

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import time
import sys
import tick
import schedule
from pymongo import MongoClient
report_time = time.strftime("%Y-%m-%d %H时%M分", time.localtime())

# MAC
# report_address = '/Users/zoutao/Report/'+report_time+'-每日复盘/跳空下跌三颗星.txt'
# if os.path.exists('/Users/zoutao/Report/'+report_time+'-每日复盘'):
#     message = 'file exists.'
#     print message
# else:
#     os.makedirs('/Users/zoutao/Report/'+report_time+'-每日复盘')
#     print 'Created Report '+report_time+'-每日复盘'

# ubuntu
report_address = '/home/feheadline/PycharmProjects/Report/'+report_time+' 每日复盘/跳空下跌三颗星.txt'
if os.path.exists('/home/feheadline/PycharmProjects/Report/'+report_time+' 每日复盘'):
    message = 'file exists.'
    print message
else:
    os.makedirs('/home/feheadline/PycharmProjects/Report/'+report_time+' 每日复盘')
    print 'Created Report '+report_time+' 每日复盘'

f = open(report_address, 'a+')
f.write('跳空下跌三颗星\n')
f.write(report_time + '\n')
conn = MongoClient('localhost',27017)

#----------------------------------------------------------
#---------------------此处修改参数---------------------------

db = conn.db.data08
start = '2016-08-08'
span = 3
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
        print (1-round(data[i]['open']/data[i]['close'],2))
        if (1-round(data[i]['open']/data[i]['close'],2)) < -0.03 and\
            data[i+1]['open']>data[i+1]['close'] and data[i+2]['open']>data[i+2]['close'] and data[i+3]['open']>data[i+3]['close'] and\
                data[i+1]['open']<data[i]['low'] and data[i+2]['open']<data[i]['low'] and data[i+3]['open']<data[i]['low']:
                    print ''
                    print data[i+1]['tick'],data[i+1]['dt']
                    print ('----------------')
    del data[:]
    print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
    sys.stdout.flush()
