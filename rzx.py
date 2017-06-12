#!/usr/bin/env python
import telnetlib
import time
def rzx_telnet(ip,username,password1,password2,type):
	try:
		tn = telnetlib.Telnet(ip,timeout=5)
		time.sleep(1)
		tn.read_until('Username:')
		tn.write(username + '\r\n')
		tn.read_until('Password:')
		tn.write(password1 + '\r\n')
		if password2 != 'null':
			tn.write('enable\n')
			tn.write(password2 + '\r\n')
		time.sleep(1)
		r1 = tn.read_very_eager()
		filename = 'config/' + 'rzx.txt'
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
	password2 = "test"
	type = 'rzx'
	rzx_telnet(ip,username,password1,password2,type)
