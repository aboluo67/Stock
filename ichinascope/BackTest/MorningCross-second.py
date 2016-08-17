# -*- coding:utf-8 -*-
# 早晨十字星
# 再加一个第三根K线的 收盘价超第一次的开盘价
#时间问题 停牌问题　停牌因素是否引起计数图形的无效性
import sys
import tick
import schedule
from pymongo import MongoClient
conn = MongoClient('localhost',27017)
data = []
datalist = []
#十字星有红绿 最好第一天跌幅能在input时手动输入%之多少 提示一般为X
#十字星上下影线长度灵活设定  是否上影线越长越好
#----------------------------------------------------------
#---------------------此处修改参数---------------------------

db = conn.db.data2016
start = '2016-01-04'
span = 30

#----------------------------------------------------------
#---------------------此处修改参数---------------------------
print('——*——*——*————*——*——*————*——*——*————*——*——*———*——*——*——')
print('当 K 线 下 行 至 MA15 以 下 时,切 勿 冲 动 买 入 !!!')
print('——*——*——*————*——*——*————*——*——*————*——*——*———*——*——*——')


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
        # 跌幅大于４％　0.04
        try:
            for i in range(len(data)):
                if (1-round(data[i]['open']/data[i]['close'],2)) < -0.04 :
                    if data[i+1]['open'] > data[i+1]['close']:
                        if ((data[i+1]['open']/data[i+1]['close'] - 1) * 100) < 0.5:
                            count += 1
                            print ''
                            print 'No: ', count
                            print '十字星系数', round(((data[i+1]['open']/data[i+1]['close'] - 1) * 100),2)
                            print data[i]['tick'], '  前一日跌幅为4%以上 今日为早晨十字星 绿'
                            print '%28s' % 'close ', '%4s' % 'rate', '%5s' % 'vol'
                            maxclose = []
                            for i in range(len(data)):
                                maxclose.append(data[i]['close'])
                            for i in range(len(data)):
                                if i == maxclose.index(max(maxclose)):
                                    print 'Day:','%2s' % (i+1),(data[i]['dt']),'<-', \
                                        ('%5.2f' % data[i]['close']),\
                                        ('%5.2f' % round(data[i]['close']/data[0]['close'],2)),\
                                        ('%7d' % (data[i]['vol']/1000))\
                                        ,('%6d' % (data[i]['amount']/1000000)),('%27s' % data[i]['macd'])
                                else:
                                    print 'Day:','%2s' % (i+1),(data[i]['dt']), ('%8.2f' % data[i]['close']),('%5.2f' % round(data[i]['close']/data[0]['close'],2)), ('%6d' % (data[i]['vol']/1000))\
                                        ,('%6d' % (data[i]['amount']/1000000)),('%27s' % data[i]['macd'])
                    if data[i+1]['open'] < data[i+1]['close']:
                        if ((data[i+1]['open']/data[i+1]['close'] - 1) * 100) < 0.5:
                            count += 1
                            print ''
                            print 'No: ', count
                            print '十字星系数', round(((data[i+1]['open']/data[i+1]['close'] - 1) * 100),2)
                            print '%17s' % 'open ', '%7s' % 'close'
                            print data[i]['tick'], '  前一日跌幅为4%以上 今日为早晨十字星 红'
                            print '%28s' % 'close ', '%4s' % 'rate', '%5s' % 'vol'
                            maxclose = []
                            for i in range(len(data)):
                                maxclose.append(data[i]['close'])
                            for i in range(len(data)):
                                if i == maxclose.index(max(maxclose)):
                                    print 'Day:','%2s' % (i+1),(data[i]['dt']),'<-', \
                                        ('%5.2f' % data[i]['close']),\
                                        ('%5.2f' % round(data[i]['close']/data[0]['close'],2)),\
                                        ('%7d' % (data[i]['vol']/1000))\
                                        ,('%6d' % (data[i]['amount']/1000000)),('%27s' % data[i]['macd'])
                                else:
                                    print 'Day:','%2s' % (i+1),(data[i]['dt']), ('%8.2f' % data[i]['close']),('%5.2f' % round(data[i]['close']/data[0]['close'],2)), ('%6d' % (data[i]['vol']/1000))\
                                        ,('%6d' % (data[i]['amount']/1000000)),('%27s' % data[i]['macd'])
        except:pass
    del data[:]
    print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
    sys.stdout.flush()