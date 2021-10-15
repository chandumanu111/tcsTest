# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 23:01:37 2019

@author: Manu
"""
#image flipping
'''
from PIL import Image
img=Image.open('textmirror.jpg')
transpose_image=img.transpose(Image.FLIP_LEFT_RIGHT)
transpose_image.save('corrected.jpg')
print("done flipping")
'''


import cv2
img=cv2.imread('bullethole.jpg')
clahe=cv2.createCLAHE()
gray_img=cv2.cvtColor(img,cv2.Color_BGR2GRAY)
enh_image=clahe.apply(gray_img)
cv2.imwrite('enhanced.jpg',enh_image)
print("enhanced")