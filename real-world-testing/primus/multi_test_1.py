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

def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0

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
		resume_flag = 0
		one_time_flag = 0
		for jkj in (0,1):

			# change bandwidth
			bw_array = [5000, 1000, 384, 120]
			for bw in bw_array:
				if resume_flag == 1:
					change_bw(bw)
					time.sleep(1)
				# break
				# change delay
				delay_array = [25, 50, 100, 150, 250, 400]
				for delay in delay_array:	
					# change loss
					loss_array = [0, 1, 2.5, 5]

					for loss in loss_array:
						# change_delay_loss(delay, loss)
						# print "delay changed tp:",delay,"loss changed to:", loss
						# prot_array = ['cubic','reno','bic','highspeed','htcp','hybla','illinois','lp','scalable','vegas','veno','westwood','yeah']
						prot_array = ['cubic','reno','vegas']
						for prot in prot_array:
							if resume_flag == 1:
								print "changing parameters to:", prot, bw, delay, loss
								try:
									# display = Display(visible=0, size=(800, 600))
									# display.start()
									driver = webdriver.Firefox()
									para_url = 'http://152.3.144.154/change_para.php?delay='+str(delay)+'&loss='+str(loss)+'&bw='+str(bw)+'&prot='+str(prot)
									print(para_url)
									driver.get(para_url)
									time.sleep(1)
									driver.quit()
									# display.stop()
									print "para changed to:", prot, bw, delay, loss
								except Exception,e:
									driver.quit()
									print "error in changing in para",e
									pass
									# del_tc_para()

							# change cwnd
							# cwnd_array = [2,4,6,8,10,12,14,16,18,20]
							cwnd_array = [3,6,9,12,15,18]
							for cwnd in cwnd_array:
								avg_plt_arr = []
								avg_obj_arr = []

								check_flag = 0
								if resume_flag == 0:
									try:
										fo = open('object_load_record.csv')
										csvfileo = csv.reader(fo)
										for rowo in csvfileo:
											# print rowo
											if (str(rowo[1]) == str('5mb image')):
												# print(1)
												if (str(rowo[3]) == str(cwnd)):
													# print(2)
													if (str(rowo[4]) == str(prot)):
														# print(3)
														if (str(rowo[5]) == str(loss)):
															# print(4)
															if (str(rowo[6]) == str(delay)):
																# print(5)
																if (str(rowo[7]) == str(bw)):
																	# print(6)
																	resume_flag = 0
																	check_flag = 1
																	print "found",rowo
																	break
										if (check_flag == 0):
											resume_flag = 1
											one_time_flag = 1
											print "continue",cwnd,prot,loss,delay,bw
									except Exception, e:
										print "resume error",e
										resume_flag = 1
										one_time_flag = 1
										pass


								resume_flag = 1
								if resume_flag == 1:
									if one_time_flag == 1:
										one_time_flag = 0
										
										change_bw(bw)
										time.sleep(1)
										
										print "changing parameters to:", prot, bw, delay, loss
										try:
											driver = webdriver.Firefox('/home/usama/proxitron/primus_server/profile')
											para_url = 'http://152.3.144.154/change_para.php?delay='+str(delay)+'&loss='+str(loss)+'&bw='+str(bw)+'&prot='+str(prot)
											print(para_url)
											driver.get(para_url)
											time.sleep(2)
											driver.quit()
											print "para changed to:", prot, bw, delay, loss
										except Exception,e:
											driver.quit()
											print "error in changing in para",e
											pass
											# del_tc_para()

									print "changing cwnd to:", cwnd
									try:
										# display = Display(visible=0, size=(800, 600))
										# display.start()							
										driver = webdriver.Firefox()
										cwnd_url = 'http://152.3.144.154/change_cwnd.php?cwnd='+str(cwnd)
										driver.get(cwnd_url)
										time.sleep(1)
										driver.quit()
										# display.stop()
										print "cwnd changed to:",cwnd
									except Exception,e:
										driver.quit()
										print "error in changing in cwnd",e
										pass
										# del_tc_para()				
							
									for load_time in range(0,5):
										try:
											continue_flag = 1
											site = "http://152.3.144.154/replay/www.yahoo.com"
											print "loaded for:", load_time, site
											end_time = 0
											start_time = 0
											# socket.setdefaulttimeout(120000)
											try:
												f = webdriver.FirefoxProfile('/home/usama/proxitron/primus_server/profile')
												# f.set_preference('devtools.netmonitor.har.defaultLogDir','/home/usama/proxitron/primus_server/har')
												# f.set_preference('devtools.netmonitor.har.enableAutoExportToFile',True)
												# f.set_preference('extensions.netmonitor.har.contentAPIToken','test')
												# f.set_preference('extensions.netmonitor.har.autoConnect',True)
												# ext_path = 'harexporttrigger-0.5.0-beta.10.xpi'
												# f.add_extension(extension=ext_path)
												f.set_preference('browser.cache.disk.enable',False)
												# f.set_preference('extensions.netmonitor.har.enableAutomation',True)
												driver = webdriver.Firefox(firefox_profile=f)

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
													arr.append(str(datetime.now()))
													filename = "yahoo_plt_record.csv"
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

		display.stop()
	except Exception, e:
		print('1', e)
		pass
