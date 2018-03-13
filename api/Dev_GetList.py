#coding=utf-8
'''
获取设备列表:
Dev_GetList
request:
{
	"user_id":"1",				#设备所属的用户
	"limit":"10",
	"offset":"0",
}

return:
{
	"error":"SUCCESS",
	"all_cnt":10,		#共有10条记录
	"result":
	[
		{
			"dev_id":1,             #设备id
			"dev_addr":"00000001",  #设备地址
			"usage":"汽车",			#设备用途
			"power":100,			#电量
			"lat":39.111111,	·	#维度
			"lon":107.879865,		#经度
			"accury":10000,			#定位精度cm（10000 => 100m）
			"time_s":"2018-02-08 18:30:30.12345" #定位时间
		},
		...
	]
}
'''

def main(data):
	cip=data['client_ip']
	par=data['params']
	red=data['red']
	dbconn=data['dbconn']
	cur=data['dbcursor']
	cur.execute('''select d.dev_id,substr(dev_addr::text,3,16),usage,lat,lon,accuracy,time_s::text,d.power
			from device d left join locate_data l on d.last_locate_id=l.locate_id
			where user_id=%(user_id)s  limit %(limit)s offset %(offset)s'''%par)
	rows=cur.fetchall()
	dbconn.commit()

	rows_dict=[{'dev_id':r[0],'dev_addr':r[1],'usage':r[2],'lat':r[3],'lon':r[4],'accuracy':r[5],'time_s':r[6],'power':r[7]} for r in rows]	
	cur.execute(''' select count(dev_id) from device ''')
	cnt=cur.fetchone()
	res=dict(error='SUCCESS',all_cnt=cnt,result=rows_dict)
	return res
