def Merge(arle, arri):
    re = []
    li = ri = 0
    while li < len(arle) and ri < len(arri):
        if arle[li] <= arri[ri]:
            re.append(arle[li])
            li += 1
        else:
            re.append(arri[ri])
            ri += 1

    re.extend(arle[li:])
    re.extend(arri[ri:])
    return re

def MergeSort(ar, left, right):
    if left == right:
        return [ar[left]]
    else:
        mid = (left + right) // 2
        arle = MergeSort(ar, left, mid)
        arri = MergeSort(ar, mid + 1, right)
        re = Merge(arle, arri)
        return re


ar = [1,3,2,4,5,-1,-1]

import random
ar = random.sample(range(-20,20), 10)

print(ar)
arm = MergeSort(ar, 0, len(ar)-1)
print(arm)
armd = [-1 if (arm[i+1] - arm[i]) < 0 else 0 for i in range(len(arm)-1)]
print(armd)
