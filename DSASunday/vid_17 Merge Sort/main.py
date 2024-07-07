
def Merge(arle, arri):
    re = []
    print('   aL-aR', arle, arri)
    while (len(arle)) != 0 and (len(arri) != 0):
        if arle[0] <= arri[0]:
            re.append(arle[0])
            arle = arle[1::]
        else:
            re.append(arri[0])
            arri = arri[1::]
    arle += arri
    re += arle
    print('===== re', re, end='\n\n')
    return re


def MergeSort(ar, left, right):
    if left == right:
        print('   aL=aR', ar[left])
        return [ar[left]]
    else:
        print('>>>  L-R', left, right)
        mid = int((left+right)/2)
        arle = MergeSort(ar, left, mid)
        arri = MergeSort(ar, mid+1, right)
        re = Merge(arle, arri)
        return re
        
        
if __name__ == '__main__':
    ar = [1,3,2,4,5,-1, -1]
    print(ar)
    import random
    # ar = random.sample(range(-1000,1000), 2000)

    print(MergeSort(ar, 0, len(ar)-1))