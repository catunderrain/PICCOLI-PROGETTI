
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
        
hanoi(3,0,2,1)

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

'''
H 3 i j k
	H 2 i k j
		H 1 i j k
			_p1 i>>j
		_p2 i>>k
		H 1 j k i
			_p1 j>>k
	_p3 i>>j
	H 2 k j i
		H1 k i j
			_p1 k>>i
		_p2 k>>j
		H1 i j k
			_p1 i>>j
'''