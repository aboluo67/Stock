# -*- coding:utf-8 -*-
import sys
import tushare as ts
import json
import tick,dt
from pymongo import MongoClient
# 第一次数据入库后字段顺序　隔断时间再录入会有错误
# 可能只能按时间分成数据库
conn = MongoClient('localhost',27017)
ticklen = len(tick.tick)
for i in tick.tick:
    for y in dt.dt:
        try:
            df = ts.get_hist_data('' + i + '', start=y, end=y)
            list = json.loads(df.to_json(orient='records'))
            list[0][u'tick'] = i
            list[0][u'dt'] = y
            conn.db.data08.insert(list[0])
        except:
            print ('Yeah check No. '+ i + ' get something wrong')
    print '\r','进度 :',tick.tick.index(i),'/',ticklen,
    sys.stdout.flush()