# -*- coding:utf-8 -*-
# 每日复盘
import time

# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

import calendar

cal = calendar.month(2016, 1)
print "以下输出2016年1月份的日历:"
print cal

cal = calendar
print "以下输出2016年1月份的日历:"
print cal