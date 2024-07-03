
count = 0

def hanoi(n, i, j, k):
    global count
    c = ['A', 'B', 'C']
    if n == 1:
        count += 1
        print(f'Step {count}{(5-len(str(count)))*' '}plate {n}: {c[i]} > {c[j]}')
    else:
        hanoi(n-1, i, k, j)
        count += 1
        print(f'Step {count}{(5-len(str(count)))*' '}plate {n}: {c[i]} > {c[j]}')
        hanoi(n-1, k, j, i)
        
hanoi(12,0,2,1)

'''
1 : 1
2 : 3
3 : 7
4 : 15
5 : 31
6 : 63
7 : 127
...
12: 4095
'''