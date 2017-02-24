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
import socket
from pyvirtualdisplay import Display

def get_ip_table():
	try:
		cm = "ip route show "
		process = Popen([cm], stdout=PIPE, stderr=PIPE, shell=True)
		stdout, stderr = process.communicate()
		print('ip table: ', stdout, stderr)
	except Exception as e:
		print("get_ip_table",e)
		pass

def change_cwnd(tid, cwnd):
	try:
		cm = "sudo ttyecho -n %s ls"%(tid)
		print(cm)
		# cm = "sudo ttyecho -n %s 'python change_cwnd.py %s'"%(tid,cwnd)
		process = Popen([cm], stdout=PIPE, stderr=PIPE, shell=True)
		stdout, stderr = process.communicate()
		print('change cwnd: ', stdout, stderr)
	except Exception as e:
		print("change_cwnd",e)
		pass

def change_rto(val):
	process = Popen(["ip route show"], stdout=PIPE, stderr=PIPE, shell=True)
	stdout, stderr = process.communicate()
	output = stdout.decode("utf-8").strip()
	output = output.split('\n')
	for i in output:
		if "nameserver" not in i:
			if "rto_min" in i:
				vcv = i.split("rto_min")
				print(vcv)
				i = vcv[0]
			try:
				command = "sudo ip route change %s rto_min %s"%(i,val)
				# print(command)
				process = Popen([command], stdout=PIPE, stderr=PIPE, shell=True)
				stdout, stderr = process.communicate()
				print("change_rto",stderr,stdout)
				time.sleep(0.3)
			except Exception as e:
				print("change_rto:",e)

if __name__ == "__main__":
	display = Display(visible=0, size=(800, 600))
	display.start()
	sys.stdout = open("log3.txt", "a")
	try:
		# arr = []
		# arr.append(str(1))
		# c = csv.writer(open("flag_2.csv", "w"))
		# c.writerow(arr)
		print("*********")
		flag = 1
		time.sleep(10)
		for times in range(0,1000000):
			print("*********")
			time.sleep(3)
			fff = open('flag_cwnd_change.csv')
			csvfilefff = csv.reader(fff)
			for rowfff in csvfilefff:
				if (int(rowfff[0]) == str(1)):
					print("waiting")
				else:
					print("wait finished")
					flag = 0
			if flag == 0:
				break
		print('Free to proceed')
		time.sleep(5)				

		print("running xterm")
		site1 = str(sys.argv[1])
		cwnd = str(sys.argv[2])
		tid = str(sys.argv[3])
		prot = str(sys.argv[4])
		bw = str(sys.argv[5])
		loss = str(sys.argv[6])
		delay = str(sys.argv[7])
		abc = str(sys.argv[8])
		cork = str(sys.argv[9])
		low_lat = str(sys.argv[10])
		rto = str(sys.argv[11])
		ss = str(sys.argv[12])
		site = 'http://www.'+site1

		# get_ip_table()
		print(site,cwnd,tid,prot)

		# # change cwnd at server
		# change_cwnd(tid, cwnd)
		# for rto_load_time in range(0,2):
		for rto_load_time in range(0,1):
			# if rto_load_time == 0:
			# 	rto = 2*2*int(delay)
			# 	print("testing 2 rto",rto)
			# 	change_rto(rto)
			# else:
			# 	rto = 4*2*int(delay)
			# 	print("testing 4 rto",rto)
			# 	change_rto(rto)

			plt_arr = []
			for load_time in range(0,5):
				try:
					chromium_path = '/usr/bin/chromium-browser'
					chrome_options = webdriver.ChromeOptions()
					chrome_options.binary_location = chromium_path
					chrome_options.add_argument('--disable-application-cache')
					driver = webdriver.Chrome(executable_path='/home/usama/mm/chromedriver', chrome_options = chrome_options)
					time.sleep(1)
					end_time = 0
					start_time = time.time()
					driver.get(site)
					end_time = time.time()
					print('%s took %s to load.'%(site,end_time-start_time))
					plt_arr.append(end_time-start_time)
					driver.quit()
					time.sleep(1)

					try:
						print('Combining results')
						onload_time = end_time - start_time
						arr = []
						arr.append(load_time)
						arr.append(site1)
						arr.append(onload_time)
						#plt_arr.append(onload_time)
						arr.append(str(bw))
						arr.append(str(loss))
						arr.append(str(delay))
						arr.append(str(cwnd))
						arr.append(str(prot))
						arr.append(str(abc))
						arr.append(str(cork))
						arr.append(str(low_lat))
						arr.append(str(rto))
						arr.append(str(ss))
						arr.append(str(datetime.now()))
						c = csv.writer(open("plt_results.csv", "a", newline=''))
						c.writerow(arr)
					except Exception as e:
						print('5: ',e)		
				except Exception as e:
					print("site load:",e)
					driver.quit()
					pass

			try:
				plt_sum = sum(plt_arr)
				print("calculating avg")
				arr = []
				arr.append(site1)
				arr.append(plt_sum/len(plt_arr))
				arr.append(str(bw))
				arr.append(str(loss))
				arr.append(str(delay))
				arr.append(str(cwnd))
				arr.append(str(prot))
				arr.append(str(abc))
				arr.append(str(cork))
				arr.append(str(low_lat))
				arr.append(str(rto))
				arr.append(str(ss))
				for g in plt_arr:
					arr.append(g)
				#arr.append(plt_arr)
				c = csv.writer(open("plt_results_avg.csv", "a", newline=''))
				c.writerow(arr)
				
			except Exception as e:
				print("avg:",e)
				pass

		# time.sleep(10)
		# arr = []
		# arr.append(str(0))
		# c = csv.writer(open("flag_2.csv", "w"))
		# c.writerow(arr)

	except Exception as e:
		print(1,e)
		time.sleep(20)
		pass
	display.stop()
