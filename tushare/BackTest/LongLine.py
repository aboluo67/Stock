# -*- coding:utf-8 -*-
# longline
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
report_time = time.strftime("%Y-%m-%d %H-%M", time.localtime())



db = conn.db.data08
start = '2016-08-16'
span = 1
data = []
count = 0
ticklen = len(tick.tick)
for ticki in tick.tick:
    for item in db.find({'dt':'2016-08-16', 'tick':ticki}):
        data.append(item)
    for i in range(len(data)):
        # if data[i]['close']>((data[i]['ma10']+data[i]['ma20'])/2):
            if data[i]['open']<data[i]['close']:
                if (data[i]['high']-data[i]['open'])!=0 and \
                                ((data[i]['open']-data[i]['low'])*1.00/(data[i]['high']-data[i]['open']))>2:
                        count += 1
                        print('')
                        print ('No.'),count
                        print data[i]['tick'], data[i]['dt']
                        print ('----------------')
            if data[i]['open']>data[i]['close']:
                if (data[i]['high']-data[i]['close'])!=0 and \
                                ((data[i]['close']-data[i]['low'])*1.00/(data[i]['high']-data[i]['close']))>2:
                        count += 1
                        print('')
                        print ('No.'),count
                        print data[i]['tick'], data[i]['dt']
                        print ('----------------')
    del data[:]
    print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
    sys.stdout.flush()
