# -*- coding:utf-8 -*-
# 模仿回测 按照某只股票近几日的走势 查找近一段时间所有的股票是否有类似
import sys
import tick
import schedule
from pymongo import MongoClient
conn = MongoClient('localhost',27017)
data = []
datalist = []
reference_data = []
reference_datalist = []
#----------------------------------------------------------
#---------------------此处修改参数---------------------------

db = conn.db.data2016
reference_tick = '600149'
reference_start = '2016-07-25'
reference_span = 5

start = '2016-03-23'
span = 10

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
# print(reference_data)
print reference_datalist
if reference_data == []:
    print reference_tick,'数据不存在,请确认是否停牌'
reference_day = []
for i in range(len(reference_data)):
    reference_day.append(round(reference_data[i]['close']/reference_data[i]['open'],2))

print(reference_day)
reference_day1 = reference_day[0]
reference_day2 = reference_day[1]
reference_day3 = reference_day[2]
reference_day4 = reference_day[3]
reference_day5 = reference_day[4]
datalistindex = schedule.schedule.index(start)

for i in range(datalistindex,datalistindex+span):
    datalist.append(schedule.schedule[i])

print(datalist)
count = 0
ticklen = len(tick.tick)
for ticki in tick.tick:
    for i in range(0,span):
        for item in db.find({'dt':datalist[i],'tick':ticki}):
            data.append(item)
    if data != []:
        try:
            for i in range(len(data)):
                if (reference_day1*0.99) < (data[i]['close']/data[i]['open']) < (reference_day1*1.01):
                    if (reference_day2*0.99) < (data[i+1]['close']/data[i+1]['open']) < (reference_day2*1.01):
                        if (reference_day3*0.99) < (data[i+2]['close']/data[i+2]['open']) < (reference_day3*1.01):
                            print(data[i]['tick'],data[i]['dt'])
        except:pass
    del data[:]
    print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
    sys.stdout.flush()