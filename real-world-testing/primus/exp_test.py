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

def change_delay(new):
	# tc qdisc to check delay
	try:
		cm = "sudo tc qdisc change dev eno1 root netem delay " + str(new) + "ms"
		process = Popen([cm], stdout=PIPE, stderr=PIPE, shell=True)
		stdout, stderr = process.communicate()
		print "add delay",stdout
		print "add delay",stderr
	except Exception,e:
		print "error in change delay",e
		pass
	time.sleep(1)

def change_loss(new):
	try:
		cm = "sudo tc qdisc change dev eno1 root netem loss " + str(new) + "%"
		process = Popen([cm], stdout=PIPE, stderr=PIPE, shell=True)
		stdout, stderr = process.communicate()
		print "add loss",stdout
		print "add loss",stderr
	except Exception,e:
		print "error in change loss",e
		pass
	time.sleep(1)

def change_delay_loss(newd, newl):
	# tc -s qdisc ls dev eno1
	try:
		cm = "sudo tc qdisc change dev eno1 root netem delay " + str(newd) + "ms loss " + str(newl) + "%"
		process = Popen([cm], stdout=PIPE, stderr=PIPE, shell=True)
		stdout, stderr = process.communicate()
		print "add loss",stdout
		print "add loss",stderr
	except Exception,e:
		print "error in change delay loss",e
		pass
	time.sleep(1)

def change_bw(bw):
	try:
		cm = "./change_bw.sh " + str(bw)
		process = Popen([cm], stdout=PIPE, stderr=PIPE, shell=True)
		stdout, stderr = process.communicate()
		print "change bw",stdout
		print "change bw",stderr
	except Exception,e:
		print "error in change bw",e
		pass
	time.sleep(2)

def del_tc_para():
	try:
		cm = "./del_para.sh"
		process = Popen([cm], stdout=PIPE, stderr=PIPE, shell=True)
		stdout, stderr = process.communicate()
		print "dele para",stdout
		print "del para",stderr
	except Exception,e:
		print "error in del para",e
		pass
	time.sleep(1)

if __name__ == "__main__":
	try:
		display = Display(visible=0, size=(800, 600))
		display.start()

		site_arr = ["bbc.com"]
		delay_arr = [50,150,250,500]
		loss_arr = [0,0.01,0.025,0.05]

		# change
		bw_arr = [384, 120, 5000, 1000]
		# bw_arr = ['0.3mb', '1mb', '5mb']
		cwnd_arr = [3,6,9,12,15,18]
		prot_arr = ['cubic','reno','vegas']
		low_lat_arr = [0,1]
		cork_arr = [0,1]
		slow_start_arr = [1,0]
		
		for bw in bw_arr:
			change_bw(bw)
			time.sleep(1)

			for ss in slow_start_arr:
				change_slow_start(ss)		
				for cork in cork_arr:
					change_cork(cork)
					for low_lat in low_lat_arr:
						change_low_lat(low_lat)
						for loss in loss_arr:
							for delay in delay_arr:
								for prot in prot_arr:
									for site in site_arr:

										try:
											print "changing parameters to:", prot, bw, delay, loss
											try:
												chromium_path = '/usr/bin/chromium-browser'
												chrome_options = webdriver.ChromeOptions()
												chrome_options.binary_location = chromium_path
												chrome_options.add_argument('--disable-application-cache')
												driver = webdriver.Chrome(executable_path='/home/usama/mm/chromedriver', chrome_options = chrome_options)
												time.sleep(1)

												#change
												para_url = 'http://xeno-100/magnus/change_para.php?delay='+str(delay)+'&loss='+str(loss)+'&bw='+str(bw)+'&prot='+str(prot)+'&ss='+str(ss)+'&cork='+str(cork)+'&low_lat='+str(low_lat)
												print(para_url)
												driver.get(para_url)
												driver.quit()

											except Exception,e:
												driver.quit()
												print "error in changing in para",e
												pass
												# del_tc_para()

											print "changing cwnd to:", cwnd
											try:
												chromium_path = '/usr/bin/chromium-browser'
												chrome_options = webdriver.ChromeOptions()
												chrome_options.binary_location = chromium_path
												chrome_options.add_argument('--disable-application-cache')
												driver = webdriver.Chrome(executable_path='/home/usama/mm/chromedriver', chrome_options = chrome_options)
												time.sleep(1)

												# change
												para_url = 'http://xeno-100/magnus/change_cwnd.php?cwnd='+str(cwnd)
												print(para_url)
												driver.get(para_url)
												driver.quit()

											except Exception,e:
												driver.quit()
												print "error in changing in cwnd",e
												pass
												# del_tc_para()		

											for load_time in range(0,5):
												try:
													continue_flag = 1
													site = "http://xeno-100/magnus/bbc/www.bbc.com"
													print "loaded for:", load_time, site
													end_time = 0
													start_time = 0
													# socket.setdefaulttimeout(120000)
													try:
														chromium_path = '/usr/bin/chromium-browser'
														chrome_options = webdriver.ChromeOptions()
														chrome_options.binary_location = chromium_path
														chrome_options.add_argument('--disable-application-cache')
														driver = webdriver.Chrome(executable_path='/home/usama/mm/chromedriver', chrome_options = chrome_options)
														time.sleep(1)

														start_time = time.time()
														driver.get(site)
														end_time = time.time()

														driver.quit()
													except socket.timeout:
														driver.quit()
														print "timedout"
														continue_flag = 0
														pass
													if continue_flag == 1:
														try:
															plt = end_time - start_time
															print(site, "plt:", plt)

															arr = []
															arr.append(load_time)
															arr.append(site)
															arr.append(plt)
															arr.append(cwnd)
															arr.append(prot)
															arr.append(loss)
															arr.append(delay)
															arr.append(bw)
															arr.append(ss)
															arr.append(cork)
															arr.append(low_lat)
															arr.append(str(datetime.now()))
															filename = "bbc_plt_record.csv"
															c = csv.writer(open(filename, "a"))
															c.writerow(arr)
															print "results written to %s.csv"%(filename)
															time.sleep(1)

														except Exception,e:
															print("timed out after loading:",e)
															# driver.quit()
															pass
												except Exception,e:
													print("exception here:",e)
													pass		
										

										except Exception as e:
											print(2,e)
											pass



	except Exception as e:
		print(1,e)
		pass

		