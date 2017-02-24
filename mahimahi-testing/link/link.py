import math
import sys

link1 = float(sys.argv[1])
link = link1*1000000
nump = link/1500
nums = 1000/nump
print(nums)
tries = 100
if link1 > 10:
	tries = 200
if link1 > 40:
	tries = 500
if link1 > 90:
	tries = 800
arr = []
k = 0
count = 0
for i in range(0,5000000):
	count = count + 1
	arr.append(k)
	k = k + nums
	if count == tries:
		# print('k',k)
		break



for i in arr:
	i = math.floor(i)
	print(i)
	f = open(str(link1)+'mb','a')
	f.write(str(i)+'\n') # python will convert \n to os.linesep
	f.close() 






# prev = -1
# cnt = 0
# for i in arr:
# 	i = math.floor(i)
# 	if prev == i:
# 		cnt = cnt + 1
# 	else:
# 		if prev != -1:
# 			for m in range(0,cnt):
# 				print(i)
# 				f = open(str(link1)+'mb','a')
# 				f.write(str(prev)+'\n') # python will convert \n to os.linesep
# 				f.close()

# 		else:
# 			prev = i
# 			cnt = 1
# 	# i = math.floor(i)
# 	# print(i)
# 	# f = open(str(link1)+'mb','a')
# 	# f.write(str(i)+'\n') # python will convert \n to os.linesep
# 	# f.close() 































