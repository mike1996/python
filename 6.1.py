# 载入numpy库做数学计算.
import numpy as np
# 载入matplotlib库显示结果图像
from matplotlib import pyplot as plt
import time

start = time.perf_counter()
# def drawRect():
#    img = np.zeros([400,400]
#    cv2.rectangle(img, (150, 150), (250, 250), (255, 255, 255), # 第一个坐标为矩形起始点,第二个坐标为矩形结束点
#                  thickness=-1)  # thickness为负值指全部填充
#    cv2.resizeWindow('image', 400, 400)  # 定义frame的大小
#    cv2.imwrite('rect.png', img)
#    # cv2.imshow('image', img)  # 显示生成的矩形

img1 = np.zeros([200, 200])
x, y = np.shape(img1)
img1[100-10:100+100, 100-10:100+10] = 1
plt.imshow(img1)

img2 = np.zeros([200, 200])
for m in range(200):
    for n in range(200):
        if (m-100)**2+(n-100)**2 <= 500:
            img2[m, n] = 1
plt.imshow(img2)


# 读取图片
propagator = np.ones((200, 200))
# 定义大小
n1 = 100
n2 = 100
# 定义观察距离 z
Z = 3
# 定义波长
l_ambda = 500e-6
# 定义角谱坐标,注意与u,v与图片大小x,y相同
u = np.arange(-n1, n1, 1)
v = np.arange(-n2, n2, 1)
U, V = np.meshgrid(u, v)

# U0角谱 方法一

for m in u:
    for n in v:
        propagator[m, n] = np.exp(
            2*np.pi*1j*Z*np.sqrt((1/l_ambda)**2-U[m, n]**2-V[m, n]**2))

# U0角谱 方法二
# propagator=np.exp(2*np.pi*1j*(Z)*np.sqrt((1/l_ambda)**2-(U)**2-(V)**2))

# 透射函数傅里叶变换
f1 = np.fft.fft2(img1)
f2 = np.fft.fft2(img2)
# 修正高低频
fshift1 = np.fft.fftshift(f1)
fshift2 = np.fft.fftshift(f2)
# 将两个矩阵相乘：傅里叶变换和传播矩阵。
field1 = fshift1*propagator
field2 = fshift2*propagator
# 计算逆傅立叶变换
field_ifft1 = np.fft.ifft2(field1)
field_ifft2 = np.fft.ifft2(field2)
diffracted_field1 = np.abs(field_ifft1)
diffracted_field2 = np.abs(field_ifft2)
end = time.perf_counter()
print("耗时:{:}s".format(end-start))
plt.figure(1)
plt.imshow(diffracted_field1,cmap='gray')
plt.figure(2)
plt.imshow(diffracted_field2,cmap='gray')
plt.show()
