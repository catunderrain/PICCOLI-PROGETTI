def binary_search_recursive(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_recursive(arr, low, mid - 1, x)
        else:
            return binary_search_recursive(arr, mid + 1, high, x)
    else:
        return -1

arr = [2, 3, 4, 7, 40]
x = 2

result = binary_search_recursive(arr, 0, len(arr)-1, x)
if result != -1:
    print("Phần tử có trong mảng tại chỉ số", result)
else:
    print("Phần tử không có trong mảng")