#!/usr/bin/env python
import time
import pexpect
import sys

def h3c_ssh(ip,username,password1,password2,type):
	try:
		ssh = pexpect.spawn('ssh %s@%s' %(username,ip))
		i = ssh.expect(['password:','Are you sure you want to continue connecting (yes/no)?'],timeout=5)
		time.sleep(1)
		if i == 0:
			ssh.sendline(password1)
		elif i == 1:
			ssh.sendline('yes')
			ssh.expect('password:')
			ssh.sendline(password1)
		time.sleep(1)
		if password2 != 'null':
			ssh.expect('>')
			time.sleep(1)
			ssh.sendline('super')
			ssh.sendline(password2)
		time.sleep(1)
		ssh.expect('>')
		filename = 'config/' + 'h3c.txt'
		f = file(filename,'r')
		commands = f.readlines()
		for command in commands:
			ssh.sendline(command)
		for i in range(15):
			ssh.sendline('\n')
		ssh.expect('>')
		alert = ssh.before
	#	print alert
	except Exception as e:
		alert = ip + ' --> Login failed'
	#	print alert
	return alert

if __name__ == '__main__':
	ip = '11.11.11.11'
	username = 'test'
	password1 = 'test'
	password2 = 'test'
	type = 'h3c'
	h3c_ssh(ip,username,password1,password2,type)
