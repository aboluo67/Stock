# -*- coding:utf-8 -*-
# 早晨十字星

# 再加一个第三根K线的 收盘价超第一次的开盘价
#时间问题 停牌问题　停牌因素是否引起计数图形的无效性
import schedule
import sys
import tick
from pymongo import MongoClient
conn = MongoClient('localhost',27017)
data = []
#十字星有红绿 最好第一天跌幅能在input时手动输入%之多少 提示一般为X
#十字星上下影线长度灵活设定  是否上影线越长越好
#----------------------------------------------------------
#---------------------此处修改参数---------------------------


db = conn.db.data08
datalist = ['2016-08-08','2016-08-09']


#----------------------------------------------------------
#---------------------此处修改参数---------------------------
ticklen = len(tick.tick)
count = 0
for ticki in tick.tick:
    for i in range(0,2):
        for item in db.find({'dt':datalist[i],'tick':ticki}):
            data.append(item)
    for i in range(len(data)):
        if len(data) == 2:
            if (1-round(data[0]['open']/data[0]['close'],2)) < -0.04 :
                # print (1-round(data[0]['open']/data[0]['close'],2))
                # print(data[0]['open'], data[0]['close']), (data[1]['open'], data[1]['close'])
                if data[1]['open']>data[1]['close']:
                    if ((data[1]['open']/data[1]['close'] - 1) * 100) < 0.5:
                        count += 1
                        print ('No.'),count
                        # 十字星系数好像有点不对　问题不严重
                        print ('十字星系数'),round(((data[1]['open']/data[1]['close'] - 1) * 100),2)
                        print data[0]['dt'],' open ',data[0]['open'],'close',data[0]['close']
                        print data[1]['dt'],' open ',data[1]['open'],'close',data[1]['close']
                        print(data[0]['tick']),('  前一日跌幅为4%以上 今日为早晨十字星 绿')
                        print ('----------------')
                if data[1]['open'] < data[1]['close']:
                    if ((data[1]['close'] / data[1]['open'] - 1) * 100) < 0.5:
                        count += 1
                        print ('No.'),count
                        print ('十字星系数'), round(((data[1]['open'] / data[1]['close'] - 1) * 100), 2)
                        print data[0]['dt'], ' open ', data[0]['open'], 'close', data[0]['close']
                        print data[1]['dt'], ' open ', data[1]['open'], 'close', data[1]['close']
                        print(data[0]['tick']), ('  前一日跌幅为4%以上 今日为早晨十字星 红')
                        print ('----------------')
    del data[:]
    print '\r', '进度 :', tick.tick.index(ticki), '/', ticklen,
    sys.stdout.flush()
