# -*- coding: utf-8 -*-
#======================================================
#  Convert the picture to picture shown by character
#
#  A simple test by Wang Bingwen 
#                    2020-11-7
#======================================================

import pic2chr


# input the file
fpath = 'D:\\work\\python\\pic_to_chr\\test_cat.jpg'

# set resolution larger than 2 but less than the picture's frame
# smaller means better but slower
resolution = 2

# you can set fonts that you like
# for example (defult):
# 'C:\\WINDOWS\\Fonts\\times.ttf'
fonts = None

pic2chr.transf(fpath=fpath,resolution=resolution,fonts=fonts)
