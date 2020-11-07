# -*- coding: utf-8 -*-

# the shell convert picture to chr
import cv2
import os
import numpy as np
from PIL import Image,ImageFont,ImageDraw

def transf(fpath,resolution,fonts=None):
    imgGrey = cv2.imread(fpath, 0)
    #print(imgGrey.shape)
    new_high = int(imgGrey.shape[0]/resolution)
    new_wide = int(imgGrey.shape[1]/resolution)
    img2 = cv2.resize(imgGrey,(new_wide,new_high))
    #print(img2.shape)
    imgnew = np.empty((img2.shape[0],img2.shape[1]),dtype='object')
    imgnew[:,:]='.'
    imgnew[img2<=51] = '#'
    imgnew[(img2>51)&(img2<=87)] = '@'
    imgnew[(img2>87)&(img2<=102)] = '8'
    imgnew[(img2>102)&(img2<=123)] = '+'
    imgnew[(img2>123)&(img2<=143)] = '~'
    imgnew[(img2>143)&(img2<=204)] = '-'

    image = Image.new("RGB", (new_wide*resolution, new_high*resolution), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # use a  font
    if fonts == None:
        font = ImageFont.truetype("C:\\WINDOWS\\Fonts\\times.ttf", resolution)
    else:
        font = ImageFont.truetype(fonts, resolution)

    # draw
    for raw in np.arange(imgnew.shape[0]):
        for col in np.arange(imgnew.shape[1]):
            draw.text((col*resolution,raw*resolution), imgnew[raw,col], font=font, fill = "#000000")


    new_fpath = os.path.splitext(fpath)[0] + '_result.png'
    #image.show()
    image.save(new_fpath)
