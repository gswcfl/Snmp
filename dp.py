#!/usr/bin/env python
import telnetlib
import time
def dp_telnet(ip,username,password1,password2,type):
	try:
		tn = telnetlib.Telnet(ip,timeout=5)
		time.sleep(1)
		tn.write(username + '\r\n')
		tn.read_until('Password:')
		tn.write(password1 + '\r\n')
		time.sleep(1)
		if password2 != 'null':
			tn.write('conf-mode\r\n')
			tn.write(password2 + '\r\n')
		r1 = tn.read_very_eager()
		if type == 'DPX8000-A12':
			filename = 'config/' + 'dp_a12.txt'
		else:
			filename = 'config/' + 'dp.txt'
		f = file(filename,'r')
		commands = f.readlines()
		for command in commands:
			tn.write(str(command) + '\n')
		time.sleep(1)
		alert = tn.read_very_eager()
		tn.close()
		#print alert
	except Exception as e:
		alert = ip + ' --> Login failed'
		#print alert
	return alert
if __name__ == '__main__':
	ip = '111.111.111.111'
	username = "test"
	password1 = "test"
	password2 = "test"
	type = 'DP'
	dp_telnet(ip,username,password1,password2,type)
