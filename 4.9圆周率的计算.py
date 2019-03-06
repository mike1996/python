# %%
pi = 0
N = 100
for k in range(N):
    pi += 1/pow(16, k)*(
        4/(8*k+1)-2/(8*k+4) -
        1/(8*k+5)-1/(8*k+6))
print("圆周率是:{}".format(pi))
# %% 蒙特卡洛
from time import perf_counter
from random import random
darts = 1000*1000
hits = 0.0
start = perf_counter()
for i in range(1, darts+1):
    x,y=random(),random()
    dist=pow(x**2+y**2,0.5)
    if dist<=1.0:
        hits+=1
pi = 4*(hits/darts)
print("圆周率是:{}".format(pi))
print("运行时间是:{}".format(perf_counter()-start))