# -*- coding:utf-8 -*-
# 平底(钳子底)

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

report_time = time.strftime("%Y-%m-%d %H:%M", time.localtime())

# MAC
# report_address = '/Users/zoutao/ichinascope数据/'+report_time+'-每日复盘/平底(钳子底).txt'
# if os.path.exists('/Users/zoutao/ichinascope数据/'+report_time+'-每日复盘'):
#     message = 'file exists.'
#     print message
# else:
#     os.makedirs('/Users/zoutao/ichinascope数据/'+report_time+'-每日复盘')
#     print 'Created Report '+report_time+'-每日复盘'

# ubuntu
report_address = '/home/feheadline/PycharmProjects/Report/'+report_time+' 每日复盘/平底(钳子底).txt'
if os.path.exists('/home/feheadline/PycharmProjects/Report/'+report_time+' 每日复盘'):
    message = 'file exists.'
    print message
else:
    os.makedirs('/home/feheadline/PycharmProjects/Report/'+report_time+' 每日复盘')
    print 'Created Report '+report_time+' 每日复盘'

f = open(report_address, 'a+')
f.write('平底(钳子底)\n')
f.write(report_time + '\n')

#----------------------------------------------------------
#---------------------此处修改参数---------------------------

db = conn.tushare.data0812
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
        for item in db.find({'JYR':datalist[i], 'JYDM':ticki}):
            data.append(item)
    for i in range(len(data)-1):
        if (data[i+1]['low']*0.98)<data[i]['low']<(data[i+1]['low']*1.01):
            print ''
            f.write('\n')
            print data[i+1]['JYDM'],data[i+1]['JYR']
            f.write('\n')
            print ('----------------')
            f.write('----------------\n')
    del data[:]
    print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
    sys.stdout.flush()
