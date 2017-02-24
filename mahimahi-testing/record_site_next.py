import subprocess
import csv
import os
import time
import threading
import sys


if __name__ == "__main__":
	print(sys.argv[1],sys.argv[2])
	# time.sleep(5)
	os_call = 'mm-webrecord recorded_sites/'+sys.argv[2]+' chromium-browser --ignore-certificate-errors --user-data-dir=/tmp/nonexistent$(date +%s%N) '+sys.argv[1]
	print(os_call)
	p = subprocess.Popen(os_call, shell=True)
	time.sleep(10)
	print("doing work")
	time.sleep(55)
		

	# f = open('alexa_top_500.csv')
	# csvfile = csv.reader(f)
	# for row in csvfile:
	# 	if (int(row[0]) == 2):
	# 		break
	# 	temp = row[1].split('.')
	# 	site_name = temp[0] + '_' + temp[1]
	# 	os_call = 'mm-webrecord recorded_sites/' + site_name + ' chromium-browser --ignore-certificate-errors --user-data-dir=/tmp/nonexistent$(date +%s%N) ' + row[1]
	# 	# os_call = 'mm-webrecord recorded_sites/google_com chromium-browser --ignore-certificate-errors --user-data-dir=/tmp/nonexistent$(date +%s%N) google.com'
	# 	print(row[0], site_name, os_call)
	# 	time.sleep(2)

	# 	# t = threading.Thread(target=record_website, args = (os_call,))
	# 	# t.start()
	# 	# # t.join(2)
	# 	# print('********************')
	# 	# print('********************')
	# 	# print('********************')
	# 	# print('********************')
	# 	# print('********************')
	# 	# time.sleep(5)
	# 	# t.exit()

	# 	# subprocess.call(['gnome-terminal', '-x', 'ls'], shell=True)

	# 	p = subprocess.Popen(os_call, shell=True)
	# 	time.sleep(10)
	# 	print("doing work")
	# 	time.sleep(50)
	# 	# time.sleep(5)
	# 	# p.kill()

	# 	# proc = subprocess.call(os_call, shell=True)
	# 	# try:
	# 	#     outs, errs = proc.communicate(timeout=5)
	# 	# except TimeoutExpired:
	# 	# 	print('***********************************')
	# 	# 	print('***********************************')
	# 	# 	print('***********************************')
	# 	# 	proc.kill()
	# 	# 	outs, errs = proc.communicate()
	# 	# proc = 0
	# 	# try:
	# 	# 	proc = subprocess.Popen(os_call, shell=True, timeout=5)
	# 	# except Exception as e:
	# 	# 	print('***********************************')
	# 	# 	print('***********************************')
	# 	# 	print('***********************************')
	# 	# 	proc.kill()
	# 	# 	# os.kill(proc)
	# 	# 	print("timeout exception: ", e)
