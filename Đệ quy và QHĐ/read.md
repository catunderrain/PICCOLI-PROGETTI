Anh yêu, đệ quy và quy hoạch động (dynamic programming) đều là các kỹ thuật lập trình để giải quyết các bài toán phức tạp bằng cách chia nhỏ thành các bài toán con. Dưới đây là mối quan hệ và sự khác biệt giữa chúng:

### Mối Quan Hệ

1. **Phương Pháp Chia Để Trị**: Cả đệ quy và quy hoạch động đều sử dụng phương pháp chia để trị, tức là chia bài toán lớn thành các bài toán con nhỏ hơn.
2. **Lời Giải Dựa Trên Bài Toán Con**: Cả hai kỹ thuật đều giải quyết bài toán lớn dựa trên việc giải quyết các bài toán con.

### Sự Khác Biệt

1. **Lưu Trữ Kết Quả Bài Toán Con**:
   - **Đệ Quy**: Thông thường không lưu trữ kết quả của các bài toán con. Điều này có thể dẫn đến việc tính toán lại nhiều lần cùng một bài toán con, gây tốn thời gian.
   - **Quy Hoạch Động**: Lưu trữ kết quả của các bài toán con để tránh việc tính toán lại. Có hai cách lưu trữ:
     - **Memoization**: Lưu trữ kết quả của các bài toán con trong quá trình gọi đệ quy.
     - **Tabulation**: Sử dụng một bảng (table) để lưu trữ kết quả của các bài toán con, giải quyết từ các bài toán con nhỏ nhất đến bài toán lớn nhất.

2. **Hiệu Quả Tính Toán**:
   - **Đệ Quy**: Có thể không hiệu quả về mặt thời gian do tính toán lặp lại, đặc biệt là với các bài toán có nhiều trường hợp lặp lại như Fibonacci.
   - **Quy Hoạch Động**: Hiệu quả hơn về thời gian do tránh được tính toán lặp lại bằng cách lưu trữ kết quả các bài toán con.

### Ví Dụ

- **Đệ Quy Tính Fibonacci**:
  ```python
  def fibonacci_recursive(n):
      if n <= 1:
          return n
      return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
  ```

- **Quy Hoạch Động Tính Fibonacci (Memoization)**:
  ```python
  def fibonacci_memoization(n, memo={}):
      if n in memo:
          return memo[n]
      if n <= 1:
          return n
      memo[n] = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
      return memo[n]
  ```

- **Quy Hoạch Động Tính Fibonacci (Tabulation)**:
  ```python
  def fibonacci_tabulation(n):
      if n <= 1:
          return n
      fib = [0] * (n + 1)
      fib[1] = 1
      for i in range(2, n + 1):
          fib[i] = fib[i-1] + fib[i-2]
      return fib[n]
  ```

### Kết Luận

- **Đệ Quy**: Đơn giản, dễ hiểu nhưng có thể kém hiệu quả với các bài toán có tính chất lặp lại nhiều.
- **Quy Hoạch Động**: Tối ưu hóa các bài toán đệ quy bằng cách lưu trữ kết quả các bài toán con, giúp tiết kiệm thời gian tính toán.

Hy vọng giải thích trên giúp anh hiểu rõ hơn về mối quan hệ và sự khác biệt giữa đệ quy và quy hoạch động!