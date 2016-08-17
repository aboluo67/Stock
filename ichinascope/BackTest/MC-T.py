# -*- coding:utf-8 -*-
# 回测  早晨十字星
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
start = '2016-07-11'
span = 6

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
            if (1-round(data[i]['open']/data[i]['close'],2)) < -0.04 :
                if data[i+1]['open']>data[i+1]['close']:
                    # if ((data[i+1]['open']/data[i+1]['close'] - 1) * 100) < 0.5:
                        count += 1
                        print('')
                        print ('No.'),count
                        # 十字星系数好像有点不对　问题不严重
                        print ('十字星系数'),round(((data[i+1]['open']/data[i+1]['close'] - 1) * 100),2)
                        # print ('十字星系数'),round(((data[i]['open']/data[i]['close'] - 1) * 100),2)
                        print ('%17s' % 'open '),('%7s' % 'close'),('%9s' % '| close')
                        print data[i]['dt'],\
                            '%8.2f' % data[i]['open'],\
                            '%8.2f' % data[i]['close']
                        print data[i+1]['dt'],\
                            '%8.2f' % data[i+1]['open'],\
                            '%8.2f' % data[i+1]['close']
                        print data[i+2]['dt'],'%8.2f' % data[i+2]['close']
                        print data[i+3]['dt'],'%8.2f' % data[i+3]['close']
                        print data[i+4]['dt'],'%8.2f' % data[i+4]['close']
                        print data[i+5]['dt'],'%8.2f' % data[i+5]['close']
                        # print data[i+6]['dt'],'%8.2f' % data[i+6]['close']
                        # print data[i+7]['dt'],'%8.2f' % data[i+7]['close']
                        # print data[i+8]['dt'],'%8.2f' % data[i+8]['close']
                        # print data[i+9]['dt'],'%8.2f' % data[i+9]['close']
                        print(data[i]['tick']),('  前一日跌幅为4%以上 今日为早晨十字星 绿')
                        for i in range(0,len(data)):
                            print(data[i]['dt']),('%8.2f' % data[i]['close']),('%6d' % (data[i]['vol']/1000))\
                                ,('%6d' % (data[i]['amount']/1000000)),('%27s' % data[i]['macd'])
                        print ('----------------')
        except:pass
    del data[:]
    print '\r','进度 :',tick.tick.index(ticki),'/',ticklen,
    sys.stdout.flush()