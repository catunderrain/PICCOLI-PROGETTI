Anh yêu, giải thuật Tháp Hà Nội là một bài toán cổ điển trong lý thuyết tính toán và lập trình đệ quy. Mục tiêu của bài toán là di chuyển một chồng đĩa từ cột nguồn sang cột đích với sự trợ giúp của cột trung gian, tuân theo các quy tắc sau:

1. Chỉ một đĩa có thể di chuyển một lần.
2. Mỗi đĩa chỉ có thể đặt lên trên một đĩa lớn hơn hoặc một cột trống.
3. Đĩa nhỏ hơn phải luôn nằm trên đĩa lớn hơn.

### Nguyên lý giải thuật

Giả sử anh có \( n \) đĩa, và chúng được đánh số từ 1 (nhỏ nhất) đến \( n \) (lớn nhất). Ta có ba cột: Nguồn (Source), Đích (Destination), và Trung gian (Auxiliary).

### Quy tắc đệ quy

1. **Trường hợp cơ sở**: Nếu chỉ có 1 đĩa, di chuyển nó từ cột nguồn sang cột đích trực tiếp.
2. **Trường hợp tổng quát**: Nếu có \( n \) đĩa, di chuyển \( n-1 \) đĩa trên cùng từ cột nguồn sang cột trung gian bằng cách sử dụng cột đích làm trung gian. Sau đó, di chuyển đĩa lớn nhất từ cột nguồn sang cột đích. Cuối cùng, di chuyển \( n-1 \) đĩa từ cột trung gian sang cột đích bằng cách sử dụng cột nguồn làm trung gian.

### Giải thuật chi tiết

1. **Di chuyển \( n-1 \) đĩa từ cột nguồn sang cột trung gian**:
   - Sử dụng đệ quy, coi như \( n-1 \) đĩa là một bài toán con.
   - Lúc này, cột đích sẽ làm trung gian cho việc di chuyển.

2. **Di chuyển đĩa lớn nhất (thứ \( n \)) từ cột nguồn sang cột đích**:
   - Đây là bước di chuyển đơn giản, không cần đệ quy.

3. **Di chuyển \( n-1 \) đĩa từ cột trung gian sang cột đích**:
   - Lại sử dụng đệ quy để coi \( n-1 \) đĩa là một bài toán con.
   - Cột nguồn sẽ làm trung gian cho việc di chuyển.

### Minh họa với 3 đĩa

Giả sử anh có 3 đĩa (1 nhỏ nhất, 3 lớn nhất) trên cột A (Nguồn):

1. Di chuyển 2 đĩa từ A sang B (sử dụng C làm trung gian):
   - Di chuyển đĩa 1 từ A sang C.
   - Di chuyển đĩa 2 từ A sang B.
   - Di chuyển đĩa 1 từ C sang B.

2. Di chuyển đĩa 3 từ A sang C.

3. Di chuyển 2 đĩa từ B sang C (sử dụng A làm trung gian):
   - Di chuyển đĩa 1 từ B sang A.
   - Di chuyển đĩa 2 từ B sang C.
   - Di chuyển đĩa 1 từ A sang C.

### Đoạn mã minh họa

```python
def thap_ha_noi(n, cot_nguon, cot_dich, cot_trung_gian):
    if n == 1:
        print(f"Di chuyển đĩa 1 từ cột {cot_nguon} sang cột {cot_dich}")
        return
    thap_ha_noi(n - 1, cot_nguon, cot_trung_gian, cot_dich)
    print(f"Di chuyển đĩa {n} từ cột {cot_nguon} sang cột {cot_dich}")
    thap_ha_noi(n - 1, cot_trung_gian, cot_dich, cot_nguon)

# Ví dụ sử dụng
so_dia = 3
thap_ha_noi(so_dia, 'A', 'C', 'B')
```

### Tóm tắt

1. Đệ quy chia bài toán lớn thành các bài toán con nhỏ hơn.
2. Di chuyển các đĩa từng bước theo quy tắc đệ quy.
3. Đảm bảo không vi phạm quy tắc đặt đĩa.

Giải thuật Tháp Hà Nội là một ví dụ điển hình về sức mạnh của đệ quy trong lập trình.