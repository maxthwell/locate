#encoding=utf-8
import json
import os
import sys
import requests
url='http://192.168.10.117:11773/'

def req(api,_data):
	_url="%s%s"%(url,api)
	print(_url)
	r=requests.post(_url,data=json.dumps(_data),headers={"Content-Type":"application/json"})
	t=r.text
	print(_data)
	print(t)
	return t
	
if __name__=="__main__":
#	req("Dev_Add",_data={'user_id':1,'usage':'汽车','dev_addr':'00000001'})
#	req("Dev_GetList",_data={'user_id':1,'limit':100,'offset':0})
#	req("Locate_UpdateDevPosition",_data={"user_id":"1","lat":33.1111111,"lon":108.1111111,"dev_id":1})
	req("Locate_GetTrailById",_data={"user_id":"1","dev_id":1,"date":"2018-02-28","time_begin":"14:00:00","time_end":"15:00:00"})


