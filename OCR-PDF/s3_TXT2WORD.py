# import language_tool_python
from docx import Document

# Đường dẫn file .txt và file .docx xuất ra
input_txt_path = r'C:\Users\Lenovo\Desktop\PICCOLI PROGETTI\OCR-PDF\result.txt'
output_docx_path = r'C:\Users\Lenovo\Desktop\PICCOLI PROGETTI\OCR-PDF\result.docx'

# Khởi tạo LanguageTool cho tiếng Việt
# tool = language_tool_python.LanguageTool('vi')

# Hàm dự đoán và sửa lỗi ký tự tiếng Việt
# def correct_vietnamese_text(text):
#     matches = tool.check(text)
#     corrected_text = language_tool_python.utils.correct(text, matches)
#     return corrected_text

# Đọc nội dung file .txt và sửa lỗi
with open(input_txt_path, 'r', encoding='utf-8') as file:
    text_content = file.read()

# Sửa lỗi trong nội dung đã nhận diện
corrected_text = text_content

# Chuyển nội dung đã sửa sang file .docx
doc = Document()
pages = corrected_text.split('================================================================================')
for page in pages:
    doc.add_paragraph(page.strip())
    doc.add_page_break()

doc.save(output_docx_path)
print(f'Kết quả đã được lưu vào file: {output_docx_path}')
