# -*- coding:utf-8 -*-
# 模仿回测 按照某只股票近几日的走势 查找近一段时间所有的股票是否有类似
import sys
import tick
import schedule
from pymongo import MongoClient
conn = MongoClient('localhost',27017)
# 回测数据
data = []
datalist = []
# 参照数据
reference_data = []
reference_datalist = []
#----------------------------------------------------------
#---------------------此处修改参数---------------------------

db = conn.db.data2016
reference_tick = '300282'
reference_start = '2016-04-15'
reference_span = 3

start = '2016-03-01'
span = 100

#----------------------------------------------------------
#---------------------此处修改参数---------------------------
print('——*——*——*————*——*——*————*——*——*————*——*——*———*——*——*——')
print('当 K 线 下 行 至 MA15 以 下 时,切 勿 冲 动 买 入 !!!')
print('——*——*——*————*——*——*————*——*——*————*——*——*———*——*——*——')

reference_index = schedule.schedule.index(reference_start)
for i in range(reference_index,reference_index + reference_span):
    reference_datalist.append(schedule.schedule[i])
    for item in db.find({'dt':schedule.schedule[i],'tick':reference_tick}):
        reference_data.append(item)

if reference_data == []:
    print reference_tick,'数据不存在,请确认是否停牌'
reference_day = []
for i in range(len(reference_data)):
    reference_day.append(round(reference_data[i]['close']/reference_data[i]['open'],2))

print 'reference_day:', (reference_day)
reference_data1 =[]
reference_data2 =[]
for i in reference_data:
    reference_data1.append(i-0.01)
    reference_data2.append(i+0.01)
print 'reference_data1:',reference_data1
print 'reference_data2:',reference_data2

datalistindex = schedule.schedule.index(start)

for i in range(datalistindex,datalistindex+span):
    datalist.append(schedule.schedule[i])

print('datalist:',len(datalist))
count = 0
data3 = []
ticklen = len(tick.tick)
for ticki in tick.tick:
    try:
        for i in range(len(datalist)):
            for item in db.find({'dt':datalist[i], 'tick':ticki}):
                data.append(item)
        # print len(data)
        # for i in range(reference_span-3):
        #     if (reference_day[i]*0.9)<(round(data[i]['close']/data[i]['open'],2))<(reference_day[i]*1.02):
        #         data3.append(data[i])
        # if len(data3) == reference_span:
        #     print ''
        #     print data3[0]['dt'],data3[0]['tick']
        #     print data3[0]['close']/data3[0]['open'],data3[1]['close']/data3[1]['open'],\
        #         data3[2]['close']/data3[2]['open']
        # del data3[:]
        # len1 = len(data)-len(reference_data)+1
        len1 = len(data)-reference_span+1
        data2 = []

        for i in range(len1):
            if reference_data1<round(data[i],2)<reference_data2




    except:pass
    del data[:]
    print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
    sys.stdout.flush()

    # a = [1, 2, 3, 4, 5, 6]
    # b = [2, 3, 4]
    # b1 = [1.9, 2.9, 3.9]
    # b2 = [2.1, 3.1, 4.1]
    # for i in range(len(a) - len(b) + 1):
    #     if b1 < a[i:i + len(b)] < b2:
    #         print 'O',
    #     else:
    #         print 'X',
#
# ['2016-04-15', '2016-04-18', '2016-04-19']
# reference_day [0.98, 0.99, 1.0]
# ('datalist:', 100)
# 进度 : 72 / 2886 2016-04-21 2016-04-22 2016-04-25
# 300392 300392 300392
# 0.91593046452 0.954470471791 1.005521049
# 进度 : 96 / 2886 2016-03-21 2016-03-22 2016-03-23
# 300087 300087 300087
# 0.997557003257 0.999163179916 0.972928630025
# 进度 : 151 / 2886