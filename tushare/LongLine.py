# -*- coding:utf-8 -*-
# longline
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import time
import sys
import tick
import dt
from pymongo import MongoClient
conn = MongoClient('localhost',27017)
report_time = time.strftime("%Y-%m-%d %H-%M", time.localtime())

# MAC
report_address = '/Users/zoutao/ichinascope数据/'+report_time+'-每日复盘/早晨十字星.txt'
if os.path.exists('/Users/zoutao/ichinascope数据/'+report_time+'-每日复盘'):
    message = 'file exists.'
    print message
else:
    os.makedirs('/Users/zoutao/ichinascope数据/'+report_time+'-每日复盘')
    print 'Created Report '+report_time+'-每日复盘'

db = conn.db.data0812
start = '2016-08-12'
span = 1
data = []
count = 0
ticklen = len(tick.JYDM)
for ticki in tick.JYDM:
    for item in db.find({'JYR':'2016-08-12', 'JYDM':ticki}):
        data.append(item)
    for i in range(len(data)):
        if data[i]['close']>((data[i]['ma10']+data[i]['ma20'])/2):
            if data[i]['open']>data[i]['close']:
                if (data[i]['close']-data[i]['low'])!=0 and ((1-round(data[i]['open']/data[i]['close'],2)) > -0.03):
                    if ((data[i]['high']-data[i]['open'])*1.00/(data[i]['close']-data[i]['low']))>15:
                        count += 1
                        f = open(report_address, 'a+')
                        print('')
                        f.write('\n')
                        print ('No.'),count
                        f.write('No. '+str(count)+'\n')
                        # print ('长下阴线系数:'),round(((data[i+1]['open']/data[i+1]['close'] - 1) * 100),2)
                        # f.write('十字星系数:'+str(round(((data[i+1]['open']/data[i+1]['close'] - 1) * 100),2))+'\n')
                        print data[i]['JYDM'], data[i]['JYR']
                        f.write(data[i]['JYDM'] + "      "+ data[i]['JYR'] + '\n')
                        # print ('%19s' % 'open '),('%8s' % 'close'),('%8s' % 'amplitude'),('%6s' % 'vol')
                        # f.write(('%19s' % 'open ')+('%8s' % 'close')+('%8s' % 'amplitude')+('%6s' % 'vol')+'\n')
                        # amplitudelist = []
                        # for ii in range(i,len(data)):
                        #     amplitude = data[ii]['close']/data[i]['close']
                        #     amplitudelist.append(amplitude)
                        # for ii in range(i,len(data)):
                        #     amplitude = data[ii]['close']/data[i]['close']
                        #     if amplitude == max(amplitudelist):
                        #         bestprice.append(round(amplitude,2))
                        #         print(data[ii]['JYR']),('%8.2f' % data[ii]['open']),('%8.2f' % data[ii]['close']),\
                        #             '->',('%5.2f' % amplitude),('%8d' % (data[ii]['vol']/1000))
                        #         f.write((data[ii]['JYR'])+('%8.2f' % data[ii]['open'])+('%8.2f' % data[ii]['close'])+\
                        #           ' ->'+('%5.2f' % amplitude)+('%8d' % (data[ii]['vol']/1000))+'\n')
                        #         # print('%6d' % (data[i]['amount']/1000000)),('%27s' % data[i]['macd'])
                        #     if amplitude != max(amplitudelist):
                        #         print(data[ii]['JYR']),('%8.2f' % data[ii]['open']),('%8.2f' % data[ii]['close']),\
                        #             ('%8.2f' % amplitude),('%8d' % (data[ii]['vol']/1000))
                        #         f.write((data[ii]['JYR'])+('%8.2f' % data[ii]['open'])+('%8.2f' % data[ii]['close'])+\
                        #           ('%8.2f' % amplitude)+('%8d' % (data[ii]['vol']/1000))+'\n')
                        #         # print('%6d' % (data[i]['amount']/1000000)),('%27s' % data[i]['macd'])
                        print ('----------------')
                        f.write('----------------\n')
            if data[i]['open']<data[i]['close']:
                if (data[i]['high']-data[i]['close'])!=0 and ((data[i]['close']-data[i]['open'])/data[i]['open'] * 100) < 2:
                    if ((data[i]['open']-data[i]['low'])*1.00/(data[i]['high']-data[i]['close']))>15:
                        count += 1
                        f = open(report_address, 'a+')
                        print('')
                        f.write('\n')
                        print ('No.'),count
                        f.write('No. '+str(count)+'\n')
                        # print ('十字星系数:'),round(((data[i+1]['open']/data[i+1]['close'] - 1) * 100),2)
                        # f.write('十字星系数:'+str(round(((data[i+1]['open']/data[i+1]['close'] - 1) * 100),2))+'\n')
                        print data[i]['JYDM'], data[i]['JYR']
                        f.write(data[i]['JYDM'] + "      "+ data[i]['JYR'] + '\n')
                        # print ('%19s' % 'open '),('%8s' % 'close'),('%8s' % 'amplitude'),('%6s' % 'vol')
                        # f.write(('%19s' % 'open ')+('%8s' % 'close')+('%8s' % 'amplitude')+('%6s' % 'vol')+'\n')
                        # amplitudelist = []
                        # for ii in range(i,len(data)):
                        #     amplitude = data[ii]['close']/data[i]['close']
                        #     amplitudelist.append(amplitude)
                        # for ii in range(i,len(data)):
                        #     amplitude = data[ii]['close']/data[i]['close']
                        #     if amplitude == max(amplitudelist):
                        #         bestprice.append(round(amplitude,2))
                        #         print(data[ii]['JYR']),('%8.2f' % data[ii]['open']),('%8.2f' % data[ii]['close']),\
                        #             '->',('%5.2f' % amplitude),('%8d' % (data[ii]['vol']/1000))
                        #         f.write((data[ii]['JYR'])+('%8.2f' % data[ii]['open'])+('%8.2f' % data[ii]['close'])+\
                        #            ' ->'+('%5.2f' % amplitude)+('%8d' % (data[ii]['vol']/1000))+'\n')
                        #         # print('%6d' % (data[i]['amount']/1000000)),('%27s' % data[i]['macd'])
                        #     if amplitude != max(amplitudelist):
                        #         print(data[ii]['JYR']),('%8.2f' % data[ii]['open']),('%8.2f' % data[ii]['close']),\
                        #             ('%8.2f' % amplitude),('%8d' % (data[ii]['vol']/1000))
                        #         f.write((data[ii]['JYR'])+('%8.2f' % data[ii]['open'])+('%8.2f' % data[ii]['close'])+\
                        #           ('%8.2f' % amplitude)+('%8d' % (data[ii]['vol']/1000))+'\n')
                        #         # print('%6d' % (data[i]['amount']/1000000)),('%27s' % data[i]['macd'])
                        print ('----------------')
                        f.write('----------------\n')
    del data[:]
    print '\r','进度 :',tick.JYDM.index(ticki), '/',ticklen,
    sys.stdout.flush()

