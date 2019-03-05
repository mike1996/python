# 文本进度条
import time
print("执行开始".center(50, '-'))
scale = 50
for i in range(51):
    a = '*' * i
    b = '-' * (50-i)
    c = (i / scale)*100
    print("\r{:2.2f}%[{}->{}".format(c, a, b), end='')
    time.sleep(0.1)
print("\n"+"执行完毕".center(50, '-'))
