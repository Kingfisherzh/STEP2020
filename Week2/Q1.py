import matplotlib.pyplot as plt
import time
import math

total = 100
num = [s for s in range(1,total,1)]
value = 0

a = [[] for _ in range(total)]
b = [[] for _ in range(total)]
c = [[] for _ in range(total)]
times = []

for n in num:

	for i in range(n):
		for j in range(n):
			a[i].append(i*j)
	for i in range(n):
		for j in range(n):
			b[i].append(i+j)

	start = time.time()

	# Time complexity is O(n^3)
	
	for row in range(n):
		for col in range(n):
			for k in range(n):
				value = value + a[col][k]*b[k][col]
				c[row].append(value)
	end = time.time()
	last = end-start
	times.append(last)

print(times)
plt.figure()
plt.plot(num,times)
plt.xlabel('N')
plt.ylabel('Time')
plt.show()