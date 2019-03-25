# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
import time
import numpy.matlib
start = time.perf_counter()
# rect
img1 = np.zeros((1000, 1000))
img2 = np.zeros((1000, 1000))
img1[500-100:500+100, 500-100:500+100] = 1
plt.figure(0)
plt.imshow(img1)
for i in range(1000):
    for j in range(1000):
        if (i-500)**2+(j-500)**2 <= 10000:
            img2[i, j] = 1
plt.figure(1)
plt.imshow(img2)
z = 5
wave = 600e-6
u1 = np.zeros((1000, 1000))
x=0
y=0
for u in np.arange(0, 1000, 1):
    for v in np.arange(0, 1000, 1):
        r = np.sqrt(z**2+(x-u)**2+(y-v)**2)
        u1[x, y] += z/(1j*wave)*img1[u, v] * \
             np.exp(2*np.pi*1j*r)/(r)**2
        y+=1
    x+=1
diffracted_field1=np.abs(u1)
end=time.perf_counter()
print("{:}s".format(end-start))

plt.figure(3)
plt.imshow(diffracted_field1)
plt.show()
