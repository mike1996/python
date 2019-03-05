# 3.6程序计时应用
import time


def wait():
    time.sleep(3.3)


# 测量时间：perf_counter()
start = time.perf_counter()
wait()
end = time.perf_counter()
print(end-start)
'''
sleep(s)
sleep休眠函数
def wait(): 
    time.sleep(3.3)
wait()
'''
