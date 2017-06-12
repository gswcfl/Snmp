#!/usr/bin/env python
import telnetlib
import time
def force10_telnet(ip,username,password1,password2,type):
	try:
		tn = telnetlib.Telnet(ip,timeout=5)
		time.sleep(1)
		tn.write(username + '\r\n')
		tn.read_until('Password:')
		tn.write(password1 + '\r\n')
		if password2 != 'null':
			tn.write('enable\r\n')
			tn.write(password2 + '\r\n')
		r1 = tn.read_very_eager()
		filename = 'config/' + 'force10.txt'
		f = file(filename,'r')
		commands = f.readlines()
		for command in commands:
			tn.write(str(command) + '\r\n')
		time.sleep(1)
		alert = tn.read_very_eager()
		tn.close()
		#print alert
	except Exception as e:
		alert = ip + ' --> Login failed'
		#print alert
	return alert
if __name__ == '__main__':
	ip = '11.11.11.11'
	username = "test"
	password1 = "test"
	password2 = "test"
	type = 'force10'
	force10_telnet(ip,username,password1,password2,type)
