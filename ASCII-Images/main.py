import matplotlib.image as image
import numpy as np


def layer(x, key):
    l1 = []
    l2 = []
    l3 = []
    for row in x:
        for node in row:
            l1.append(node[0])
            l2.append(node[1])
            l3.append(node[2])
    if key == 1:
        return l1
    elif key == 2:
        return l2
    elif key == 3:
        return l3
    else:
        return 'None layer'


def gray(x):
    a = layer(x, 1)
    b = layer(x, 2)
    c = layer(x, 3)
    d = []
    if np.max(a) > 1:
        t = 3
    else:
        t = 255
    for i in range(len(a)):
        m = round((a[i]+b[i]+c[i])*t/3, 0)
        d.append(m)
    return(d)


def show(img, shap):
    pt = gray(img)
    pts = []
    for i in range(len(pt)):
        if pt[i] <= 10:
            pts.append('  ')
        elif pt[i] <= 20:
            pts.append('..')
        elif pt[i] <= 30:
            pts.append('--')
        elif pt[i] <= 40:
            pts.append(',,')
        elif pt[i] <= 50:
            pts.append('::')
        elif pt[i] <= 60:
            pts.append('==')
        elif pt[i] <= 70:
            pts.append('rr')
        elif pt[i] <= 80:
            pts.append('ss')
        elif pt[i] <= 90:
            pts.append('oo')
        elif pt[i] <= 100:
            pts.append('cc')
        elif pt[i] <= 110:
            pts.append('zz')
        elif pt[i] <= 120:
            pts.append('uu')
        elif pt[i] <= 130:
            pts.append('xx')
        elif pt[i] <= 140:
            pts.append('ww')
        elif pt[i] <= 150:
            pts.append('mm')
        elif pt[i] <= 160:
            pts.append('WW')
        elif pt[i] <= 170:
            pts.append('RR')
        elif pt[i] <= 180:
            pts.append('OO')
        elif pt[i] <= 190:
            pts.append('88')
        elif pt[i] <= 200:
            pts.append('BB')
        elif pt[i] <= 210:
            pts.append('##')
        elif pt[i] <= 220:
            pts.append('&&')
        elif pt[i] <= 230:
            pts.append('00')
        elif pt[i] <= 240:
            pts.append('00')
        elif pt[i] <= 250:
            pts.append('QQ')
        elif pt[i] <= 260:
            pts.append('@@')
        else:
            pts.append('d')

    ptss = ''.join(pts)
    for j in range(shap[0] - 1):
        k = 2*j*shap[1]
        for i in range(shap[1]*2):
            print(ptss[i+k], end='')
        print('')
    print(shap)


def main():
    print('WELCOME!')
    img = r"C:\Users\Lenovo\Desktop\2b87a08ae4c732996bd6.jpg"
    img = image.imread(img)
    shap = img.shape
    show(img, shap)


main()