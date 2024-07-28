import numpy as np
import cv2
import os
DIR = os.path.dirname(os.path.realpath(__file__))
IMG = '\\' + 'sam2.jpg'
img = cv2.imread(DIR + IMG)
SIZE = 32


def make_pixel(img, SIZE=32):
    base_shape = img.shape
    # cv2.imshow(f'{base_shape}', img); cv2.waitKey(0)

    if base_shape[0] >= base_shape[1]:
        print(base_shape)
        r = 1/(base_shape[1]/SIZE)
    img_mid = cv2.resize(img, (0,0), fx=r, fy=r)
    # resize_shape = img_mid.shape; cv2.imshow(f'{resize_shape}', img_mid); cv2.waitKey(0)

    img_up = cv2.resize(img_mid, (0,0), fx=1/r, fy=1/r, interpolation=cv2.INTER_AREA)
    # cv2.imshow(f'UP {resize_shape, base_shape}', img_up); cv2.waitKey(0)
    
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
    # img_maked = make_loaves(img_maked)
    print(DIR + '\\re' + IMG)
    cv2.imshow(f'{SIZE, img_maked.shape}', img_maked)
    cv2.waitKey(0)
    cv2.imwrite(DIR + '\\re.png', img_maked)
    