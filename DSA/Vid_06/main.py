
ar = [3,2,5,1,16,12,10,19,5,2,7,7]
print(ar)

def A(ar):
    for i in range(1,len(ar)):
        j=i
        while j > 0 and ar[j] < ar[j-1]:
            ar[j], ar[j-1] = ar[j-1], ar[j]
            j -= 1
    return ar

def insertion_sort(arr):
    # Duyệt qua từng phần tử trong mảng (bắt đầu từ phần tử thứ hai)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Di chuyển các phần tử của arr[0..i-1], lớn hơn key, sang vị trí tiếp theo phía trước chúng
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(A(ar))
                        