# -*- coding:utf-8 -*-
# 早晨十字星
# 十字星之后几天会放大量 后量维持稍微减少但股价继续上升 当高位量降低时 上升结束
#十字星有红绿 最好第一天跌幅能在input时手动输入%之多少 提示一般为X
#十字星上下影线长度灵活设定  是否上影线越长越好

# daily 35+

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

# MAC
# report_address = '/Users/zoutao/ichinascope数据/'+report_time+'-每日复盘/早晨十字星.txt'
# if os.path.exists('/Users/zoutao/ichinascope数据/'+report_time+'-每日复盘'):
#     message = 'file exists.'
#     print message
# else:
#     os.makedirs('/Users/zoutao/ichinascope数据/'+report_time+'-每日复盘')
#     print 'Created Report '+report_time+'-每日复盘'

# ubuntu
report_address = '/home/feheadline/PycharmProjects/ichinascope/Report/'+report_time+'-每日复盘/早晨十字星.txt'
if os.path.exists('/home/feheadline/PycharmProjects/ichinascope/Report/'+report_time+'-每日复盘'):
    message = 'file exists.'
    print message
else:
    os.makedirs('/home/feheadline/PycharmProjects/ichinascope/Report/'+report_time+'-每日复盘')
    print 'Created Report '+report_time+'-每日复盘'

#----------------------------------------------------------
#---------------------此处修改参数---------------------------

