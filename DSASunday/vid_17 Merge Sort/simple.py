
def Merge(arle, arri):
    re = []
    while (len(arle) != 0) and (len(arri) != 0):
        if arle[0] <= arri[0]:
            re.append(arle[0])
            arle = arle[1::]
        else:
            re.append(arri[0])
            arri = arri[1::]
    arle += arri
    re += arle
    return re


def MergeSort(ar, left, right):
    if left == right:
        return [ar[left]]
    else:
        mid = int((left+right)/2)
        arle = MergeSort(ar, left, mid)
        arri = MergeSort(ar, mid+1, right)
        re = Merge(arle, arri)
        return re
        
def main():
    ar = [1,3,2,4,5,-1,-1]

    import random
    ar = random.sample(range(-50,50), 10)

    print(ar)
    arm = MergeSort(ar, 0, len(ar)-1)
    print(arm)
    armd = [-1 if (arm[i+1] - arm[i]) < 0 else 0 for i in range(len(arm)-1)]
    print(armd)
    
main()