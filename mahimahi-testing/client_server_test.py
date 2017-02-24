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
import _thread
import threading
from pyvirtualdisplay import Display

def get_ip_table():
	try:
		cm = "ip route show "
		process = Popen([cm], stdout=PIPE, stderr=PIPE, shell=True)
		stdout, stderr = process.communicate()
		output = stdout.decode("utf-8").strip()
		output = output.split('\n')
		for i in output:
			print(i)
		# print('ip table: ', stdout, stderr)
	except Exception as e:
		print("get_ip_table",e)
		time.sleep(10)
		pass

def get_tid():
	try:
		cm = "tty"
		process = Popen([cm], stdout=PIPE, stderr=PIPE, shell=True)
		stdout, stderr = process.communicate()
		output = stdout.decode("utf-8").strip()
		output = output.split('\n')
		res = str(output[0])
		print('tty: ', res, stdout, stderr)
		return res		
	except Exception as e:
		print("det_tid",e)
		time.sleep(10)
		pass

def change_cw(t,val):
	process = Popen(["ip route show"], stdout=PIPE, stderr=PIPE, shell=True)
	stdout, stderr = process.communicate()
	output = stdout.decode("utf-8").strip()
	output = output.split('\n')
	for i in output:
		if "nameserver" not in i:
			if "initcwnd" in i:
				vcv = i.split("initcwnd")
				i = vcv[0]
			print("sudo ip route change %s initcwnd %s"%(i,val))
			# time.sleep(5)
			process = Popen(["sudo ip route change %s initcwnd %s"%(i,val)], stdout=PIPE, stderr=PIPE, shell=True)
			stdout, stderr = process.communicate()
			print(stderr)
			print(stdout)
			time.sleep(0.5)
	arr = []
	arr.append(str(0))
	c = csv.writer(open("flag_cwnd_change.csv", "w"))
	c.writerow(arr)

def open_xterm(t,site, delay, loss, bw, terminal_id, cwnd, prot, abc, cork, low_lat, rto, ss):
	try:
		# cm = 'xterm -e "mm-delay %s mm-loss uplink %s mm-link link/%s link/%s python client_test.py %s %s %s %s"'%(delay,loss,bw,bw,site,cwnd,terminal_id,prot)
		cm = 'xterm -e "mm-delay %s mm-loss uplink %s mm-link link/%s link/%s python3 client_test.py %s %s %s %s %s %s %s %s %s %s %s %s"'%(delay,loss,bw,bw,site,cwnd,terminal_id,prot,bw,loss,delay,abc,cork,low_lat,rto,ss)
		# cm = 'gnome-terminal -e "mm-delay %s mm-loss uplink %s mm-link link/%s link/%s python3 client_test.py %s %s %s %s"'%(delay,loss,bw,bw,site,cwnd,terminal_id,prot)
		# cm = 'xterm'
		# cm = 'urxvt &'
		# print(cm)
		process = Popen([cm], stdout=PIPE, stderr=PIPE, shell=True)
		# process = Popen([cm])
		stdout, stderr = process.communicate()
		print('xterm: ', stdout, stderr)
	except Exception as e:
		print("open_xterm",e)
		time.sleep(10)
		pass

def foo(n,s):
	get_ip_table()
	# for i in range(0,10):
		# print("yolo")

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter, site, delay, loss, bw, terminal_id, cwnd, prot, abc, cork, low_lat, rto, ss):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.site = site
        self.delay = delay
        self.loss = loss
        self.bw = bw
        self.terminal_id = terminal_id
        self.cwnd = cwnd
        self.prot = prot
        self.abc = abc
        self.cork = cork
        self.low_lat = low_lat
        self.rto = rto
        self.ss = ss
    def run(self):
    	if self.threadID == 1:
    		open_xterm(self.name, self.site, self.delay, self.loss, self.bw, self.terminal_id, self.cwnd, self.prot, self.abc, self.cork, self.low_lat, self.rto, self.ss)
    	elif self.threadID == 2:
    		change_cw(self.name, self.cwnd)

if __name__ == "__main__":
	display = Display(visible=0, size=(800, 600))
	display.start()
	
	sys.stdout = open("log2.txt", "a")
	try:
		site = str(sys.argv[1])
		delay = str(sys.argv[2])
		loss = str(sys.argv[3])
		bw = str(sys.argv[4])
		prot = str(sys.argv[5])
		abc = str(sys.argv[6])
		cork = str(sys.argv[7])
		low_lat =  str(sys.argv[8])
		rto = str(sys.argv[9])
		ss = str(sys.argv[10])
		cwnd_arr = [3,6,9,12,15,18]

		for cwnd in cwnd_arr:

			print("testing for cwnd:",cwnd)
			print("para:", site, bw, delay, loss, prot, abc, cork, low_lat, rto, ss)
			# time.sleep(10)
			# get terminal id
			# terminal_id = get_tid()
			terminal_id = 0
			# open xterm
			arr = []
			arr.append(str(1))
			c = csv.writer(open("flag_cwnd_change.csv", "w"))
			c.writerow(arr)

			thread1 = myThread(1, "Thread-1", 1, site, delay, loss, bw, terminal_id, cwnd, prot, abc, cork, low_lat, rto, ss)
			thread2 = myThread(2, "Thread-2", 2, site, delay, loss, bw, terminal_id, cwnd, prot, abc, cork, low_lat, rto, ss)

			# Start new Threads
			thread1.start()
			time.sleep(3)
			thread2.start()
			thread1.join()
			thread2.join()
			print ("Exiting Main Thread")
			# time.sleep(10)

			# _thread.start_new_thread(open_xterm, ('t1',site, delay, loss, bw, terminal_id, cwnd, prot))
			# time.sleep(3)
			# _thread.start_new_thread(change_cw,('t2',cwnd))

			# open_xterm(site, delay, loss, bw, terminal_id, cwnd, prot)
			# flag = 1
			# time.sleep(100)
			# for times in range(0,1000000):
			# 	print("*********")
			# 	time.sleep(1)
			# 	fff = open('flag_2.csv')
			# 	csvfilefff = csv.reader(fff)
			# 	for rowfff in csvfilefff:
			# 		if (int(rowfff[0]) == 1):
			# 			print(int(rowfff[0]))
			# 		else:
			# 			print(int(rowfff[0]))
			# 			flag = 0
			# 	if flag == 0:
			# 		break
			# print('Free to proceed')
									
			# time.sleep(100)
		# arr = []
		# arr.append(str(0))
		# c = csv.writer(open("flag_1.csv", "w"))
		# c.writerow(arr)
									
	except Exception as e:
		print(1,e)
		time.sleep(10)
		pass
	display.stop()
