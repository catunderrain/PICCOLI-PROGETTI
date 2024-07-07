**Brute force** (tạm dịch: tấn công vét cạn) là một phương pháp giải quyết vấn đề bằng cách thử tất cả các khả năng có thể cho đến khi tìm được giải pháp đúng. Đây là cách tiếp cận đơn giản và dễ hiểu nhất nhưng thường không hiệu quả đối với các bài toán có không gian tìm kiếm lớn, vì thời gian thực hiện có thể tăng lên rất nhanh.

### Ví dụ: Giải Thuật Brute Force cho Bài Toán Tìm Dãy Con Liên Tục Có Tổng Lớn Nhất

Để minh họa phương pháp brute force, chúng ta sẽ giải quyết bài toán tìm dãy con liên tục có tổng lớn nhất trong một mảng. Với brute force, ta sẽ kiểm tra tất cả các dãy con có thể và tính tổng của chúng, sau đó chọn ra dãy con có tổng lớn nhất.

Dưới đây là cách triển khai bằng Python:

```python
def max_subarray_sum_brute_force(arr):
    n = len(arr)
    max_sum = float('-inf')  # Khởi tạo tổng lớn nhất với giá trị âm vô cùng
    
    # Duyệt qua tất cả các dãy con có thể
    for i in range(n):
        for j in range(i, n):
            current_sum = sum(arr[i:j+1])
            if current_sum > max_sum:
                max_sum = current_sum
                
    return max_sum

# Ví dụ sử dụng
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Tổng lớn nhất của dãy con liên tục là:", max_subarray_sum_brute_force(arr))
```

Kết quả sẽ là:

```
Tổng lớn nhất của dãy con liên tục là: 6
```

### Giải Thích:

1. Khởi tạo `max_sum` với giá trị âm vô cùng để đảm bảo bất kỳ tổng nào cũng lớn hơn.
2. Duyệt qua tất cả các cặp chỉ số (i, j) sao cho `i <= j`.
3. Với mỗi cặp (i, j), tính tổng của dãy con từ `arr[i]` đến `arr[j]`.
4. Cập nhật `max_sum` nếu tổng của dãy con hiện tại lớn hơn `max_sum`.
5. Trả về `max_sum` là tổng lớn nhất tìm được.

### Độ Phức Tạp Thời Gian:

Phương pháp brute force này có độ phức tạp thời gian là \(O(n^3)\), do có ba vòng lặp lồng nhau: hai vòng để chọn cặp chỉ số (i, j) và một vòng để tính tổng của dãy con từ `i` đến `j`. Điều này làm cho phương pháp brute force trở nên không hiệu quả đối với các mảng có kích thước lớn.

So sánh với thuật toán Kadane với độ phức tạp thời gian là \(O(n)\), phương pháp brute force chậm hơn rất nhiều và không được sử dụng trong thực tế cho các bài toán lớn. Tuy nhiên, brute force lại dễ hiểu và thường được sử dụng như một cách tiếp cận ban đầu hoặc để kiểm tra tính đúng đắn của các thuật toán phức tạp hơn.