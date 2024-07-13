ar = [3,2,5,1,16,12,10,19,2,5,4,3,7,8,9]
print(ar)
def A(ar):
    f = False
    count = 1
    while not f:
        print('time', count)
        count += 1
        a1 = ar + [max(ar)]
        a2 = [min(ar)] + ar
        import numpy as np

        a1 = np.array(a1)
        a2 = np.array(a2)
        a3 = a1-a2
        print(np.array(ar))
        print(a1)
        print(a2)
        print(a3)
        c = 0
        # for i in range(len(a3)-1, -1, -1):
        for i in range(len(a3)):
            if a3[i] < 0:
                ar[i-1], ar[i] = ar[i], ar[i-1]
                c += 1
                
        if c == 0: f = True
        print(ar)
        print('-------')
            
A(ar)