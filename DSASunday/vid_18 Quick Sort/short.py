
import random 
ar = random.sample(range(-0,20),6)
print(ar)


def QuickSort(ar,l,r):
    if l == r:
        return [ar[l]]
    else:
        pivot = ar[l]
        ra = []
        la = []
        for i in range(l+1, r+1):
            if ar[i] >= pivot:
                ra.append(ar[i])
            else:
                la.append(ar[i])
        if len(la) > 0:
            la = QuickSort(la,0,len(la)-1)
        if len(ra) > 0:
            ra = QuickSort(ra,0,len(ra)-1)
        r = la + [pivot] + ra
        
    return r


print(QuickSort(ar,0,len(ar)-1))

