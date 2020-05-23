import matplotlib.pyplot as plt
import time
import math

total = 1000
num = [s for s in range(1,total,50)]

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

	for i in range(n):
		for j in range(n):
			c[i].append(a[i][j]*b[i][j])
	end = time.time()
	last = end-start
	times.append(last)

print(times)
plt.figure()
plt.plot(num,times)
plt.xlabel('N')
plt.ylabel('Time')
plt.show()