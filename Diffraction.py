"""
all of the unit should be mm


D1: the size of object  
D2: the size of screen
object and the screen have the same coordination 
"""

import numpy as np
import matplotlib.pyplot as plt
import time

pi = np.pi
exp = np.exp
'''
dx,dy: the steps in x and y direction for object
w_len:wavelength 
z:distance from object to screen
'''


def diffraction(in_im, w_len, z, dx, dy, D, x0, y0):
    k = 2*pi/w_len
    # m,n=in_im.shape
    x = np.arange(-D/2, D/2, dx)
    y = np.arange(-D/2, D/2, dy)
    xm, ym = np.meshgrid(x, y)
    r = np.sqrt((xm-x0)**2+(ym-y0)**2+z**2)
    temp_r = z*exp(1j*k*r)/(r**2)
    temp_2 = temp_r*in_im*dx*dy
    intensity = (np.abs(temp_2.sum()))**2
    return intensity


w_len = 500e-6  # mm
z = 35  # mm
dx, dy = 0.01, 0.01  # mm
D1 = 0.5
D10 = D1/2
x_center = np.arange(-D10/2, D10/2, dx)
y_c = x_center.shape[0]
x = np.arange(-D1/2, D1/2, dx)
sy = x.shape[0]
in_im = np.zeros([sy, sy])
x_start = int(np.floor((sy-y_c)/2))
in_im[x_start:x_start+y_c, x_start:x_start+y_c] = 1.

D2 = 0.5                         # mm
tx, ty = 0.005, 0.005  # mm
t_x = np.arange(-D2/2, D2/2, tx)
t_sy = t_x.shape[0]
Intensity = np.zeros([t_sy, t_sy])
k = 0
for m in t_x:
    l = 0
    for n in t_x:
        Intensity[k, l] = diffraction(in_im, w_len, z, dx, dy, D1, m, n)
        l += 1
    k += 1
    print(k)
Intensity = Intensity/w_len
plt.figure(1)
plt.imshow(Intensity, cmap='gray')
plt.show()
