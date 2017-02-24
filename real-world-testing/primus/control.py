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
from pyvirtualdisplay import Display
import wget

if __name__=="__main__":
	try:
		for i in range(0,100):
			print(i)
			cm = "python multi_test.py"
			process = Popen([cm], stdout=PIPE, stderr=PIPE, shell=True)
			stdout, stderr = process.communicate()
			print "control",stdout
			print "control",stderr
			output = stdout.decode("utf-8").strip()
			output = output.split('\n')
			pid = output[1]
			print("pid:",pid)
			
			time.sleep(10)
			cm = "kill %s"%(pid)
			process = Popen([cm], stdout=PIPE, stderr=PIPE, shell=True)
			stdout, stderr = process.communicate()
			print "kill",stdout
			print "kill",stderr
		
		
	except Exception,e:
		print "error in change delay",e
		pass
	time.sleep(1)
