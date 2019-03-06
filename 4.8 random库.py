# %%
# random库是生成随机数的库
# 随机数种子seed决定了随机数,可以复现随机数程序
import random
random.seed(10)
random.random()
# %%扩展随机数函数
# randint(a,b)生成一个[a,b]之间的整数
random.randint(0,100)
# %%
# randrange(m,n,[,k])
# %%
random.randrange(1,10,3)
# %%
random.getrandbits(16)
# %%
random.uniform(10,100)
# %%
random.choice([1,2,3,4,5])
#%%
s=[1,2,3,4,5,6,7,8]
random.shuffle(s)
print(s)

