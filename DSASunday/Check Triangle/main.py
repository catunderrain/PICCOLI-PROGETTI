'''
1. Khái niệm thuật toán
2. Tính chất thuật toán
    Tính dừng
    Tính xác định
    Tính đúng
    Đầu vào và đầu ra
    Tính hiệu quả
    Tính tổng quát
3. Cách biểu diễn thuật toán
4. Các cấu trúc cơ bản của thuật toán
5. Một số thuật toán cơ bản
6. Bài tập
'''
class A:
    def Tri_Check(a, b, c):
        def l(x, y): 
            import numpy as np
            return np.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)
        l1 = l(a, b)
        l2 = l(a, c)
        l3 = l(b, c)
        if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
            print('Tri')
            if l1 == l2 or l1 == l3 or l2 == l3:
                print('Can')
            return True
        else:
            print('Not tri')
            return False
        
        
    def CheckNT(a):
        if a <= 3:
            pass
        
        
if __name__ == "__main__":
    A.Tri_Check((0,0),(1,0),(2,0))
    pass