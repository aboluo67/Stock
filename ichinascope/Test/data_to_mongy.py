#!/usr/bin/env python
#encoding:utf-8
import datetime
import md5
import re
import threading
import time

import numpy
import tushare as ts
from pymongo import MongoClient


def IsNumber(x):
	 if re.match(r'^\d+\.?\d+$', x) == None:
		 return False
	 return True

def IsFloat(x):
	 if type(x) is float:
	 	 return True
	 if re.match(r'^\d+\.\d+$', x) == None:
		 return False
	 return True

def IsInt(x):
	if type(x) is int:
		return True
	if x=='0':
		return True
	if re.match(r'^[1-9]\d*$', x) == None:
		return False
		return True

def DataFrameToMongo(df, collection, id_field=[], id_prefix=''):
	'''
	df : Pandas DataFrame
	collection: mongodb collection
	id_field: identifield field. Especially, '__index__' means index name
	id_prefix: prefix for id string
	'''
	if df is not None and not df.empty:
		for x in df.index:
			row = df.ix[x]
			m  = md5.new()
			if id_field:
				fg =  ''.join([row.ix[f] if f is not '__index__' else row.name for f in id_field]).encode('utf-8')
				m.update(id_prefix+fg)
				id = m.hexdigest()
			else:
				m.update(time.time())
				id = m.hexdigest()
			data = {'_id': id}
			for k in row.index:
				v = row.ix[k]
				if type(v) is numpy.int8 or type(v) is numpy.int16  or type(v) is numpy.int32  or type(v) is numpy.int64  or type(v) is numpy.uint8  or type(v) is numpy.uint16  or type(v) is numpy.uint32  or type(v) is numpy.uint64  or type(v) is numpy.float16   or type(v) is numpy.float32  or type(v) is numpy.float64  or type(v) is numpy.complex64  or type(v) is numpy.complex128:
				# if isinstance(v, numpy.dtype):
					data[k] = numpy.asscalar(v)
				# if isinstance(k, float):
					# data[k] = float(v)
				# elif isinstance(k, int):
					# data[k] = int(v)
				elif IsFloat(v):
					data[k] = float(v)
				elif IsInt(v):
					data[k] = int(v)
				else:
					data[k] = v

			if df.index.name:
				data[df.index.name] = row.name
			if id_prefix:
				data['did'] = id_prefix
			data['updated'] = int(time.time()*1000)
			collection.update_one(
				{ '_id': id },
				{ '$set': data},
				upsert = True
			)
			# collection.update_one(
			# 	{ '_id': id },
			# 	{ '$set': data, '$push': { 'updated' : int(time.time()*1000)} },
			# 	upsert = True
			# )
			# print 'insert data to mongo: %s'%data


mongourl = 'mongodb://mongodb.feheadline.net:27017/'
stocklist = []

def sync_stock_list():
	'''
	get stock list only
	'''
	global stocklist
	df = ts.get_stock_basics()
	stocklist = df.index.tolist()

def sync_stock_basics():
	'''
	stock basic info, stock list
	'''
	global stocklist
	df = ts.get_stock_basics()
	stocklist = df.index.tolist()
	DataFrameToMongo(df, MongoClient(mongourl)['stoinfo']['stock'], ['__index__'])

def sync_stock_month_history():
	'''
	stock monthly history
	'''
	today_str = datetime.datetime.now().strftime(u'%Y-%m-%d')
	yesterday_str = datetime.date.fromordinal(datetime.date.today().toordinal()-60).strftime(u'%Y-%m-%d')
	for k in stocklist:
		df = ts.get_hist_data(code=k, start=yesterday_str, end=today_str, ktype='M')
		DataFrameToMongo(df, MongoClient(mongourl)['stoinfo']['history_month'], ['__index__'], k)

def sync_stock_week_history():
	'''
	stock weekly history
	'''
	today_str = datetime.datetime.now().strftime(u'%Y-%m-%d')
	yesterday_str = datetime.date.fromordinal(datetime.date.today().toordinal()-7).strftime(u'%Y-%m-%d')
	for k in stocklist:
		df = ts.get_hist_data(code=k, start=yesterday_str, end=today_str, ktype='W')
		DataFrameToMongo(df, MongoClient(mongourl)['stoinfo']['history_week'], ['__index__'], k)

def sync_stock_day_history():
	'''
	stock daily history
	'''
	today_str = datetime.datetime.now().strftime(u'%Y-%m-%d')
	yesterday_str = datetime.date.fromordinal(datetime.date.today().toordinal()-1).strftime(u'%Y-%m-%d')
	for k in stocklist:
		df = ts.get_hist_data(code=k, start=yesterday_str, end=today_str, ktype='D')
		DataFrameToMongo(df, MongoClient(mongourl)['stoinfo']['history_day'], ['__index__'], k)

def sync_stock_minutes_history():
	'''
	stock minutes history
	'''
	today_str = datetime.datetime.now().strftime(u'%Y-%m-%d')
	yesterday_str = datetime.date.fromordinal(datetime.date.today().toordinal()-1).strftime(u'%Y-%m-%d')
	for k in stocklist:
		df = ts.get_hist_data(code=k, start=yesterday_str, end=today_str, ktype='5')
		DataFrameToMongo(df, MongoClient(mongourl)['stoinfo']['history_5min'], ['__index__'], k)
		df = ts.get_hist_data(code=k, start=yesterday_str, end=today_str, ktype='15')
		DataFrameToMongo(df, MongoClient(mongourl)['stoinfo']['history_15min'], ['__index__'], k)
		df = ts.get_hist_data(code=k, start=yesterday_str, end=today_str, ktype='30')
		DataFrameToMongo(df, MongoClient(mongourl)['stoinfo']['history_30min'], ['__index__'], k)
		df = ts.get_hist_data(code=k, start=yesterday_str, end=today_str, ktype='60')
		DataFrameToMongo(df, MongoClient(mongourl)['stoinfo']['history_60min'], ['__index__'], k)

