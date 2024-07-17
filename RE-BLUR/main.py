
'''
a = x = y = 0
a[0,x-1,y-1] = 0
a[0,x-1,y] = 0
a[0,x-1,y+1] = 0
a[0,x,y-1] = 0
a[0,x,y] = 0
a[0,x,y+1] = 0
a[0,x+1,y-1] = 0
a[0,x+1,y] = 0
a[0,x+1,y+1] = 0

a[1,x,y] = (a[0,x-1,y-1] + a[0,x-1,y] + a[0,x-1,y+1] + a[0,x,y-1] + a[0,x,y] + a[0,x,y+1] + a[0,x+1,y-1] + a[0,x+1,y] + a[0,x+1,y+1])/9

a[0,x-1,y-1] = 9*a[1,x-1,y-1] - D(a[0,x-1,y-1])
a[0,x-1,y] = 9*a[1,x-1,y] - D(a[0,x-1,y])
a[0,x-1,y+1] = 9*a[1,x-1,y+1] - D(a[0,x-1,y+1])
a[0,x,y-1] = 9*a[1,x,y-1] - D(a[0,x,y-1])
a[0,x,y] = 9*a[1,x,y] - D(a[0,x,y])
a[0,x,y+1] = 9*a[1,x,y+1] - D(a[0,x,y+1])
a[0,x+1,y-1] = 9*a[1,x+1,y-1] - D(a[0,x+1,y-1])
a[0,x+1,y] = 9*a[1,x+1,y] - D(a[0,x+1,y])
a[0,x+1,y+1] = 9*a[1,x+1,y+1] - D(a[0,x+1,y+1])


a[0,x,y] = 9*a[1,x,y] - D(a[0,x,y])
         = 9*a[1,x,y] -  D(a[1,x,y]) + 8*S(a[0,x,y])
         = 9*a[1,x,y] -  D(a[1,x,y]) + 8*a[1,x,y]/9
         = 89*a[1,x,y]/9 - D(a[1,x,y])
'''


import cv2
import numpy as np


img = cv2.imread(r"C:\Users\Lenovo\Desktop\img.jpg")
img = cv2.resize(img, (0,0), fx = 0.3, fy = 0.3)
print(img.shape)
for x in img:
    for y in x:
        img[x,y]


img = np.array(img)
cv2.imshow('', img)
cv2.waitKey(0)
cv2.destroyAllWindows()