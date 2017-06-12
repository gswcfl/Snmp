#!/usr/bin/env python
import telnetlib
import time
def zxr10_telnet(ip,username,password1,password2,type):
	try:
		tn = telnetlib.Telnet(ip,timeout=5)
		time.sleep(1)
		if tn.read_until('Username:'):
			tn.write(username + '\r\n')
		else:
			tn.write(username + '\r\n')
		tn.read_until('Password:')
		tn.write(password1 + '\r\n')
		if password2 != 'null':
			tn.write('enable\n')
			tn.write(password2 + '\r\n')
		r1 = tn.read_very_eager()
		if type == '9005':
			filename = 'config/' + 'zxr10_9005.txt'
		elif type == '8908' or type == 'ZXR10':
			filename = 'config/' + 'zxr10_8908.txt'
		else:
			filename = 'config/' + 'zxr10.txt'
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
	ip = '10.52.95.21'
	username = "special_g"
	password1 = "bj!@#_zg"
	password2 = "en_bj!2#"
	type = 'zxr10'
	zxr10_telnet(ip,username,password1,password2,type)
