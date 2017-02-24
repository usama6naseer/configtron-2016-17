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
from pyvirtualdisplay import Display

def change_prot(prot):
	try:
		cn = "sudo sh -c 'echo %s > /proc/sys/net/ipv4/tcp_congestion_control'"%('"'+prot+'"')
		# cn = "ls /proc/sys/net/ipv4"
		# cn = "sudo sysctl net.ipv4.tcp_congestion_control=%s"%(prot)
		# print(cn)
		process = Popen([cn], stdout=PIPE, stderr=PIPE, shell=True)
		stdout, stderr = process.communicate()
		# output = stdout.decode("utf-8").strip()
		# output = output.split('\n')
		# print(output)
		print('prot: ', stdout, stderr)
		time.sleep(1)
		# # check if protocol changed
		process = Popen(['sudo cat /proc/sys/net/ipv4/tcp_congestion_control'], stdout=PIPE, stderr=PIPE, shell=True)
		stdout, stderr = process.communicate()
		print('prot changed to:', str(stdout.decode("utf-8")).strip())
		if(str(stdout.decode("utf-8")).strip() == prot):
			print('change successful')
			return True
		else:
			print('**** change not successful')
			return False					

	except Exception as e:
		print('change_prot',e)
		time.sleep(10)
		pass

def change_abc(prot):
	try:
		cn = "sudo sh -c 'echo %s > /proc/sys/net/ipv4/tcp_congestion_control'"%('"'+prot+'"')
		# cn = "ls /proc/sys/net/ipv4"
		# cn = "sudo sysctl net.ipv4.tcp_congestion_control=%s"%(prot)
		# print(cn)
		process = Popen([cn], stdout=PIPE, stderr=PIPE, shell=True)
		stdout, stderr = process.communicate()
		# output = stdout.decode("utf-8").strip()
		# output = output.split('\n')
		# print(output)
		print('prot: ', stdout, stderr)
		time.sleep(1)
		# # check if protocol changed
		process = Popen(['sudo cat /proc/sys/net/ipv4/tcp_congestion_control'], stdout=PIPE, stderr=PIPE, shell=True)
		stdout, stderr = process.communicate()
		print('prot changed to:', str(stdout.decode("utf-8")).strip())
		if(str(stdout.decode("utf-8")).strip() == prot):
			print('change successful')
			return True
		else:
			print('**** change not successful')
			return False					

	except Exception as e:
		print('change_prot',e)
		time.sleep(10)
		pass

def change_cork(cork):
	try:
		cn = "sudo sh -c 'echo %s > /proc/sys/net/ipv4/tcp_autocorking'"%(cork)
		# print(cn)
		process = Popen([cn], stdout=PIPE, stderr=PIPE, shell=True)
		stdout, stderr = process.communicate()
		print('cork: ', stdout, stderr)
		time.sleep(1)
		# # check if cork changed
		process = Popen(['sudo cat /proc/sys/net/ipv4/tcp_autocorking'], stdout=PIPE, stderr=PIPE, shell=True)
		stdout, stderr = process.communicate()
		print('cork changed to:', str(stdout.decode("utf-8")).strip())
		if(str(stdout.decode("utf-8")).strip() == str(cork)):
			print('change successful')
			return True
		else:
			print('**** change not successful')
			return False					

	except Exception as e:
		print('change_cork',e)
		time.sleep(10)
		pass

def change_low_lat(low_lat):
	try:
		cn = "sudo sh -c 'echo %s > /proc/sys/net/ipv4/tcp_low_latency'"%(low_lat)
		process = Popen([cn], stdout=PIPE, stderr=PIPE, shell=True)
		stdout, stderr = process.communicate()
		print('low_lat: ', stdout, stderr)
		time.sleep(1)
		# # check if cork changed
		process = Popen(['sudo cat /proc/sys/net/ipv4/tcp_low_latency'], stdout=PIPE, stderr=PIPE, shell=True)
		stdout, stderr = process.communicate()
		print('low_lat changed to:', str(stdout.decode("utf-8")).strip())
		if(str(stdout.decode("utf-8")).strip() == str(low_lat)):
			print('change successful')
			return True
		else:
			print('**** change not successful')
			return False					

	except Exception as e:
		print('change_low_lat',e)
		time.sleep(10)
		pass

def change_slow_start(ss):
	try:
		cn = "sudo sh -c 'echo %s > /proc/sys/net/ipv4/tcp_slow_start_after_idle'"%(ss)
		# print(cn)
		process = Popen([cn], stdout=PIPE, stderr=PIPE, shell=True)
		stdout, stderr = process.communicate()
		print('slow start: ', stdout, stderr)
		time.sleep(1)
		# # check if ss changed
		process = Popen(['sudo cat /proc/sys/net/ipv4/tcp_slow_start_after_idle'], stdout=PIPE, stderr=PIPE, shell=True)
		stdout, stderr = process.communicate()
		print('ss changed to:', str(stdout.decode("utf-8")).strip())
		if(str(stdout.decode("utf-8")).strip() == str(ss)):
			print('change successful')
			return True
		else:
			print('**** change not successful')
			return False					

	except Exception as e:
		print('change_slow_start',e)
		time.sleep(10)
		pass

