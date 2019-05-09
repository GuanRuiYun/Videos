# * coding:utf-8 *
"""
@Author: GRYun
@Date  : 19-5-7
@Time  : 上午8:27
@File  : convolved.py
@IDE   : PyCharm
@Func  :
"""
import cv2
import numpy as np

ipath = './img/'
fname = 'Youku_00000_l001.bmp'
# fname = 'lena.jpg'
img = cv2.imread(ipath+fname,0)

cv2.imshow("Youku",img)

# print(img.shape)

#  cv2.BORDER_CONSTANT padding for the fix value
cons = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=0)

# cv2.BORDER_CONSTANT padding for the type of default
default = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_DEFAULT)


# define the kernel of convolved
kernel = np.ones((3,3),np.float) / 10

# convolved operate , the '-1' is  channel equaling the channel of original
dst = cv2.filter2D(img,-1,kernel)

print(cons)
print(default)
print(dst)
cv2.imshow("Youku_Fix",cons)
cv2.imshow("Youku_De",default)
cv2.imshow("Youku_Con",dst)
# print(cons.shape)
cv2.waitKey(0)