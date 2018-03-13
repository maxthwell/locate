#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, abort, request, jsonify,make_response
from flask_cors import *
from functools import wraps
import json
import redis
from psycopg2 import pool as pgpool
from importlib import import_module as dimport
app = Flask(__name__)
CORS(app, supports_credentials=True)

#添加redis与postgresql连接池
redis_pool=redis.ConnectionPool(host='127.0.0.1', port=6379,db=2)
pg_conn_pool = pgpool.SimpleConnectionPool(5,200,
		host = '127.0.0.1',port='15432',user='locate',
		password='dbpassword',dbname='locate')

def resp(body):
	r = jsonify(body)
	r.headers['Access-Control-Allow-Origin'] = '*'
	return r 

@app.route('/<apiname>', methods=['POST'])
def post_opration(apiname):
	params=request.json
	print('params=>',params)
	red=redis.Redis(connection_pool=redis_pool)
	db=pg_conn_pool.getconn()
	cursor=db.cursor()
	func=getattr(dimport('api.%s'%apiname),'main')
	print('client_ip=>',request.remote_addr)
	res=func(dict(dbconn=db,dbcursor=cursor,red=red,client_ip=request.remote_addr,params=params))
	print(res)
	cursor.close()
	pg_conn_pool.putconn(db)
	return resp(res)

def run():
	return app.run(host="0.0.0.0", port=11773, debug=True)

if __name__ == "__main__":
	run()
