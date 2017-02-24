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

# # cn = "mm-webreplay recorded_sites/espn python t2.py"
# process = Popen(["xterm -e 'mm-delay 50 python3 t3.py' &"], stdout=PIPE, stderr=PIPE, shell=True)
# # process = Popen(["ip route show"], stdout=PIPE, stderr=PIPE, shell=True)
# stdout, stderr = process.communicate()
# print(stderr,stdout)
# time.sleep(100)
# # print(stderr,stdout)
site_name = "http://www.amazon.com"
chromium_path = '/usr/bin/chromium-browser'
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chromium_path
st = 'user-data-dir=/tmp/nonexistent$(%s)'%(str(datetime.now()))
chrome_options.add_argument(st)
chrome_options.add_argument('--disable-application-cache')
driver = webdriver.Chrome(executable_path='/home/usama/mahimahi-test/chromedriver', chrome_options = chrome_options)
# end_time = 0
# start_time = time.time()
# driver.get(site_name)
# if(driver.execute_script("return document.readyState") != "complete"):
# 	while(driver.execute_script("return document.readyState") != "complete"):
# 		print("*************** waiting in while ***************")
# 	end_time = time.time()
# else:
# 	end_time = time.time()
# print('%s took %s to load.'%(site_name,end_time-start_time))
# driver.quit()