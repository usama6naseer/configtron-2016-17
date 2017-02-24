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

def change_rto(val):
	process = Popen(["ip route show"], stdout=PIPE, stderr=PIPE, shell=True)
	stdout, stderr = process.communicate()
	output = stdout.decode("utf-8").strip()
	output = output.split('\n')
	for i in output:
		if "nameserver" not in i:
			if "rto_min" in i:
				vcv = i.split("rto_min")
				print(vcv)
				i = vcv[0]
			try:
				command = "sudo ip route change %s rto_min %s"%(i,val)
				print(command)
				process = Popen([command], stdout=PIPE, stderr=PIPE, shell=True)
				stdout, stderr = process.communicate()
				print("change_rto",stderr,stdout)
				time.sleep(0.3)
			except Exception as e:
				print("2:",e)


if __name__ == "__main__":
	try:
		change_rto(int(sys.argv[1]))

	except Exception as e:
		print('3:',e)
		pass

