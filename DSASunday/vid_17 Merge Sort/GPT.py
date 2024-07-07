def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Tìm điểm giữa của mảng
        left_half = arr[:mid]  # Chia mảng thành nửa trái
        right_half = arr[mid:]  # Chia mảng thành nửa phải

        merge_sort(left_half)  # Đệ quy sắp xếp nửa trái
        merge_sort(right_half)  # Đệ quy sắp xếp nửa phải

        i = j = k = 0

        # Trộn nửa trái và nửa phải
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Kiểm tra các phần tử còn lại
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Ví dụ sử dụng
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Mảng đã sắp xếp:", arr)