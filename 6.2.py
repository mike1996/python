# 载入cv2库加载图片,图片为方形孔
import cv2
# 载入numpy库做数学计算.
import numpy as np
# 载入matplotlib库显示结果图像
from matplotlib import pyplot as plt
import time
from numba import jit


start=time.perf_counter()

def drawRect():
    img = np.zeros((400, 400, 3), np.uint8)
    cv2.rectangle(img, (150, 150), (250, 250), (255, 255, 255), # 第一个坐标为矩形起始点,第二个坐标为矩形结束点
                  thickness=-1)  # thickness为负值指全部填充
    cv2.resizeWindow('image', 400, 400)  # 定义frame的大小
    cv2.imwrite('rect.png', img)
    # cv2.imshow('image', img)  # 显示生成的矩形


def drawCircle():
    img = np.zeros((400, 400, 3), np.uint8)
    img = cv2.circle(img, (200, 200), 50, (255, 255, 255), -1) # 半径为50
    cv2.imwrite('circle.png', img)


drawCircle()
drawRect()
# 读取图片
img1 = cv2.imread('rect.png', 0)  # 读取矩形
img2 = cv2.imread('circle.png', 0)  # 读取圆孔
#propagator = np.zeros((400, 400))
# 定义大小
n1 = 200
n2 = 200
# 定义观察距离 z
Z = 1
# 定义波长
l_ambda = 800e-6
# 定义角谱坐标,注意与u,v与图片大小x,y相同
u= np.arange(-n1, n1, 1)
v = np.arange(-n2, n2, 1)
U, V = np.meshgrid(u, v)
propagator = np.ones((400, 400))
# U0角谱 方法一
@jit(nopython=True)
def jisuan():
    for m in u:
        for n in v:
            propagator[m,n] = np.exp(
                    2*np.pi*1j*Z*np.sqrt((1/l_ambda)**2-U[m, n]**2-V[m, n]**2))
    return propagator

# U0角谱 方法二
#propagator=np.exp(2*np.pi*1j*(Z)*np.sqrt((1/l_ambda)**2-(U)**2-(V)**2))
propagator=jisuan()
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
# 定义强度
i = 1e15
diffracted_field1 = np.abs(field_ifft1)+i
diffracted_field2 = np.abs(field_ifft2)+i
end=time.perf_counter()
print("耗时:{:}s".format(end-start))
# 定义画布
plt.figure(1)
# 绘画结果
plt.subplot(121), plt.imshow(img1, cmap='gray')
plt.title('Amplitude Boundary Condition1'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(diffracted_field1, cmap='plasma')
plt.title('Diffracted Field1'), plt.xticks([]), plt.yticks([])
plt.figure(2)
plt.subplot(121), plt.imshow(img2, cmap='gray')
plt.title('Amplitude Boundary Condition2'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(diffracted_field2, cmap='plasma')
plt.title('Diffracted Field2'), plt.xticks([]), plt.yticks([])
# Show the image
plt.show()
