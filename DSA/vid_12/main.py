import random
import numpy as np
ar = random.sample(range(-20,20),10)
# ar = [4,5,3,2,1]
ar = np.array(ar)
print('origin  : ',ar)


def A(ar):
    ar = list(ar)
    ar_A = np.array([min(ar)] + ar)
    ar_B = np.array(ar + [max(ar)])
    ar_C = ar_B - ar_A
    
    print('min + ar: ', ar_A)
    print('ar + max: ', ar_B)
    print('div     : ', ar_C)
    
    divmap = list(np.where(ar_C < 0)[0])
    divmap = [0] + divmap + [len(ar)]
    glomap = [ar[divmap[i]:divmap[i+1]] for i in range(len(divmap)-1)]
    m = max([len(i) for i in glomap])
    mmap = [li for li in glomap if len(li) == m]
    
    print('negative index map: ', divmap)
    print('split ar map      : ', glomap)
    print('max len           : ', m)
    print('longest sub_ar    : ', mmap)
    
    return mmap
        
    
A(ar)