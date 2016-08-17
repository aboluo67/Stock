# -*- coding:utf-8 -*-
# 突破前期高位
#300158 突破前期高位 0701 突破前2.5个月 取前去平均值对应0701值(缩小范围)
#上5日线 突破 0701
import sys
import tick
import schedule
from pymongo import MongoClient
conn = MongoClient('localhost',27017)
# 回测数据
data = []
datalist = []
#----------------------------------------------------------
#---------------------此处修改参数---------------------------

db = conn.db.data2016
start = '2016-03-23'
# span = 15
span = 65

#----------------------------------------------------------
#---------------------此处修改参数---------------------------
print('——*——*——*————*——*——*————*——*——*————*——*——*———*——*——*——')
print('当 K 线 下 行 至 MA15 以 下 时,切 勿 冲 动 买 入 !!!')
print('——*——*——*————*——*——*————*——*——*————*——*——*———*——*——*——')

datalistindex = schedule.schedule.index(start)

for i in range(datalistindex,datalistindex+span):
    datalist.append(schedule.schedule[i])

print datalist

dataclose = []
ticklen = len(tick.tick)
for ticki in tick.tick:
    try:
        for i in range(len(datalist)):
            for item in db.find({'dt':datalist[i], 'tick':ticki}):
                data.append(item)
        # data65 = []
        # for i in range(65):
        #     data65.append(data[i]['close'])
        # if (max(data65[:6])/min(data65[6:12]))>1.1 and data[11]['close']>data[10]['close'] and \
        #                 data[11]['close'] > max(data65[:11])*0.7:
        #     print ''
        #     print 'data12'
        #     print data[0]['dt'], data[0]['tick'], '--', data[11]['dt']
        # if (max(data65[:8])/min(data65[8:15]))>1.1 and data[15]['close']>data[14]['close'] and \
        #                 data[15]['close'] > max(data65[:15])*0.7:
        #     print ''
        #     print 'data15'
        #     print data[0]['tick'], data[0]['dt'], '--', data[14]['dt']
        # if (max(data65[:10])/min(data65[10:20]))>1.1 and data[20]['close']>data[19]['close'] and \
        #                 data[20]['close'] > max(data65[:20])*0.7:
        #     print ''
        #     print 'data20'
        #     print data[0]['tick'], data[0]['dt'], '--', data[19]['dt']
        # if (max(data65[:13])/min(data65[13:25]))>1.1 and data[20]['close']>data[24]['close'] and \
        #                 data[25]['close'] > max(data65[:25])*0.7:
        #     print ''
        #     print 'data25'
        #     print data[0]['tick'], data[0]['dt'], '--', data[24]['dt']
        data12 = []
        for i in range(12):
            # print max(data[i].['close'])
            data12.append(data[i]['close'])
        if (max(data12[:6])/min(data12[6:12]))>1.1 and data[11]['close']>data[10]['close'] and \
                        data[11]['close'] > max(data12)*0.7:
            print ''
            print 'data12'
            print data[0]['dt'], data[0]['tick'], '--', data[11]['dt']
        data15 = []
        for i in range(15):
            # print max(data[i].['close'])
            data15.append(data[i]['close'])
        if (max(data12[:8])/min(data12[8:15]))>1.1 and data[15]['close']>data[14]['close'] and \
                        data[15]['close'] > max(data15)*0.7:
            print ''
            print 'data15'
            print data[0]['tick'], data[0]['dt'], '--', data[14]['dt']
        data20 = []
        for i in range(20):
            # print max(data[i].['close'])
            data20.append(data[i]['close'])
        if (max(data20[:10])/min(data20[10:20]))>1.1 and data[20]['close']>data[19]['close'] and \
                        data[20]['close'] > max(data20)*0.7:
            print ''
            print 'data20'
            print data[0]['tick'], data[0]['dt'], '--', data[19]['dt']
        data25 = []
        for i in range(25):
            # print max(data[i].['close'])
            data25.append(data[i]['close'])
        if (max(data25[:13])/min(data25[13:25]))>1.1 and data[25]['close']>data[24]['close'] and \
                        data[25]['close'] > max(data25)*0.7:
            print ''
            print 'data25'
            print data[0]['tick'], data[0]['dt'],  '--', data[24]['dt']
    except:pass
    del data[:]
    print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
    sys.stdout.flush()