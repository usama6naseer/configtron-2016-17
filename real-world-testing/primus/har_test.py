import json
from datetime import datetime
import subprocess
from subprocess import Popen, PIPE
import csv
import math
import os
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver import ActionChains
import socket
# def change_delay(prev, new):
# 	# tc qdisc to check delay
# 	try:
# 		cm = "sudo tc qdisc del dev eno1 root netem delay " + str(prev) + "ms"
# 		process = Popen([cm], stdout=PIPE, stderr=PIPE, shell=True)
# 		stdout, stderr = process.communicate()
# 		print "del delay",stdout
# 		print "del delay",stderr
# 	except Exception,e:
# 		print "error in del delay",e
# 	time.sleep(1)
# 	try:
# 		cm = "sudo tc qdisc add dev eno1 root netem delay " + str(new) + "ms"
# 		process = Popen([cm], stdout=PIPE, stderr=PIPE, shell=True)
# 		stdout, stderr = process.communicate()
# 		print "add delay",stdout
# 		print "add delay",stderr
# 	except Exception,e:
# 		print "error in add delay",e
# 	time.sleep(1)


if __name__ == "__main__":
	try:
		# process = Popen(["sudo tc qdisc del dev eno1 root netem delay 100ms"], stdout=PIPE, stderr=PIPE, shell=True)
		# stdout, stderr = process.communicate()
		# print stdout
		# print stderr

		# process = Popen(["sudo tc qdisc add dev eno1 root netem delay 0ms"], stdout=PIPE, stderr=PIPE, shell=True)
		# stdout, stderr = process.communicate()
		# print stdout
		# print stderr

		# f = webdriver.FirefoxProfile('/home/usama/.mozilla/firefox/gf55s9ay.t2')
		# f.set_preference('devtools.netmonitor.har.defaultLogDir','/home/usama/proxitron/har')
		# f.set_preference('devtools.netmonitor.har.enableAutoExportToFile',True)
		# f.set_preference('extensions.netmonitor.har.contentAPIToken','test')
		# f.set_preference('extensions.netmonitor.har.autoConnect',True)
		# ext_path = 'harexporttrigger-0.5.0-beta.10.xpi'
		# f.add_extension(extension=ext_path)
		# f.set_preference('browser.cache.disk.enable',False)
		# driver = webdriver.Firefox(firefox_profile=f)
		# # driver.set_script_timeout(10)

		# time.sleep(1)
		# # print "loading:",site
		# end_time = 0
		# start_time = time.time()
		# socket.setdefaulttimeout(5)
		# try:
		# 	driver.get('http://152.3.144.154/replay/www.instagram.com')
		# except socket.timeout:
		# 	print "timedout"		
		# end_time = time.time()
		# plt = end_time - start_time
					
		# f = open('alexa_top_500.csv')
		# csvfile = csv.reader(f)
		# for row in csvfile:
		# 	if (int(row[0]) == 2):
		# 		break
		
		# 	site = "http://www." + str(row[1])
		# 	# har_name = str(row[1]) + str(datetime.now())
		# 	har_name = 'google'
		# 	# read har
		# 	try:
		# 		with open('har/'+ har_name +'.har') as data_file:    
		# 			data = json.load(data_file)
		# 			# print(data)
		# 			log = data['log']
		# 			creator = log['creator']
		# 			entries = log['entries']
		# 			pages = log['pages']
		# 			browser = log['browser']
		# 			total = 0
		# 			obj_num = 0
		# 			for i in entries:
		# 				print(obj_num, i['time'])
		# 				obj_num = obj_num + 1 
		# 				total = total + i['time']

		# 	except Exception, e:
		# 		print "error in reading HAR", e			
	except Exception, e:
		print('1', e)
