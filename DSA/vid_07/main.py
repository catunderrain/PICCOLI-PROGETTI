ar = [3,2,5,1,16,12,10,19,5,2,7,7]
print(ar)

def A(ar):
    for i in range(len(ar)):
        i_min = i
        for j in range(i+1,len(ar)):
            if ar[j] < ar[i_min]:
                i_min = j
        ar[i], ar[i_min] = ar[i_min], ar[i]
    return ar
print(A(ar))