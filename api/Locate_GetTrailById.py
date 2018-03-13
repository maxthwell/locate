#coding=utf-8
'''
查询设备的轨迹：
request:
{
	"user_id":"1",			#设备所属的用户
	"dev_id":1,				#设备id
	"date":"2018-02-07",	#日期
	"time_begin":"10:10:00",#开始时间
	"time_end":"11:00:00",	#结束时间
}

return:
--返回一系列的坐标，前端根据坐标生产轨迹
{
	"error":"SUCCESS",
	"result":
		[{
			"time_s":"00:00:10",
			"lat":33.1234332,
			"lon":107.1234332,
			"power":10000,
			"locate_method":"GPS",
			"accuracy":10000,
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
	assert('date' in par)
	assert('dev_id' in par)
	if 'time_begin' not in par:
		data['time_begin']='00:00:00'
	if 'time_end' not in par:
		data['time_end']='23:59:59'
	cur.execute(''' select substr(time_s::text,12,13),lat,lon,power,locate_method,accuracy from locate_data where dev_id=%(dev_id)s and time_s between '%(date)s %(time_begin)s' and '%(date)s %(time_end)s' and lat>0 order by time_s'''%par)
	rows=cur.fetchall()
	dbconn.commit()
	res=dict(error='SUCCESS',result=[{'time_s':r[0],'lat':r[1],'lon':r[2],'power':r[3],'locate_method':r[4],'accuracy':r[5]} for r in rows])
	return res
