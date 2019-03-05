# 星号三角形
a = eval(input())
for i in range(a):
    if (i+1) % 2 == 1:
        b = '*'*(i+1)
        b = str(b)
        print(b.center(a, " "))
