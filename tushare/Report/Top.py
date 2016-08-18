# -*- coding:utf-8 -*-
# 0812 TOP list analysis

import schedule
import sys
import tick
from pymongo import MongoClient
conn = MongoClient('localhost',27017)
data = []
p_change =[]
#-9~9
Len_Positive_0 = []
Len_Positive_1 = []
Len_Positive_2 = []
Len_Positive_3 = []
Len_Positive_4 = []
Len_Positive_5 = []
Len_Positive_6 = []
Len_Positive_7 = []
Len_Positive_8 = []
Len_Positive_9 = []

Len_Negative_0 = []
Len_Negative_1 = []
Len_Negative_2 = []
Len_Negative_3 = []
Len_Negative_4 = []
Len_Negative_5 = []
Len_Negative_6 = []
Len_Negative_7 = []
Len_Negative_8 = []
Len_Negative_9 = []
#----------------------------------------------------------
#---------------------此处修改参数---------------------------


db = conn.db.data08
datalist = ['2016-08-12']


#----------------------------------------------------------
#---------------------此处修改参数---------------------------
ticklen = len(tick.tick)
count = 0
for ticki in tick.tick:
    for i in range(len(datalist)):
        for item in db.find({'dt':datalist[i],'tick':ticki}):
            data.append(item)
    for i in range(len(data)):
        if 0 <= data[i]['p_change'] <= 1:
            Len_Positive_0.append(data[i]['p_change'])
        if 1 <= data[i]['p_change'] <= 2:
            Len_Positive_1.append(data[i]['p_change'])
        if 2 <= data[i]['p_change'] <= 3:
            Len_Positive_2.append(data[i]['p_change'])
        if 3 <= data[i]['p_change'] <= 4:
            Len_Positive_3.append(data[i]['p_change'])
        if 4 <= data[i]['p_change'] <= 5:
            Len_Positive_4.append(data[i]['p_change'])
        if 5 <= data[i]['p_change'] <= 6:
            Len_Positive_5.append(data[i]['p_change'])
        if 6 <= data[i]['p_change'] <= 7:
            Len_Positive_6.append(data[i]['p_change'])
        if 7 <= data[i]['p_change'] <= 8:
            Len_Positive_7.append(data[i]['p_change'])
        if 8 <= data[i]['p_change'] <= 9:
            Len_Positive_8.append(data[i]['p_change'])
        if 9 <= data[i]['p_change'] <= 10:
            Len_Positive_9.append(data[i]['p_change'])
        if -1 <= data[i]['p_change'] <= 0:
            Len_Negative_0.append(data[i]['p_change'])
        if -2 <= data[i]['p_change'] <= -1:
            Len_Negative_1.append(data[i]['p_change'])
        if -3 <= data[i]['p_change'] <= -2:
            Len_Negative_2.append(data[i]['p_change'])
        if -4 <= data[i]['p_change'] <= -3:
            Len_Negative_3.append(data[i]['p_change'])
        if -5 <= data[i]['p_change'] <= -4:
            Len_Negative_4.append(data[i]['p_change'])
        if -6 <= data[i]['p_change'] <= -5:
            Len_Negative_5.append(data[i]['p_change'])
        if -7 <= data[i]['p_change'] <= -6:
            Len_Negative_6.append(data[i]['p_change'])
        if -8 <= data[i]['p_change'] <= -7:
            Len_Negative_7.append(data[i]['p_change'])
        if -9 <= data[i]['p_change'] <= -8:
            Len_Negative_8.append(data[i]['p_change'])
        if -10 <= data[i]['p_change'] <= -9:
            Len_Negative_9.append(data[i]['p_change'])
        # if data[i]['p_change'] > 5:
        #     count += 1
        #     print ''
        #     print ('No.'), count
        #     print data[i]['tick'], ' open ', data[i]['open'], 'close', data[i]['close']
        #     print ('----------------')
    del data[:]
    print '\r', '进度 :', tick.tick.index(ticki), '/', ticklen,
    sys.stdout.flush()


