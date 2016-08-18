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
report_time = time.strftime("%Y-%m-%d %H时%M分", time.localtime())

# MAC
# report_address = '/Users/zoutao/Report/'+report_time+'-每日复盘/锤头线.txt'
# if os.path.exists('/Users/zoutao/Report/'+report_time+'-每日复盘'):
#     message = 'file exists.'
#     print message
# else:
#     os.makedirs('/Users/zoutao/Report/'+report_time+'-每日复盘')
#     print 'Created Report '+report_time+'-每日复盘'

# ubuntu
report_address = '/home/feheadline/PycharmProjects/Report/'+report_time+' 每日复盘/锤头线.txt'
if os.path.exists('/home/feheadline/PycharmProjects/Report/'+report_time+' 每日复盘'):
    message = 'file exists.'
    print message
else:
    os.makedirs('/home/feheadline/PycharmProjects/Report/'+report_time+' 每日复盘')
    print 'Created Report '+report_time+' 每日复盘'

f = open(report_address, 'a+')
f.write('锤头线\n')
f.write(report_time + '\n')
conn = MongoClient('localhost',27017)

#-----------------------------------------------------------
#---------------------此处修改参数---------------------------

db = conn.db.data08
start = '2016-08-08'
span = 1
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
                count += 1
                print ''
                f.write('\n')
                print 'No: ',count
                f.write('No:'+ str(count) + '\n')
                print '倒锤头线-红'
                f.write('倒锤头线-红\n')
                print data[i]['tick'],data[i]['dt']
                f.write(str(data[i]['tick'])+ str(data[i]['dt']) + '\n')
                print ('----------------')
            # 收阴
        if data[i]['close']<data[i]['open']:
            if (data[i]['high']/data[i]['close'])/(data[i]['open']/data[i]['close'])>1.05:
                count += 1
                print ''
                f.write('\n')
                print 'No: ', count
                f.write('No:' + str(count) + '\n')
                print '倒锤头线-绿'
                f.write('倒锤头线-绿\n')
                print data[i]['tick'], data[i]['dt']
                f.write(str(data[i]['tick']) + str(data[i]['dt']) + '\n')
                print ('----------------')

        if data[i]['close']>data[i]['open']:
            if (data[i]['open']/data[i]['low'])/(data[i]['open']/data[i]['close'])<1.04:
                count += 1
                print ''
                f.write('\n')
                print 'No: ',count
                f.write('No:'+ str(count) + '\n')
                print '倒锤头线-红'
                f.write('倒锤头线-红\n')
                print data[i]['tick'],data[i]['dt']
                f.write(str(data[i]['tick'])+ str(data[i]['dt']) + '\n')
                print ('----------------')

        if data[i]['close']<data[i]['open']:
            if (data[i]['close']/data[i]['low'])/(data[i]['close']/data[i]['open'])<1.04:
                count +=1
                print ''
                f.write('\n')
                print 'No: ', count
                f.write('No:' + str(count) + '\n')
                print '倒锤头线-绿'
                f.write('倒锤头线-绿\n')
                print data[i]['tick'], data[i]['dt']
                f.write(str(data[i]['tick']) + str(data[i]['dt']) + '\n')
                print ('----------------')
    del data[:]
    print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
    sys.stdout.flush()
