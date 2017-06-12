#!/usr/bin/env python
import xlrd
import commands
def ping()
	data = xlrd.open_workbook('password_info.xls')
	table = data.sheets()[0]
	nrows = table.nrows
	ncols = table.ncols
	col_data = table.col_values(3)
	for i in range(1,len(col_data)):
		command = 'ping ' + col_data[i] + ' -c 3 -i 0.2 -w 0.2'
		(status,output) = commands.getstatusoutput(command)
