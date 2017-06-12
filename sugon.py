#!/usr/bin/env python
import telnetlib
import time
def sugon_telnet(ip,username,password1,password2,type):
	try:
		tn = telnetlib.Telnet(ip,timeout=5)
		time.sleep(10)
		if tn.read_until('name:'):
			tn.write(username + '\r\n')
		else:
			tn.write(username + '\r\n')
		time.sleep(1)
		tn.write(password1 + '\r\n')
		if password2 != 'null':
			tn.write('enable\r\n')
			tn.write(password2 + '\r\n')
		time.sleep(10)
		r1 = tn.read_very_eager()
		if type == 'S214':
			filename = 'config/' + 'sugon_s214.txt'
		elif type == 'N3100':
			filename = 'config/' + 'sugon_n3100.txt'
		f = file(filename,'r')
		commands = f.readlines()
		for command in commands:
			tn.write(str(command) + '\r\n')
			time.sleep(1)
		time.sleep(1)
		alert = tn.read_very_eager()
		tn.close()
	#	print alert
	except Exception as e:
		alert = ip + ' --> Login failed'
	#	print alert
	return alert
if __name__ == '__main__':
	ip = '10.52.87.3'
	username = "admin"
	password1 = "admin"
	password2 = "null"
	type = 'S214'
	sugon_telnet(ip,username,password1,password2,type)
