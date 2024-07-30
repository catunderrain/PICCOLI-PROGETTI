import numpy as np
import cv2
import os
DIR = os.path.dirname(os.path.realpath(__file__))
IMG = '\\' + 'guardian.jpg'
PATH = DIR + IMG
PATH = r"C:\Users\Lenovo\Downloads\ichigo-kurosaki-3840x3840-11301.jpg"
img = cv2.imread(PATH)
SIZE = 160


def make_pixel(img, SIZE=32):
    base_shape = img.shape  
    print(base_shape)

    if base_shape[1] > base_shape[0]:
        print(0, base_shape[0])
        r = round(1/(base_shape[0]/SIZE), 1)
    else:
        print(1, base_shape[1])
        r = round(1/(base_shape[1]/SIZE), 1)
    print(r)
    r = 0.026
    img_mid1 = cv2.resize(img, (0,0), fx=r, fy=r)
    # img_mid2 = cv2.resize(img, (0,0), fx=r, fy=r, interpolation=cv2.INTER_NEAREST)
    img_mid = img_mid1
    # img_mid = np.concatenate((img_mid1, img_mid), 1)
    # img_up = cv2.resize(img_mid, (0,0), fx=1/r, fy=1/r, interpolation=cv2.INTER_NEAREST)
    img_up = cv2.resize(img_mid, (0,0), fx=1/r, fy=1/r, interpolation=cv2.INTER_AREA)
    
    return img_up


def make_loaves(imgin):
    cl = [0,127,255]
    img = imgin[::]
    for y in range(len(img)):
        for x in range(len(img[y])):
            for it in range(len(img[y][x])):
                for i in range(len(cl)-1):
                    if img[y][x][it] >= cl[i] and img[y][x][it] < cl[i+1]:
                        img[y][x][it] = cl[i]
    return img


if __name__ == "__main__":
    img_maked = make_pixel(img, SIZE)
    print(img_maked.shape)
    # img_maked = make_loaves(img_maked)
    print(DIR + '\\re' + IMG)
    # cv2.imshow(f'{SIZE, img_maked.shape}', img_maked)
    # cv2.waitKey(0)
    cv2.imwrite(DIR + '\\re.png', img_maked)
    