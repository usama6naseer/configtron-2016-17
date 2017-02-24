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


if __name__ == "__main__":
	display = Display(visible=0, size=(800, 600))
	display.start()
	try:
		site = 'http://www.youtube.com'
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
		driver.quit()
		print('%s took %s to load.'%(site,end_time-start_time))
	except Exception as e:
		print(1,e)
	display.stop()
