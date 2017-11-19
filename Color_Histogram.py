import numpy as np
import cv2

box_dim = 8
box_size = box_dim*box_dim*box_dim

hist = np.zeros(box_size)

for i in range(0, 500):
    image = cv2.imread('./imgs/'+str(i+1)+'.jpg')
    for x in range(0, 511):
        for y in range(0, 511):
            r = image[x, y][0]
            g = image[x, y][1]
            b = image[x, y][2]
            r = int(r/(256/box_dim))
            g = int(g/(256/box_dim))
            b = int(b/(256/box_dim))
            index = r+g*box_dim+b*box_dim*box_dim
            hist[index] += 1
    print(i)

np.savetxt("./data/histogram.csv", hist, delimiter=",")