print '+0 : ', len(Len_Positive_0)
print '+1 : ', len(Len_Positive_1)
print '+2 : ', len(Len_Positive_2)
print '+3 : ', len(Len_Positive_3)
print '+4 : ', len(Len_Positive_4)
print '+5 : ', len(Len_Positive_5)
print '+6 : ', len(Len_Positive_6)
print '+7 : ', len(Len_Positive_7)
print '+8 : ', len(Len_Positive_8)
print '+9 : ', len(Len_Positive_9)
print '-0 : ', len(Len_Negative_0)
print '-1 : ', len(Len_Negative_1)
print '-2 : ', len(Len_Negative_2)
print '-3 : ', len(Len_Negative_3)
print '-4 : ', len(Len_Negative_4)
print '-5 : ', len(Len_Negative_5)
print '-6 : ', len(Len_Negative_6)
print '-7 : ', len(Len_Negative_7)
print '-8 : ', len(Len_Negative_8)
print '-9 : ', len(Len_Negative_9)

print '------------------------------'

print '+0 : ', round((len(Len_Positive_0)*1.00/2886)*1000,2), '‰', len(Len_Positive_0), '/', len(tick.tick)
print '+1 : ', round((len(Len_Positive_1)*1.00/2886)*1000,2), '‰', len(Len_Positive_1), '/', len(tick.tick)
print '+2 : ', round((len(Len_Positive_2)*1.00/2886)*1000,2), '‰', len(Len_Positive_2), '/', len(tick.tick)
print '+3 : ', round((len(Len_Positive_3)*1.00/2886)*1000,2), '‰', len(Len_Positive_3), '/', len(tick.tick)
print '+4 : ', round((len(Len_Positive_4)*1.00/2886)*1000,2), '‰', len(Len_Positive_4), '/', len(tick.tick)
print '+5 : ', round((len(Len_Positive_5)*1.00/2886)*1000,2), '‰', len(Len_Positive_5), '/', len(tick.tick)
print '+6 : ', round((len(Len_Positive_6)*1.00/2886)*1000,2), '‰', len(Len_Positive_6), '/', len(tick.tick)
print '+7 : ', round((len(Len_Positive_7)*1.00/2886)*1000,2), '‰', len(Len_Positive_7), '/', len(tick.tick)
print '+8 : ', round((len(Len_Positive_8)*1.00/2886)*1000,2), '‰', len(Len_Positive_8), '/', len(tick.tick)
print '+9 : ', round((len(Len_Positive_9)*1.00/2886)*1000,2), '‰', len(Len_Positive_9), '/', len(tick.tick)
print '-0 : ', round((len(Len_Negative_0)*1.00/2886)*1000,2), '‰', len(Len_Negative_0), '/', len(tick.tick)
print '-1 : ', round((len(Len_Negative_1)*1.00/2886)*1000,2), '‰', len(Len_Negative_1), '/', len(tick.tick)
print '-2 : ', round((len(Len_Negative_2)*1.00/2886)*1000,2), '‰', len(Len_Negative_2), '/', len(tick.tick)
print '-3 : ', round((len(Len_Negative_3)*1.00/2886)*1000,2), '‰', len(Len_Negative_3), '/', len(tick.tick)
print '-4 : ', round((len(Len_Negative_4)*1.00/2886)*1000,2), '‰', len(Len_Negative_4), '/', len(tick.tick)
print '-5 : ', round((len(Len_Negative_5)*1.00/2886)*1000,2), '‰', len(Len_Negative_5), '/', len(tick.tick)
print '-6 : ', round((len(Len_Negative_6)*1.00/2886)*1000,2), '‰', len(Len_Negative_6), '/', len(tick.tick)
print '-7 : ', round((len(Len_Negative_7)*1.00/2886)*1000,2), '‰', len(Len_Negative_7), '/', len(tick.tick)
print '-8 : ', round((len(Len_Negative_8)*1.00/2886)*1000,2), '‰', len(Len_Negative_8), '/', len(tick.tick)
print '-9 : ', round((len(Len_Negative_9)*1.00/2886)*1000,2), '‰', len(Len_Negative_9), '/', len(tick.tick)