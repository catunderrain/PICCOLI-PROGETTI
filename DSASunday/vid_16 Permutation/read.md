### Độ Khó Của Hai Thuật Toán

#### 1. Giải Thuật Đệ Quy Đầu Tiên
Giải thuật này xây dựng hoán vị bằng cách chọn từng phần tử làm phần tử đầu tiên và tạo các hoán vị cho phần còn lại của dãy số. Độ khó của giải thuật này có thể được phân tích như sau:

- **Độ phức tạp thời gian**: \(O(n!)\), nơi \(n\) là số lượng phần tử trong dãy số. Mỗi phần tử có thể xuất hiện ở bất kỳ vị trí nào trong hoán vị, và có tổng cộng \(n!\) cách hoán vị.
- **Độ phức tạp không gian**: \(O(n!)\) để lưu trữ tất cả các hoán vị. Bên cạnh đó, độ sâu của ngăn xếp đệ quy là \(O(n)\) vì cần phải lưu trữ trạng thái cho mỗi cuộc gọi đệ quy.

#### 2. Giải Thuật Đệ Quy Dễ Hiểu Hơn
Giải thuật này sử dụng backtracking để tạo các hoán vị bằng cách hoán đổi phần tử bắt đầu với các phần tử khác và tiếp tục với các phần tử tiếp theo. Độ khó của giải thuật này cũng tương tự:

- **Độ phức tạp thời gian**: \(O(n!)\), giống như giải thuật đầu tiên. Mỗi lần hoán đổi tạo ra một nhánh mới trong cây đệ quy, dẫn đến tổng cộng \(n!\) nhánh.
- **Độ phức tạp không gian**: \(O(n!)\) để lưu trữ tất cả các hoán vị. Độ sâu của ngăn xếp đệ quy cũng là \(O(n)\), tương tự như giải thuật đầu tiên.

### So Sánh

- **Độ phức tạp thời gian**: Cả hai giải thuật đều có độ phức tạp thời gian là \(O(n!)\).
- **Độ phức tạp không gian**: Cả hai giải thuật đều yêu cầu \(O(n!)\) không gian để lưu trữ kết quả và \(O(n)\) không gian cho ngăn xếp đệ quy.
- **Độ dễ hiểu**: Giải thuật thứ hai (backtracking) có thể dễ hiểu hơn vì nó sử dụng một phương pháp trực tiếp hơn để hoán đổi các phần tử, và dễ dàng hơn để hình dung và theo dõi trạng thái của dãy số trong từng bước của quá trình hoán vị.

Nhìn chung, cả hai giải thuật đều có độ phức tạp tương đương nhau về thời gian và không gian, nhưng giải thuật backtracking có thể dễ hiểu và dễ triển khai hơn.

