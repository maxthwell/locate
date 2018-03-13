#coding=utf-8
'''
更新节点的定位信息:Locate_UpdateDevPosition
request:
{
	"user_id":"1",				#设备所属的用户
	"lat":33.1111111,           #经度
	"lon":108.1111111,          #维度
	"dev_id":1,					#模块的id
	"accuracy":100,				#定位经度为100单位cm
	"time_s":"2018-02-28 17:23:20.111" #定位时间
	"power":100,				#电量为百分数
	"locate_method":"GPS"       #定位方式为GPS
}

return:
{
	"error":"SUCCESS"
}
'''

def main(data):
	cip=data['client_ip']
	par=data['params']
	red=data['red']
	dbconn=data['dbconn']
	cur=data['dbcursor']
	assert('lat' in par and 'lon' in par)
	assert('dev_id' in par)
	assert('power' in par)
	assert('accuracy' in par)
	assert('time_s' in par)
	sql='''with new_locatedata as (
			insert into locate_data (lat,lon,accuracy,dev_id,time_s,power,locate_method)
			values(%(lat)s,%(lon)s,%(accuracy)s,%(dev_id)s,'%(time_s)s',%(power)s,'%(locate_method)s') returning locate_id) 
		update device set last_locate_id = (select locate_id from new_locatedata limit 1), power=%(power)s  where dev_id=%(dev_id)s
		'''%par
	cur.execute(sql)
#row=cur.fetchone()
	dbconn.commit()
	res=dict(error='SUCCESS')
	return res
