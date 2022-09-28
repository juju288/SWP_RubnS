import random
import numpy as np

start = 1
end = 45
ziehung = 6

a = np.arange(start, end+1)
for i in range(0, ziehung):
    r = int(random.random()*end+1)
    a1 = a[r]
    a[r] = a[(end-1)-i]
    a[(end-1) - i] = a1

for i in range(end-6, end):
    print(a[i])
print(a)

dc = {}
for i in range(start, end+1):
    dc[i] = i

for i in range(0, 1000):
    dc[int(random.random()*end+1)] += 1

print(dc)