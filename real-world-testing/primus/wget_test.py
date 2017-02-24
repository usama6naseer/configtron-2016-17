from datetime import datetime
import math
import time
import wget
import urllib2
import csv

if __name__ == "__main__":
	try:
		bwa = [400]
		delaya = [50, 150, 300]
		lossa = [0, 1, 2.5, 5, 10]
		prota = ['cubic','reno','vegas']
		cwnda = [3,10,18]
		for bw in bwa:
			for delay in delaya:
				for loss in lossa:
					for prot in prota:
						for cwnd in cwnda:

							urllib2.urlopen('http://152.3.144.154/change_para.php?delay='+str(delay)+'&loss='+str(loss)+'&bw='+str(bw)+'&prot='+str(prot)).read()
							time.sleep(1)
							urllib2.urlopen('http://152.3.144.154/change_cwnd.php?cwnd='+str(cwnd)).read()
							time.sleep(1)

							arr1 = []
							arr2 = []
							arr3 = []
							arr4 = []
							arr5 = []
							arr6 = []
							arr7 = []
							arr8 = []
							for i in range(0,3):
								print(i,delay)
								start_time = time.time()
								filename = wget.download('http://152.3.144.154/large_image_10kb.jpg')
								end_time = time.time()
								# print "plt", end_time - start_time
								arr1.append(end_time - start_time)

								# start_time = time.time()
								# filename = wget.download('http://152.3.144.154/large_image_50kb.jpg')
								# end_time = time.time()
								# # print "plt", end_time - start_time
								# arr2.append(end_time - start_time)

								# start_time = time.time()
								# filename = wget.download('http://152.3.144.154/large_image_100kb.jpg')
								# end_time = time.time()
								# # print "plt", end_time - start_time
								# arr3.append(end_time - start_time)

								# start_time = time.time()
								# filename = wget.download('http://152.3.144.154/large_image_200kb.jpg')
								# end_time = time.time()
								# # print "plt", end_time - start_time
								# arr4.append(end_time - start_time)

								# start_time = time.time()
								# filename = wget.download('http://152.3.144.154/large_image_300kb.jpg')
								# end_time = time.time()
								# # print "plt", end_time - start_time
								# arr5.append(end_time - start_time)

								# start_time = time.time()
								# filename = wget.download('http://152.3.144.154/large_image_400kb.jpg')
								# end_time = time.time()
								# # print "plt", end_time - start_time
								# arr6.append(end_time - start_time)

								# start_time = time.time()
								# filename = wget.download('http://152.3.144.154/large_image_500.jpg')
								# end_time = time.time()
								# # print "plt", end_time - start_time
								# arr7.append(end_time - start_time)
								
								# start_time = time.time()
								# filename = wget.download('http://152.3.144.154/large_image_1.JPG')
								# end_time = time.time()
								# # print "plt", end_time - start_time
								# arr8.append(end_time - start_time)

							# print("done")
							# print("plt 1 : ", sum(arr1)/5)
							# print(arr1)
							# print("plt 2 : ", sum(arr2)/5)
							# print(arr2)
							# print("plt 5 : ", sum(arr3)/5)
							# print(arr3)
							# print("plt 0 : ", sum(arr4)/5)
							# print(arr4)
							# print("plt 10 : ", sum(arr5)/5)
							# print(arr5)
							# print("plt 100 : ", sum(arr6)/5)
							# print(arr6)
							# print("plt 200 : ", sum(arr7)/5)
							# print(arr7)
							# print("plt 500 : ", sum(arr8)/5)
							# print(arr8)
							c = csv.writer(open("wget_record_low_lat0.csv", "a"))
							arr = []
							arr.append('10kb')
							arr.append(sum(arr1)/5)
							arr.append(arr1)
							c.writerow(arr)

							# arr = []
							# arr.append('50kb')
							# arr.append(sum(arr2)/5)
							# arr.append(arr2)
							# c.writerow(arr)

							# arr = []
							# arr.append('100kb')
							# arr.append(sum(arr3)/5)
							# arr.append(arr3)
							# c.writerow(arr)

							# arr = []
							# arr.append('200kb')
							# arr.append(sum(arr4)/5)
							# arr.append(arr4)
							# c.writerow(arr)

							# arr = []
							# arr.append('300kb')
							# arr.append(sum(arr5)/5)
							# arr.append(arr5)
							# c.writerow(arr)

							# arr = []
							# arr.append('400kb')
							# arr.append(sum(arr6)/5)
							# arr.append(arr6)
							# c.writerow(arr)

							# arr = []
							# arr.append('500kb')
							# arr.append(sum(arr7)/5)
							# arr.append(arr7)
							# c.writerow(arr)

							# arr = []
							# arr.append('last')
							# arr.append(sum(arr8)/5)
							# arr.append(arr8)
							# c.writerow(arr)



							print "results written to plt_record.csv"
													
	except Exception, e:
		print('1', e)
		pass
						
