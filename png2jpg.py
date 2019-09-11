import os
from PIL import Image
import sys
import numpy as np

path = "/home/dingjin/test/images/"
newpath = '/home/dingjin/test/JPEGImages/'

print(path)

for filename in os.listdir(path):

    if os.path.splitext(filename)[1] == '.png':
        print(filename)
        im = Image.open(path + filename)
        rgb_im = im.convert('RGB')
        rgb_im.save(newpath + filename + '.jpg')
    else:
        print('Do nothing')
