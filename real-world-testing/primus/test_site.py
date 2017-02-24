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


display = Display(visible=0, size=(800, 600))
display.start()

try:
	cm = 'firefox -CreateProfile "multi_test /home/usama/proxitron/primus_server/profile"'
	process = Popen([cm], stdout=PIPE, stderr=PIPE, shell=True)
	stdout, stderr = process.communicate()
	print "add loss",stdout
	print "add loss",stderr
except Exception,e:
	print "error in change delay loss",e
time.sleep(5)
display.stop()

# driver = webdriver.Firefox()
# driver.get("http://www.google.com")
# print("loaded")
# time.sleep(100)											