import cv2
import numpy as np
import glob
import sys

img_array = []
files= glob.glob('./3/*.png')
files.sort()
for i in range(0,24752):
    print(str(sys.argv[1])+str(i)+".png")
    img = cv2.imread(str(sys.argv[1])+str(i)+".png")
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)


out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'X264'), 15, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