def sync_stock_today():
	'''
	sync current stock data
	'''
	df = ts.get_today_all()
	DataFrameToMongo(df, MongoClient(mongourl)['stoinfo']['quotes'], ['code'])

def sync_market_today():
	'''
	sync current market data
	'''
	df = ts.get_index()
	DataFrameToMongo(df, MongoClient(mongourl)['stoinfo']['market'], ['code'])


def sync_movie_data():
	'''
	movie boxoffice data
	'''
	df = ts.realtime_boxoffice()
	# df.to_excel('movie.xlsx',encoding='utf-8')
	# records = json.loads(df.T.to_json()).values()
	DataFrameToMongo(df, MongoClient(mongourl)['stoinfo']['movie'], ['MovieName'])
	# collection.insert(records)

def sync_report_data():
	'''
	sync report data
	'''
	year = datetime.datetime.now().year
	month = datetime.datetime.now().month
	seaon = month/3
	if month<3:
		year = year - 1
		seaon = 4
	monthstr = '%s%s'%(year,seaon)
	DataFrameToMongo(ts.get_report_data(year, seaon), MongoClient(mongourl)['stoinfo']['report_data'], ['code'], monthstr)

def sync_profit_data():
	'''
	sync profit data
	'''
	year = datetime.datetime.now().year
	month = datetime.datetime.now().month
	seaon = month/3
	if month<3:
		year = year - 1
		seaon = 4
	monthstr = '%s%s'%(year,seaon)
	DataFrameToMongo(ts.get_profit_data(year, seaon), MongoClient(mongourl)['stoinfo']['profit_data'], ['code'], monthstr)

def sync_operation_data():
	'''
	sync operation data
	'''
	year = datetime.datetime.now().year
	month = datetime.datetime.now().month
	seaon = month/3
	if month<3:
		year = year - 1
		seaon = 4
	monthstr = '%s%s'%(year,seaon)
	DataFrameToMongo(ts.get_operation_data(year, seaon), MongoClient(mongourl)['stoinfo']['operation_data'], ['code'], monthstr)

def sync_growth_data():
	'''
	sync growth data
	'''
	year = datetime.datetime.now().year
	month = datetime.datetime.now().month
	seaon = month/3
	if month<3:
		year = year - 1
		seaon = 4
	monthstr = '%s%s'%(year,seaon)
	DataFrameToMongo(ts.get_growth_data(year, seaon), MongoClient(mongourl)['stoinfo']['growth_data'], ['code'], monthstr)

def sync_debtpaying_data():
	'''
	sync debtpaying data
	'''
	year = datetime.datetime.now().year
	month = datetime.datetime.now().month
	seaon = month/3
	if month<3:
		year = year - 1
		seaon = 4
	monthstr = '%s%s'%(year,seaon)
	DataFrameToMongo(ts.get_debtpaying_data(year, seaon), MongoClient(mongourl)['stoinfo']['debtpaying_data'], ['code'], monthstr)

def sync_cashflow_data():
	'''
	sync cashflow data
	'''
	year = datetime.datetime.now().year
	month = datetime.datetime.now().month
	seaon = month/3
	if month<3:
		year = year - 1
		seaon = 4
	monthstr = '%s%s'%(year,seaon)
	DataFrameToMongo(ts.get_cashflow_data(year, seaon), MongoClient(mongourl)['stoinfo']['cashflow_data'], ['code'], monthstr)

class Scheduler(threading.Thread):
	def __init__(self, func, interval):
		super(Scheduler, self).__init__()
		self.func = func
		self.interval = interval

	def run(self):
        	while True:
        		print '\nExecuting func %s'%self.func.func_name
        		tmp_interval = self.interval
        		try:
        			self.func()
        		except Exception as e:
        			print '\nException in ',self.func.func_name,': ',e
        			tmp_interval = 60
        		print '\nSleeping func %s %s s'%(self.func.func_name,tmp_interval)
                	time.sleep(tmp_interval)

if __name__ == '__main__':
	sync_stock_list()
	s1 = Scheduler(sync_stock_basics, 86400)
	s1.daemon = True
	s1.start()
	s2 = Scheduler(sync_stock_today, 120)
	s2.daemon = True
	s2.start()
	s3 = Scheduler(sync_stock_minutes_history, 300)
	s3.daemon = True
	s3.start()
	s4 = Scheduler(sync_stock_day_history, 86400)
	s4.daemon = True
	s4.start()
	s5 = Scheduler(sync_stock_week_history, 86400*5)
	s5.daemon = True
	s5.start()
	s6 = Scheduler(sync_stock_month_history, 86400*21)
	s6.daemon = True
	s6.start()
	s7 = Scheduler(sync_movie_data, 3600)
	s7.daemon = True
	s7.start()
	s8 = Scheduler(sync_market_today, 300)
	s8.daemon = True
	s8.start()
	s9 = Scheduler(sync_report_data, 86400)
	s9.daemon = True
	s9.start()
	s10 = Scheduler(sync_profit_data, 86400)
	s10.daemon = True
	s10.start()
	s11 = Scheduler(sync_operation_data, 86400)
	s11.daemon = True
	s11.start()
	s12 = Scheduler(sync_growth_data, 86400)
	s12.daemon = True
	s12.start()
	s13 = Scheduler(sync_debtpaying_data, 86400)
	s13.daemon = True
	s13.start()
	s14 = Scheduler(sync_cashflow_data, 86400)
	s14.daemon = True
	s14.start()
	while True:
        	print 'Sync stock info scheduler running...'
        	time.sleep(3600)
