from pdf2image import convert_from_path
import os

print('Running...')
# Đường dẫn file PDF và thư mục chứa các ảnh xuất ra
pdf_path = r'C:\Users\Lenovo\Desktop\PICCOLI PROGETTI\OCR-PDF\1.pdf'
output_image_dir = r'C:\Users\Lenovo\Desktop\PICCOLI PROGETTI\OCR-PDF\images'

# Tạo thư mục nếu chưa tồn tại
if not os.path.exists(output_image_dir):
    os.makedirs(output_image_dir)

# Chuyển đổi PDF thành danh sách các ảnh
pages = convert_from_path(pdf_path, 500)  # Độ phân giải 500 DPI

# Lưu từng trang dưới dạng ảnh
for i, page in enumerate(pages):
    image_path = os.path.join(output_image_dir, f'page_{i+1}.png')
    page.save(image_path, 'PNG')
    print(f'Lưu {image_path}')

print('Chuyển đổi PDF thành ảnh hoàn tất.')
