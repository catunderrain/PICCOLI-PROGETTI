import random
ar = random.sample(range(-20,20),20)
print(ar)

def A(ar):
    maxs = ar[0]
    i_max = 0
    j_max = 0
    for i in range(len(ar)):
        for j in range(i,len(ar)):
            s = sum(ar[i:j+1])
            if s>maxs:
                maxs = s
                i_max = i
                j_max = j
                print(i, j, s)
    return i_max, j_max, maxs


def Kadane(arr):
    max_current = max_global = arr[0]
    i_max = 0
    j_max = 0
    im = 0
    jm = 0
    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        if max_current == arr[i]:
            im = i
        else:
            jm = i 
        if max_current > max_global:
            max_global = max_current
            i_max = im
            j_max = jm
            if j_max < i_max: j_max = i_max
    return i_max, j_max, max_global    


A(ar)
print(Kadane(ar))