db = conn.db.data2016
start = '2016-07-11'
span = 2
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
#最好的出售时间TOP3,最高利润TOP3
bestday = []
bestprice = []
f = open(report_address, 'a+')
f.write('if i<len(data)-1 and ((1-round(data[i][\'open\']/data[i][\'close\'],2)) < -0.03):\n')
f.write('((data[i+1][\'close\']-data[i+1][\'open\'])/data[i+1][\'open\'] * 100)>-1.5:\n')
f.write('((data[i+1][\'close\']-data[i+1][\'open\'])/data[i+1][\'open\'] * 100) < 1.5::\n')
for ticki in tick.tick:
    for i in range(0,span):
        for item in db.find({'dt':datalist[i], 'tick':ticki}):
            data.append(item)
    for i in range(len(data)):
        if i<len(data)-1 and ((1-round(data[i]['open']/data[i]['close'],2)) < -0.03):
            if data[i+1]['open']>data[i+1]['close']:
                if ((data[i+1]['close']-data[i+1]['open'])/data[i+1]['open'] * 100)>-1.2:
                    count += 1
                    f = open(report_address, 'a+')
                    print('')
                    f.write('\n')
                    print ('No.'),count
                    f.write('No. '+str(count)+'\n')
                    print ('十字星系数:'),round(((data[i+1]['open']/data[i+1]['close'] - 1) * 100),2)
                    f.write('十字星系数:'+str(round(((data[i+1]['open']/data[i+1]['close'] - 1) * 100),2))+'\n')
                    print data[i]['tick']," 首日跌幅为4%以上 ", data[i]['dt'] ,"为早晨十字星 绿"
                    f.write(data[i]['tick'] + "首日跌幅为4%以上 "+ data[i]['dt'] + "为早晨十字星 绿"+'\n')
                    print ('%19s' % 'open '),('%8s' % 'close'),('%8s' % 'amplitude'),('%6s' % 'vol')
                    f.write(('%19s' % 'open ')+('%8s' % 'close')+('%8s' % 'amplitude')+('%6s' % 'vol')+'\n')
                    amplitudelist = []
                    for ii in range(i,len(data)):
                        amplitude = data[ii]['close']/data[i]['close']
                        amplitudelist.append(amplitude)
                    for ii in range(i,len(data)):
                        amplitude = data[ii]['close']/data[i]['close']
                        if amplitude == max(amplitudelist):
                            bestprice.append(round(amplitude,2))
                            print(data[ii]['dt']),('%8.2f' % data[ii]['open']),('%8.2f' % data[ii]['close']),\
                                '->',('%5.2f' % amplitude),('%8d' % (data[ii]['vol']/1000))
                            f.write((data[ii]['dt'])+('%8.2f' % data[ii]['open'])+('%8.2f' % data[ii]['close'])+\
                              ' ->'+('%5.2f' % amplitude)+('%8d' % (data[ii]['vol']/1000))+'\n')
                            # print('%6d' % (data[i]['amount']/1000000)),('%27s' % data[i]['macd'])
                        if amplitude != max(amplitudelist):
                            print(data[ii]['dt']),('%8.2f' % data[ii]['open']),('%8.2f' % data[ii]['close']),\
                                ('%8.2f' % amplitude),('%8d' % (data[ii]['vol']/1000))
                            f.write((data[ii]['dt'])+('%8.2f' % data[ii]['open'])+('%8.2f' % data[ii]['close'])+\
                              ('%8.2f' % amplitude)+('%8d' % (data[ii]['vol']/1000))+'\n')
                            # print('%6d' % (data[i]['amount']/1000000)),('%27s' % data[i]['macd'])
                    print ('----------------')
                    f.write('----------------\n')
            if data[i+1]['open']<data[i+1]['close']:
                if ((data[i+1]['close']-data[i+1]['open'])/data[i+1]['open'] * 100) < 1.2:
                    count += 1
                    f = open(report_address, 'a+')
                    print('')
                    f.write('\n')
                    print ('No.'),count
                    f.write('No. '+str(count)+'\n')
                    print ('十字星系数:'),round(((data[i+1]['open']/data[i+1]['close'] - 1) * 100),2)
                    f.write('十字星系数:'+str(round(((data[i+1]['open']/data[i+1]['close'] - 1) * 100),2))+'\n')
                    print data[i]['tick']," 首日跌幅为4%以上 ", data[i]['dt'] ,"为早晨十字星 红"
                    f.write(data[i]['tick'] + "首日跌幅为4%以上 "+ data[i]['dt'] + "为早晨十字星 红"+'\n')
                    print ('%19s' % 'open '),('%8s' % 'close'),('%8s' % 'amplitude'),('%6s' % 'vol')
                    f.write(('%19s' % 'open ')+('%8s' % 'close')+('%8s' % 'amplitude')+('%6s' % 'vol')+'\n')
                    amplitudelist = []
                    for ii in range(i,len(data)):
                        amplitude = data[ii]['close']/data[i]['close']
                        amplitudelist.append(amplitude)
                    for ii in range(i,len(data)):
                        amplitude = data[ii]['close']/data[i]['close']
                        if amplitude == max(amplitudelist):
                            bestprice.append(round(amplitude,2))
                            print(data[ii]['dt']),('%8.2f' % data[ii]['open']),('%8.2f' % data[ii]['close']),\
                                '->',('%5.2f' % amplitude),('%8d' % (data[ii]['vol']/1000))
                            f.write((data[ii]['dt'])+('%8.2f' % data[ii]['open'])+('%8.2f' % data[ii]['close'])+\
                               ' ->'+('%5.2f' % amplitude)+('%8d' % (data[ii]['vol']/1000))+'\n')
                            # print('%6d' % (data[i]['amount']/1000000)),('%27s' % data[i]['macd'])
                        if amplitude != max(amplitudelist):
                            print(data[ii]['dt']),('%8.2f' % data[ii]['open']),('%8.2f' % data[ii]['close']),\
                                ('%8.2f' % amplitude),('%8d' % (data[ii]['vol']/1000))
                            f.write((data[ii]['dt'])+('%8.2f' % data[ii]['open'])+('%8.2f' % data[ii]['close'])+\
                              ('%8.2f' % amplitude)+('%8d' % (data[ii]['vol']/1000))+'\n')
                            # print('%6d' % (data[i]['amount']/1000000)),('%27s' % data[i]['macd'])
                    print ('----------------')
                    f.write('----------------\n')
    del data[:]
    print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
    sys.stdout.flush()
print '\n'
print '平均最好收益：',round((sum(bestprice)*1.0)/len(bestprice),2)
print bestprice

f.close()

