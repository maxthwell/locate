#coding=utf-8
'''
删除设备:Dev_Del
request:
{
	"user_id":"1",				#设备所属的用户
	"dev_id":1,             	#模块的id
}

return:
{
	"error":"SUCCESS",			#
}
'''

def main(data):
	cip=data['client_ip']
	par=data['params']
	red=data['red']
	dbconn=data['dbconn']
	cur=data['dbcursor']
	assert('dev_id' in par)
	cur.execute('''delete from device where dev_id=%(dev_id)s'''%par)
	dbconn.commit()
	res=dict(error='SUCCESS')
	return res
