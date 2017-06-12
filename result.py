#!/usr/bin/env python

import os
def result(ip,alert):
	file_name = 'result/' + ip + '.txt'
	command_clear = '> ' + file_name
	os.system(command_clear)
	f = file(file_name,'a+')
	f.write(ip)
	f.write(alert)
	f.flush()
	f.close()
	print ip + '\t' + 'done'
