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


if __name__ == "__main__":
	try:
		# binary = FirefoxBinary('/usr/bin/firefox')
		# driver = webdriver.Firefox(firefox_binary='/usr/bin/firefox')
		# driver = webdriver.Firefox(firefox_binary='/home/usama/proxitron/geckodriver')
		# fp = webdriver.FirefoxProfile('/home/usama/proxitron/profiles')
		# browser = webdriver.Firefox(firefox_binary=binary)
		# browser.get("http://www.google.com")
		# firefox_profile = webdriver.FirefoxProfile()
		# firefox_capabilities = DesiredCapabilities.FIREFOX
		# firefox_capabilities['binary'] = binary
		# driver = webdriver.Firefox(firefox_profile=fp, capabilities=firefox_capabilities)


		# firefox_path = '/usr/bin/firefox'
		# options = webdriver.FirefoxOptions()
		# options.binary_location = firefox_path
		# options.add_argument('--disable-application-cache')
		# driver = webdriver.Firefox(executable_path='/home/usama/mahimahi-test/chromedriver', chrome_options = options)
					
		# f = webdriver.FirefoxProfile('/home/usama/.mozilla/firefox/lswtme1i.default')
		f = webdriver.FirefoxProfile('/home/usama/.mozilla/firefox/gf55s9ay.t2')
		f.set_preference('devtools.netmonitor.har.defaultLogDir','/home/usama/proxitron/har')
		f.set_preference('devtools.netmonitor.har.enableAutoExportToFile',True)
		f.set_preference('extensions.netmonitor.har.contentAPIToken','test')
		f.set_preference('extensions.netmonitor.har.autoConnect',True)
		ext_path = 'harexporttrigger-0.5.0-beta.10.xpi'
		f.add_extension(extension=ext_path)
		# f.set_preference('extensions.netmonitor.har.enableAutomation',True)
		# f.set_preference('browser.cache.disk.enable',False)
		driver = webdriver.Firefox(firefox_profile=f)


		# driver = webdriver.Firefox(firefox_profile = , executable_path=firefox_path)
		# driver = webdriver.Firefox()
		# body = driver.find_element_by_xpath("//body")
		# print 1
		# action = ActionChains(driver)
		# action.send_keys(Keys.F12)
		# action.perform()
		# # body.send_keys(Keys.CONTROL, Keys.SHIFT, "k")
		# print 2
		time.sleep(1)
		driver.get("http://www.google.com")
		time.sleep(5)
		body = driver.find_element_by_xpath("//body")
		body.send_keys(Keys.F12)
		time.sleep(2)
		# cm = 'var options = {token: "test", getData: true,};	HAR.triggerExport(options).then(result => {console.log(result.data);});'
		cm = 'var options = {token: "test",fileName: "%s"};HAR.triggerExport(options).then(result => {});'%('google')
		driver.execute_script(cm)
		# assert "Python" in driver.title
		# elem = driver.find_element_by_name("q")
		# elem.clear()
		# elem.send_keys("pycon")
		# elem.send_keys(Keys.RETURN)
		# assert "No results found." not in driver.page_source
		time.sleep(200)
		# driver.close()
	except Exception as e:
		# print('************************')
		print(e)
