import numpy as np
from matplotlib import pyplot as plt
import time
start = time.perf_counter()
# rect
img1 = np.zeros([100, 100])
img2 = np.zeros([100, 100])
m, n = np.size(img2)
img1[50-10:50+10, 50-10:50+10] = 1
plt.imshow(img1)
for i in m:
    for j in n:
        if (i-50)**2+(j-50)**2 <= 5000:
            img2[i, j] = 1
z = 5
wave = 600e-9
u1 = np.zeros([100, 100])

for x in np.arange(0, 100, 1):
    for y in np.arange(0, 100, 1):
        for u in np.arange(0, 100, 1):
            for v in np.arange(0, 100, 1):
                r = np.sqrt(z**2+(x-u)**2+(y-v)**2)
                u1[x, y] += z/(1j*wave)*img1[u, v]*np.exp(2*np.pi*1j*r)/(r)**2


diffracted_field1 = np.abs(u1)
end = time.perf_counter()
print("{:}s".format(end-start))

plt.figure(1)
plt.imshow(diffracted_field1)
