'''

'''
import random
import numpy as np

numset = np.sort(random.sample(range(20), 10))
step = 5
numset = [ 1,  3,  5,  7,  8,  9, 14, 16]

x = 16
tup = []
stop_i = 0
print(numset)
f = False
for i in range(0, len(numset), step):
    if numset[i] > x:
        tup = numset[i-step:i]
        stop_i = i-step
        print(tup)
        print(stop_i)
        f = True
        break

print(f)       
if not f:
    lentup = -(len(numset)%step)
    if lentup == 0:
        print('Dont have x')
    else:
        print('lentup',-(len(numset)%step))
        tup = numset[-(len(numset)%step):]
        stop_i = len(numset)+lentup
        print(tup)
        print(stop_i)
        

found = False
for i in range(len(tup)):
    if tup[i] == x:
        print('Position of x:', stop_i + i + 1)
        found = True
        break

if not found:
    print('Dont have x')
