#!/usr/bin/env python
import telnetlib
import time
def shenma_telnet(ip,username,password1,password2,type):
	try:
		tn = telnetlib.Telnet(ip,timeout=5)
		time.sleep(1)
		tn.read_until('login:')
		tn.write(username + '\r\n')
		tn.read_until('Password:')
		tn.write(password1 + '\r\n')
		if password2 != 'null':
			tn.write('enable\n')
			tn.write(password2 + '\n')
		tn.close()
		alert = ip + ' --> Login success'
		#print alert
	except Exception as e:
		alert = ip + ' --> Login failed'
		#print alert
	return alert
if __name__ == '__main__':
	ip = '11.11.11.11'
	username = "test"
	password1 = "test"
	password2 = "null"
	type = 'shenma'
	shenma_telnet(ip,username,password1,password2,type)
