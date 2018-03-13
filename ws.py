#coding=utf-8
from websocket import WebSocketApp
import pdb
import sys
import os
import hashlib
import time
import json
import sys
import re
import struct
import redis
import numpy as np
from scipy.optimize import leastsq
import requests

restyapi_url='http://192.168.10.117:11773/'
def req(api,_data):
	_url="%s%s"%(restyapi_url,api)
	print(_url)
	r=requests.post(_url,data=json.dumps(_data),headers={"Content-Type":"application/json"})
	t=r.text
	print(_data)
	print(t)
	return t
	

def Deal(msg):
	data=msg['data']
	time_s=msg['time_s']
	a=int(data[18:24],16)
	b=int(data[24:30],16)
	a*=(90./8388608.)
	b*=(180./8388608.)
	print('lat:',a)
	print('lon:',b)
	req("Locate_UpdateDevPosition",_data={"user_id":"1","lat":a,"lon":b,"dev_id":43,"time_s":time_s,"accuracy":10000,"locate_method":"GPS","power":80})


def on_message(ws, message):
	try:
		msg=json.loads(message)
	except:
		return
	dev_eui=msg['devEUI']
	if dev_eui != '0000000000004715':
		return
	Deal(msg)

def on_error(ws, error):
	print('error:%s'%(error,))

def on_close(ws):
	print ("#closed#")

def on_open(ws):
	print ('#open#')

def calDistance(rssi):
	pass

def _run():
	prm={'appEUI':'0000000000000028','User_Sec':'39d01e51dbb720a03231fee159b00341','time_s':'13456788902'}
	prm['token']=hashlib.md5((prm['time_s']+prm['appEUI']+prm['User_Sec']).encode('utf-8')).hexdigest()
	wsuri='''ws://115.29.186.49:92/webs?appEUI=%(appEUI)s&token=%(token)s&time_s=%(time_s)s'''%prm
	ws = WebSocketApp(wsuri,on_message=on_message,on_error=on_error,on_close=on_close,on_open=on_open)
	ws.run_forever()

if __name__=='__main__':
	_run()
