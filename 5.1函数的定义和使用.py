# %% 函数的理解和定义
'''
函数是一段具有特定功能的可重复的语句组
可以代码复用
使用保留字 
def <函数名><参数>:
    <函数体>
    return <返回值>
'''


def fact(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s


print(fact(5))
# %%


def fact1():
    print("空参数")


fact1()

# %% 可选参数


def fact(n, m=1):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s//m


print(fact(10))
print(fact(10, 5))
# %% 可变参数传递


def fact(n, *b):
    s = 1
    for i in range(1, n+1):
        s *= i
    for item in b:
        s *= item
    return s


print(fact(10))
print(fact(10, 2))
print(fact(10, 2, 3))
# %% 参数传递的两种方式


def fact(n, m=1):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s//m


print(fact(10, 5))  # 按照位置传递
print(fact(n=10, m=5))  # 按照名称传递
# %% 函数的返回值


def fact(n, m=1):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s//m, n, m # 元组类型


a,b,c=fact(10, 5)
print(a,b,c)
# %%
n,s=10,100
def fact(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s
print(fact(n),s)
# %%
n,s=10,100

def fact(n):
    global s
    for i in range(1,n+1):
        s*=i
    return s
print(fact(n),s)
# %%
ls=["F","f"]
def func(a):
    ls.append(a)
    return
func("C")
print(ls)