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

# f = webdriver.FirefoxProfile('/home/usama/.mozilla/firefox/gf55s9ay.t2')
# f.set_preference('devtools.netmonitor.har.defaultLogDir','/home/usama/proxitron/har')
# f.set_preference('devtools.netmonitor.har.enableAutoExportToFile',True)
# f.set_preference('extensions.netmonitor.har.contentAPIToken','test')
# f.set_preference('extensions.netmonitor.har.autoConnect',True)
# ext_path = 'harexporttrigger-0.5.0-beta.10.xpi'
# f.add_extension(extension=ext_path)
# f.set_preference('browser.cache.disk.enable',False)
# f.set_preference('extensions.netmonitor.har.enableAutomation',True)
# driver = webdriver.Firefox(firefox_profile=f)
driver = webdriver.Firefox()

time.sleep(1)
print "loading"
end_time = 0
start_time = 0
socket.setdefaulttimeout(120)
try:
	start_time = time.time()
	driver.get("http://www.youtube.com")
	end_time = time.time()
	# time.sleep(100)
	driver.quit()
except socket.timeout:
	driver.quit()
	print "timedout", site
	pass
plt = end_time - start_time
print(plt)