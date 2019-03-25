import numpy as np
from matplotlib import pyplot as plt
import time
from numba import jit
start = time.perf_counter()
# rect
img1 = np.zeros([100, 100])
img2 = np.zeros([100, 100])
img1[50-10:50+10, 50-10:50+10] = 1
plt.figure(0)
plt.imshow(img1)
for i in range(100):
    for j in range(100):
        if (i-50)**2+(j-50)**2 <= 100:
            img2[i, j] = 1
plt.figure(1)
plt.imshow(img2)
img = img2
z = 0.5
wave = 600e-9
u1 = np.zeros([100, 100])
m, n = np.shape(img)
@jit(parallel=True)
def jisuan():
    for x in np.arange(0, 100, 1):
        for y in np.arange(0, 100, 1):
            for u in np.arange(0, 100, 1):
                for v in np.arange(0, 100, 1):
                    r = np.sqrt(z**2+(x-u)**2+(y-v)**2)
                    u1[x, y] += z/(1j*wave)*img[u, v] * \
                        np.exp(2*np.pi*1j*r)/(r)**2
    return u1


u1 = jisuan()


diffracted_field1 = np.abs(u1)
end = time.perf_counter()
print("{:}s".format(end-start))

plt.figure(1)
plt.imshow(diffracted_field1)
