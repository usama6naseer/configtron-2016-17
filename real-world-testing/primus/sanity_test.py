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
		# f = open('alexa_top_500.csv')
		f = open('test_set.csv')
		csvfile = csv.reader(f)
		for row in csvfile:
			if (int(row[0]) == 12):
				break
			# row[1] = 'qq.com'	
			site = "http://www." + str(row[1])
								
			# change bandwidth
			bw_array = [5000, 1000, 500, 40]
			for bw in bw_array:
				if resume_flag == 1:
					change_bw(bw)
					time.sleep(1)
				# break
				# change delay
				delay_array = [25, 50, 100, 150, 200, 250]
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
									time.sleep(2)
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
								# time.sleep(30)
								# break
					
								# print "changing cwnd to:", cwnd
								# try:
								# 	driver = webdriver.Firefox()
								# 	cwnd_url = 'http://152.3.144.154/change_cwnd.php?cwnd='+str(cwnd)
								# 	driver.get(cwnd_url)
								# 	time.sleep(2)
								# 	driver.quit()
								# 	print "cwnd changed to:",cwnd
								# except Exception,e:
								# 	driver.quit()
								# 	print "error in changing in cwnd",e
								# 	pass
								# 	# del_tc_para()

								avg_plt_arr = []
								avg_obj_arr = []

								check_flag = 0
								if resume_flag == 0:
									try:
										fo = open('plt_avg_record.csv')
										csvfileo = csv.reader(fo)
										for rowo in csvfileo:
											# print rowo
											if (str(rowo[0]) == str('http://www.'+row[1])):
												print(1)
												if (str(rowo[3]) == str(cwnd)):
													print(2)
													if (str(rowo[4]) == str(prot)):
														print(3)
														if (str(rowo[5]) == str(loss)):
															print(4)
															if (str(rowo[6]) == str(delay)):
																print(5)
																if (str(rowo[7]) == str(bw)):
																	print(6)
																	resume_flag = 0
																	check_flag = 1
																	print "found",rowo
																	break
										if (check_flag == 0):
											resume_flag = 1
											one_time_flag = 1
											print "continue",site,cwnd,prot,loss,delay,bw
									except Exception, e:
										print "resume error",e
										resume_flag = 1
										one_time_flag = 1
										pass

								if (resume_flag == 1):
									if one_time_flag == 1:
										one_time_flag = 0
										
										change_bw(bw)
										time.sleep(1)
										
										print "changing parameters to:", prot, bw, delay, loss
										try:
											# display = Display(visible=0, size=(800, 600))
											# display.start()
									
											driver = webdriver.Firefox()
											para_url = 'http://152.3.144.154/change_para.php?delay='+str(delay)+'&loss='+str(loss)+'&bw='+str(bw)+'&prot='+str(prot)
											print(para_url)
											driver.get(para_url)
											time.sleep(2)
											driver.quit()
											# display.stop()
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
										time.sleep(2)
										driver.quit()
										# display.stop()
										print "cwnd changed to:",cwnd
									except Exception,e:
										driver.quit()
										print "error in changing in cwnd",e
										pass
										# del_tc_para()

									
									for load_time in range(0,3):
										try:
											continue_flag = 1
											print "loaded for:", load_time

											# display = Display(visible=0, size=(800, 600))
											# display.start()
											# f = webdriver.FirefoxProfile()
											# f.set_preference('devtools.netmonitor.har.defaultLogDir','/home/usama/proxitron/primus_server/har')
											# f.set_preference('devtools.netmonitor.har.enableAutoExportToFile',True)
											# f.set_preference('extensions.netmonitor.har.contentAPIToken','test')
											# f.set_preference('extensions.netmonitor.har.autoConnect',True)
											# ext_path = 'harexporttrigger-0.5.0-beta.10.xpi'
											# f.add_extension(extension=ext_path)
											# f.set_preference('browser.cache.disk.enable',False)
											# f.set_preference('extensions.netmonitor.har.enableAutomation',True)
											# driver = webdriver.Firefox(firefox_profile=f)

											time.sleep(1)
											print "loading:",site
											end_time = 0
											start_time = 0
											socket.setdefaulttimeout(120000)
											try:
												start_time = time.time()
												filename = wget.download('http://152.3.144.154/large_image_5.jpg')
												# driver.get('http://152.3.144.154/large_image_1.JPG')
												end_time = time.time()
												# socket.settimeout(None)
												# socket.close()
											except socket.timeout:
												# socket.close()
												# driver.quit()
												# display.stop()
												# socket.settimeout(None)
												print "timedout", site
												continue_flag = 0
												pass
											if continue_flag == 1:
												try:
													# socket.setdefaulttimeout(200)
													# driver.get('http://152.3.144.154/replay/' + 'www.' + str(row[1]))
													# end_time = time.time()
													plt = end_time - start_time
													print(site, plt)
													time.sleep(1)

													# print "opening web console"
													# body = driver.find_element_by_xpath("//body")
													# body.send_keys(Keys.F12)
													# time.sleep(4)
													# har_name = str(row[1])+'-'+str(cwnd) + '-' + str(prot) + '-' + str(delay) + str(loss)
													# cm = 'var options = {token: "test",fileName: "%s"};HAR.triggerExport(options).then(result => {});'%(har_name)
													# driver.execute_script(cm)
													# print "HAR generated"
													# time.sleep(4)

													# # read har
													# total_time = 0
													# obj_num = 0
															
													# try:
													# 	with open('har/'+ har_name +'.har') as data_file:    
													# 		print "reading generated HAR"
													# 		data = json.load(data_file)
													# 		# print(data)
													# 		log = data['log']
													# 		creator = log['creator']
													# 		entries = log['entries']
													# 		pages = log['pages']
													# 		browser = log['browser']
													# 		total_time = 0
													# 		obj_num = 0
													# 		for i in entries:
													# 			try:
													# 				total_time = total_time + i['time']
													# 				obj_num = obj_num + 1 
													# 			except:
													# 				pass
													# except Exception, e:
													# 	print "error in reading HAR", e	
													# 	pass		

													# print "HAR obj load time:",float(total_time)/1000.0,obj_num
													arr = []
													arr.append(load_time)
													arr.append(site)
													arr.append(plt)
													avg_plt_arr.append(plt)
													# arr.append(float(total_time)/1000.0)
													# avg_obj_arr.append(float(total_time)/1000.0)
													# arr.append(obj_num)
													arr.append(cwnd)
													arr.append(prot)
													arr.append(loss)
													arr.append(delay)
													arr.append(bw)
													arr.append(str(datetime.now()))
													c = csv.writer(open("plt_record.csv", "a"))
													c.writerow(arr)
													print "results written to plt_record,csv"
													time.sleep(3)
													# driver.quit()
													command = "rm -r large_imag*"
													process = Popen([command], stdout=PIPE, stderr=PIPE, shell=True)
													stdout, stderr = process.communicate()
													print "stdout",stdout
													print "stderr",stderr
													# print "HAR deleted"
													# command = "rm -r har/Archive*"
													# process = Popen([command], stdout=PIPE, stderr=PIPE, shell=True)
													# stdout, stderr = process.communicate()
													# print "stdout",stdout
													# print "stderr",stderr

												except Exception,e:
													print("timed out after loading:",e)
													# driver.quit()
													pass
										except:
											print("exception here:")
											# driver.quit()
											pass
									try:
										arr = []
										# arr.append(site)
										# if len(avg_plt_arr) > 0:
										# 	arr.append(sum(avg_plt_arr)/len(avg_plt_arr))
										# 	arr.append(median(avg_plt_arr))
										# else:
										# 	arr.append(0)
										# 	arr.append(0)
										# # if len(avg_obj_arr) > 0:
										# # 	arr.append(sum(avg_obj_arr)/len(avg_obj_arr))
										# # 	arr.append(median(avg_obj_arr))
										# # else:
										# # 	arr.append(0)
										# # 	arr.append(0)
										# arr.append(cwnd)
										# arr.append(prot)
										# arr.append(loss)
										# arr.append(delay)
										# arr.append(bw)
										# c = csv.writer(open("plt_avg_record.csv", "a"))
										# c.writerow(arr)
										# print "avg results written to plt_avg_record,csv"
										# time.sleep(2)
									except Exception,e:
										print("exception here 2:")
										# arr = []
										# arr.append(site)
										# if len(avg_plt_arr) > 0:
										# 	arr.append(sum(avg_plt_arr)/len(avg_plt_arr))
										# 	arr.append(median(avg_plt_arr))
										# else:
										# 	arr.append(0)
										# 	arr.append(0)
										# # if len(avg_obj_arr) > 0:
										# # 	arr.append(sum(avg_obj_arr)/len(avg_obj_arr))
										# # 	arr.append(median(avg_obj_arr))
										# # else:
										# # 	arr.append(0)
										# # 	arr.append(0)
										# arr.append(cwnd)
										# arr.append(prot)
										# arr.append(loss)
										# arr.append(delay)
										# arr.append(bw)
										# c = csv.writer(open("plt_avg_record.csv", "a"))
										# c.writerow(arr)
										# print "avg results written to plt_avg_record,csv"
										# time.sleep(2)

										# print("timed out after loading 2:",e)
										pass

		display.stop()
	except Exception, e:
		print('1', e)
		# driver.quit()
		pass
		# del_tc_para()
