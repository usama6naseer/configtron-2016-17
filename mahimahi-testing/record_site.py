from subprocess import Popen, PIPE
import csv
import os
import time


if __name__ == "__main__":
	f = open('sites_selected.csv')
	csvfile = csv.reader(f)
	for row in csvfile:
		if (int(row[0]) == 11):
			break
		temp = row[1].split('.')
		site_name = temp[0] + '_' + temp[1]

		process = Popen(["gnome-terminal -e 'python3 record_site_next.py %s %s'"%(row[1],site_name)], stdout=PIPE, stderr=PIPE, shell=True)
		stdout, stderr = process.communicate()
		# print(stderr)
		# print('************')
		# print(stdout)
		# print('*********')
		time.sleep(80)
		print(row[1],' done')
		arr = []
		arr.append(row[1])
		arr.append(stderr)
		arr.append(stdout)
		c = csv.writer(open("log_record_site.csv", "a", newline=''))
		c.writerow(arr)
