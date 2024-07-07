
import random
import numpy as np


ar = sorted(random.sample(range(20), 16))
key = random.randint(0,20)
print(ar)
print(key)

def bi(ar, l, r, key):
    if r >= l:
        mid = (l + r)//2
        if ar[mid] == key:
            return mid
        elif ar[mid] > key:
            return bi(ar, l, mid-1, key)
        else:
            return bi(ar, mid+1, r, key)
    else:
        return -1


re = bi(ar, 0, len(ar)-1, key)
print(re)