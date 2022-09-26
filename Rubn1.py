import random
import numpy as np

a = np.arange(1, 46)
for i in range(0, 6):
    r = int(random.random()*45+1)
    a1 = a[r]
    a[r] = a[44-i]
    a[44 - i] = a1

for i in range(40, 45):
    print(a[i])


dc = {}
for i in range(1, 46):
    dc[i] = i;

for i in range(0, 1000):
    dc[int(random.random()*45+1)] += 1

print(dc)