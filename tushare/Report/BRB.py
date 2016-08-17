# -*- coding:utf-8 -*-
# 两红夹一黑

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import time
import sys
from tushare import tick
import schedule
from pymongo import MongoClient

report_time = time.strftime("%Y-%m-%d %H时%M分", time.localtime())

# MAC
# report_address = '/Users/zoutao/Report/'+report_time+'-每日复盘/两红夹一黑.txt'
# if os.path.exists('/Users/zoutao/Report/'+report_time+'-每日复盘'):
#     message = 'file exists.'
#     print message
# else:
#     os.makedirs('/Users/zoutao/Report/'+report_time+'-每日复盘')
#     print 'Created Report '+report_time+'-每日复盘'

# ubuntu
report_address = '/home/feheadline/PycharmProjects/Report/'+report_time+' 每日复盘/两红夹一黑.txt'
if os.path.exists('/home/feheadline/PycharmProjects/Report/'+report_time+' 每日复盘'):
    message = 'file exists.'
    print message
else:
    os.makedirs('/home/feheadline/PycharmProjects/Report/'+report_time+' 每日复盘')
    print 'Created Report '+report_time+' 每日复盘'

f = open(report_address, 'a+')
f.write('两红夹一黑\n')
f.write(report_time + '\n')

conn = MongoClient('localhost',27017)

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
    for i in range(len(data)-3):
        if data[i]['ma10'] != None and data[i]['ma20'] != None:
            if data[i]['close']>((data[i]['ma20']+data[i]['ma10'])*1.0/2):
                if data[i]['open']<data[i]['close'] and data[i+1]['open']>data[i+1]['close'] and data[i+2]['open']<data[i+2]['close']:
                    if data[i]['close']>data[i+1]['open'] and data[i+1]['open']<data[i+2]['close']:
                        if data[i]['open'] < (data[i + 1]['close']) and (data[i + 1]['close']) > data[i + 2]['open']:
                            count += 1
                            print ''
                            f.write('\n')
                            print 'No.', count
                            f.write('No.'+ str(count) +'\n')
                            print data[i]['JYDM'], data[i]['JYR'],data[i+3]['price_change']
                            f.write(str(data[i]['JYDM'])+' '+str(data[i]['JYR'])+' '+str(data[i+3]['price_change'])+'\n')
                            print ('----------------')
    del data[:]
    print '\r','进度 :', tick.tick.index(ticki), '/',ticklen,
    sys.stdout.flush()
