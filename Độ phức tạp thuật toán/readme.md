Dưới đây là một số ví dụ về các độ phức tạp thời gian khác nhau cùng với giải thích và ví dụ minh họa:

1. **O(1) - Thời gian hằng số:**
   - Độ phức tạp không thay đổi dù kích thước dữ liệu đầu vào thay đổi.
   - Ví dụ: Truy cập một phần tử trong mảng hoặc tìm giá trị lớn nhất trong danh sách đã sắp xếp.
   ```python
   def get_first_element(arr):
       return arr[0]
   ```

2. **O(log n) - Thời gian logarit:**
   - Độ phức tạp tăng chậm khi kích thước dữ liệu tăng.
   - Ví dụ: Tìm kiếm nhị phân trong một mảng đã sắp xếp.
   ```python
   def binary_search(arr, target):
       low, high = 0, len(arr) - 1
       while low <= high:
           mid = (low + high) // 2
           if arr[mid] == target:
               return mid
           elif arr[mid] < target:
               low = mid + 1
           else:
               high = mid - 1
       return -1
   ```

3. **O(n) - Thời gian tuyến tính:**
   - Độ phức tạp tăng tỉ lệ thuận với kích thước dữ liệu.
   - Ví dụ: Tìm phần tử lớn nhất trong một mảng.
   ```python
   def find_max(arr):
       max_val = arr[0]
       for num in arr:
           if num > max_val:
               max_val = num
       return max_val
   ```

4. **O(n log n) - Thời gian tuyến tính nhân logarit:**
   - Thường gặp trong các thuật toán sắp xếp hiệu quả như merge sort, quicksort.
   ```python
   def merge_sort(arr):
       if len(arr) <= 1:
           return arr
       mid = len(arr) // 2
       left = merge_sort(arr[:mid])
       right = merge_sort(arr[mid:])
       return merge(left, right)

   def merge(left, right):
       result = []
       i = j = 0
       while i < len(left) and j < len(right):
           if left[i] < right[j]:
               result.append(left[i])
               i += 1
           else:
               result.append(right[j])
               j += 1
       result.extend(left[i:])
       result.extend(right[j:])
       return result
   ```

5. **O(n^2) - Thời gian bình phương:**
   - Độ phức tạp tăng theo bình phương kích thước dữ liệu, thường gặp trong các thuật toán kém hiệu quả như bubble sort, selection sort.
   ```python
   def bubble_sort(arr):
       n = len(arr)
       for i in range(n):
           for j in range(0, n-i-1):
               if arr[j] > arr[j+1]:
                   arr[j], arr[j+1] = arr[j+1], arr[j]
       return arr
   ```

6. **O(2^n) - Thời gian lũy thừa:**
   - Độ phức tạp tăng rất nhanh khi kích thước dữ liệu tăng, thường gặp trong các thuật toán đệ quy không tối ưu như bài toán Fibonacci không tối ưu.
   ```python
   def fibonacci(n):
       if n <= 1:
           return n
       return fibonacci(n-1) + fibonacci(n-2)
   ```

7. **O(n!) - Thời gian giai thừa:**
   - Độ phức tạp tăng cực kỳ nhanh, thường gặp trong các bài toán hoán vị toàn bộ các phần tử.
   ```python
   def permutations(arr):
       if len(arr) == 0:
           return [[]]
       result = []
       for i in range(len(arr)):
           elem = arr[i]
           rest = arr[:i] + arr[i+1:]
           for p in permutations(rest):
               result.append([elem] + p)
       return result
   ```

Những ví dụ trên minh họa các mức độ phức tạp khác nhau và cách chúng ảnh hưởng đến hiệu suất của thuật toán khi kích thước dữ liệu đầu vào thay đổi.
#
#
#
Ngoài những độ phức tạp phổ biến đã nêu, còn một số độ phức tạp khác thường gặp trong các thuật toán và vấn đề cụ thể:

8. **O(sqrt(n)) - Thời gian căn bậc hai:**
   - Thường gặp trong các thuật toán sàng lọc số nguyên tố hoặc tìm ước số.
   ```python
   def is_prime(n):
       if n <= 1:
           return False
       for i in range(2, int(n**0.5) + 1):
           if n % i == 0:
               return False
       return True
   ```

9. **O(n^c) - Thời gian đa thức:**
   - Một cách tổng quát để chỉ độ phức tạp tăng theo cấp số nhân với một hằng số c. Thường gặp trong các thuật toán xử lý đồ thị như floyd-warshall (O(n^3)).
   ```python
   def floyd_warshall(graph):
       n = len(graph)
       dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
       for k in range(n):
           for i in range(n):
               for j in range(n):
                   dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
       return dist
   ```

10. **O(2^n) - Thời gian lũy thừa cơ bản:**
    - Như đã nêu trước đó, thường gặp trong các thuật toán đệ quy không tối ưu như bài toán Fibonacci không tối ưu.

11. **O(b^d) - Thời gian theo cấp số nhân:**
    - B với b là cơ sở và d là độ sâu, thường gặp trong các thuật toán duyệt đồ thị như tìm kiếm theo chiều sâu (DFS) và tìm kiếm theo chiều rộng (BFS) trong cây hoặc đồ thị.
    ```python
    def bfs(graph, start):
        visited = []
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.append(vertex)
                queue.extend(set(graph[vertex]) - set(visited))
        return visited
    ```

12. **O(log log n) - Thời gian logarit kép:**
    - Độ phức tạp này thường gặp trong một số thuật toán liên quan đến việc tìm kiếm và sắp xếp, chẳng hạn như một số phiên bản của cây tìm kiếm nhị phân.
    ```python
    # Chỉ là một ví dụ đơn giản về truy cập nhanh trong một cây tìm kiếm nhị phân
    ```

13. **O(n!) - Thời gian giai thừa:**
    - Như đã đề cập trước đó, thường gặp trong các bài toán hoán vị toàn bộ các phần tử.

14. **O(n^n) - Thời gian cực kỳ tăng nhanh:**
    - Thường gặp trong các bài toán tổ hợp phức tạp, ví dụ như bài toán sắp xếp hoán vị với nhiều ràng buộc.

15. **O(k^n) - Thời gian tăng theo cơ số k:**
    - Gặp trong các bài toán có nhiều lựa chọn ở mỗi bước như giải mã chữ số.
    ```python
    def count_decodings(digits, n):
        if n == 0 or n == 1:
            return 1
        count = 0
        if digits[n-1] > '0':
            count = count_decodings(digits, n-1)
        if (digits[n-2] == '1' or (digits[n-2] == '2' and digits[n-1] < '7')):
            count += count_decodings(digits, n-2)
        return count
    ```

Những độ phức tạp trên phản ánh nhiều loại thuật toán và các vấn đề khác nhau, từ các bài toán đơn giản đến phức tạp trong lĩnh vực khoa học máy tính.