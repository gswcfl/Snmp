#!/usr/bin/env python
# -*- coding:utf-8 -*-
import xlrd
import commands
import os
import sys
import string
sys.path.append(os.path.dirname(os.path.abspath('__file__')))
from cisco import cisco_telnet
from h3c_telnet import h3c_telnet
from h3c_ssh import h3c_ssh
#from shenma import shenma_telnet
from zxr10 import zxr10_telnet
from dp import dp_telnet
from huawei import huawei_telnet
from ruijie import ruijie_telnet
from sugon import sugon_telnet
from force10 import force10_telnet
from rzx import rzx_telnet
from fiberhome import fiberhome_telnet
from result import result

global alert
alert = ''
data = xlrd.open_workbook("password.xls")
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
col_data = table.col_values(3)
for i in range(nrows):
	ip = str(table.row_values(i)[3])
	type = str(table.row_values(i)[4])
	changjia = str(table.row_values(i)[5])
	login = str(table.row_values(i)[6])
	username = str(table.row_values(i)[7])
	password1 = str(table.row_values(i)[8])
	password2 = str(table.row_values(i)[9])
#	if changjia == 'CISCO':
#		alert =	cisco_telnet(ip,username,password1,password2,type)
#		print ip + '\t' + 'done'
	##	result(ip,alert)
#	elif changjia == 'H3C' and login == 'telnet':
#		alert = h3c_telnet(ip,username,password1,password2,type)
#		print ip + '\t' + 'done'
#		result(ip,alert)
#	elif changjia == 'H3C' and login == 'ssh':
#		alert = h3c_ssh(ip,username,password1,password2,type)
#		print ip + '\t' + 'done'
#		result(ip,alert)
#	##elif changjia == 'SHENMA':
#	##	alert = shenma_telnet(ip,username,password1,password2,type)
#	##	result(ip,alert)
	if changjia == 'ZXR10':
		alert = zxr10_telnet(ip,username,password1,password2,type)
		print ip + '\t' + 'done'
#		result(ip,alert)
#	elif changjia == 'DP':
#		alert = dp_telnet(ip,username,password1,password2,type)
#		result(ip,alert)
	elif changjia == 'HUAWEI':
		alert = huawei_telnet(ip,username,password1,password2,type)
		print ip + '\t' + 'done'
#		result(ip,alert)
	elif changjia == 'RUIJIE':
		alert = ruijie_telnet(ip,username,password1,password2,type)
		print ip + '\t' + 'done'
#		result(ip,alert)
	elif changjia == 'SUGON':
		alert = sugon_telnet(ip,username,password1,password2,type)
		print ip + '\t' + 'done'
#		result(ip,alert)
	elif changjia == 'FORCE10':
		alert = force10_telnet(ip,username,password1,password2,type)
		print ip + '\t' + 'done'
#		result(ip,alert)
	elif changjia == 'RZX':
		alert = rzx_telnet(ip,username,password1,password2,type)
		print ip + '\t' + 'done'
#		result(ip,alert)
#	elif changjia == 'Fiberhome':
#		alert = fiberhome_telnet(ip,username,password1,password2,type)
#		print ip + '\t' + 'done'
#		result(ip,alert)