def web_replay(site_dir, site, delay, loss, bw, prot, abc, cork, low_lat, rto, ss):
	try:
		cm = 'xterm -e "mm-webreplay recorded_sites/%s python3 client_server_test.py %s %s %s %s %s %s %s %s %s %s"'%(site_dir, site, delay, loss, bw, prot, abc, cork, low_lat, rto, ss)
		print(cm)
		process = Popen([cm], stdout=PIPE, stderr=PIPE, shell=True)
		stdout, stderr = process.communicate()
		print('replayed: ', site_dir, stdout, stderr)		
	except Exception as e:
		print("web_replay",e)
		pass

if __name__ == "__main__":
	display = Display(visible=0, size=(800, 600))
	display.start()
	# sys.stdout = open("log1.txt", "a")
	try:
		fn1 = open('plt_results.csv')
	except Exception as e:
		print("adding headers",e)
		arr = []
		arr.append("load_time")
		arr.append("site")
		arr.append("PLT")
		arr.append("bw")
		arr.append("loss")
		arr.append("delay")
		arr.append("cwnd")
		arr.append("cong control")
		arr.append("abc")
		arr.append("corking")
		arr.append("low_lat")
		arr.append("rto")
		arr.append("slow_start")
		arr.append("time")
		c = csv.writer(open("plt_results.csv", "a", newline=''))
		c.writerow(arr)
		pass
	try:
		fn1 = open('plt_results_avg.csv')
	except Exception as e:
		print("adding headers",e)
		arr = []
		arr.append("site")
		arr.append("Avg PLT")
		arr.append("bw")
		arr.append("loss")
		arr.append("delay")
		arr.append("cwnd")
		arr.append("cong control")
		arr.append("abc")
		arr.append("corking")
		arr.append("low_lat")
		arr.append("rto")
		arr.append("slow_start")
		arr.append("record")
		c = csv.writer(open("plt_results_avg.csv", "a", newline=''))
		c.writerow(arr)
		pass

	try:
		never_check = 0
		site_arr = ["youtube.com"]
		delay_arr = [50,150,250,500]
		loss_arr = [0,0.01,0.025,0.05]
		bw_arr = ['0.3mb', '1mb', '5mb']
		cwnd_arr = [3,6,9,12,15,18]
		prot_arr = ['cubic','reno','vegas']
		abc_arr = [0]
		low_lat_arr = [0,1]
		cork_arr = [0,1]
		slow_start_arr = [1,0]
		rto_arr = [0]

		for bw in bw_arr:
			for rto in rto_arr:
				for ss in slow_start_arr:
					if never_check == 1:
						change_slow_start(ss)		
					for abc in abc_arr:
						for cork in cork_arr:
							if never_check == 1:
								change_cork(cork)
							for low_lat in low_lat_arr:
								if never_check == 1:
									change_low_lat(low_lat)
								for loss in loss_arr:
									for delay in delay_arr:
										for prot in prot_arr:
											for site in site_arr:
												try:
													# check recovery
													if never_check == 0:
														try:
															flag = 0
															fr = open('recovery.csv')
															cr = csv.reader(fr)
															for rowr in cr:
																if(rowr[0] == str(bw)):
																	if(rowr[1] == str(rto)):
																		if(rowr[2] == str(ss)):
																			if(rowr[3] == str(abc)):
																				if(rowr[4] == str(cork)):
																					if(rowr[5] == str(low_lat)):
																						if(rowr[6] == str(loss)):
																							if(rowr[7] == str(delay)):
																								if(rowr[8] == str(prot)):
																									if(rowr[9] == str(site)):
																										flag = 1
																										print('continue')
																										print(rowr)
														except Exception as e:
															print("check recovery exception:",e)
															flag = 1 
															pass


													if flag == 1:
														if never_check == 0:
															never_check = 1
															change_slow_start(ss)
															change_cork(cork)
															change_low_lat(low_lat)

														# change prot
														if change_prot(prot):
															# time.sleep(100)
															# write to recovery
															arr = []
															arr.append(bw)
															arr.append(rto)
															arr.append(ss)
															arr.append(abc)
															arr.append(cork)
															arr.append(low_lat)
															arr.append(loss)
															arr.append(delay)
															arr.append(prot)
															arr.append(site)
															c = csv.writer(open("recovery.csv", "w"))
															c.writerow(arr)

															# load web-replay
															site_dir = site.split('.')[0]
															web_replay(site_dir, site, delay, loss, bw, prot, abc, cork, low_lat, rto, ss)
															print("*********")
														else:
															print("prot change was not successful: %s",prot)
															time.sleep(2)

												except Exception as e:
													print(2,e)
													time.sleep(10)
													pass



	except Exception as e:
		print(1,e)
		pass
