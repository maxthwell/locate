#coding=utf-8
'''
添加设备:Dev_Add
request:
{
	"user_id":"1",				#设备所属的用户
	"usage":"car",              #模块所属的资产类型
	"dev_addr":"000000000001",	#模块的物理地址
}

return:
{
	"error":"SUCCESS",			#
	"dev_id":1,                 #该设备在平台下的唯一标识
}
'''

def main(data):
	cip=data['client_ip']
	par=data['params']
	red=data['red']
	dbconn=data['dbconn']
	cur=data['dbcursor']
	assert('usage' in par and 'dev_addr' in par)
	cur.execute('''insert into device (dev_addr,usage,user_id) values('\\x%(dev_addr)s','%(usage)s',%(user_id)s)returning dev_id'''%par)
	row=cur.fetchone()
	dbconn.commit()
	res=dict(error='SUCCESS',res=row)
	return res
