#!/usr/bin/env python
import telnetlib
import time
def cisco_telnet(ip,username,password1,password2,type):
	try:
		tn = telnetlib.Telnet(ip,timeout=5)
		time.sleep(1)
		tn.write(username + '\r\n')
		time.sleep(1)
		tn.write(password1 + '\r\n')
		if password2 != 'null':
			tn.write('enable\n')
			tn.write(password2 + '\n')
		filename = 'config/' + 'cisco.txt'
		f = file(filename,'r')
		commands = f.readlines()
		for command in commands:
			tn.write(str(command) + '\r\n')
		time.sleep(1)
		tn.close()
		alert = tn.read_very_eager()
		#print alert
	except Exception as e:
		alert = ip + ' --> Login failed'
		#print alert
	return alert
if __name__ == '__main__':
	ip = '111.111.111.111'
	username = ""
	password1 = ""
	password2 = ""
	type = 'cisco'
	cisco_telnet(ip,username,password1,password2,type)
