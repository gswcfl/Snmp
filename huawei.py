#!/usr/bin/env python
import telnetlib
import time
def huawei_telnet(ip,username,password1,password2,type):
	try:
		tn = telnetlib.Telnet(ip,timeout=5)
		time.sleep(1)
		if tn.read_until('Username:',timeout=5):
			tn.write(username + '\r\n')
		else:
			tn.write(username + '\r\n')
		tn.read_until('Password:',timeout=5)
		tn.write(password1 + '\r\n')
		time.sleep(1)
		if password2 != 'null':
			tn.write('super\n')
			tn.write(password2 + '\r\n')
		r1 = tn.read_very_eager()
		filename = 'config/' + 'huawei.txt'
		f = file(filename,'r')
		commands = f.readlines()
		for command in commands:
			tn.write(str(command) + '\r\n')
		time.sleep(1)
		alert = tn.read_very_eager()
		tn.close()
	#	print alert
	except Exception as e:
		alert = ip + ' --> Login failed'
	#	print alert
	return alert
if __name__ == '__main__':
	ip = '11.11.11.11'
	username = "test"
	password1 = "test"
	password2 = "null"
	type = 'huawei'
	huawei_telnet(ip,username,password1,password2,type)
