import pytesseract
from pdf2image import convert_from_path
import os
from docx import Document

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Đường dẫn đến Tesseract OCR, nếu cần thiết (nếu đã cài Tesseract đúng cách, dòng này có thể không cần)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print('Running...')
# Đường dẫn file PDF và file xuất kết quả
pdf_path = r'C:\Users\Lenovo\Desktop\PICCOLI PROGETTI\OCR-PDF\1.pdf'
output_txt_path = r'C:\Users\Lenovo\Desktop\PICCOLI PROGETTI\OCR-PDF\result.txt'

# Chuyển đổi PDF thành danh sách các ảnh
pages = convert_from_path(pdf_path, 500)  # Độ phân giải 300 DPI

# Mở file kết quả để ghi
with open(output_txt_path, 'w', encoding='utf-8') as f:
    for i, page in enumerate(pages):
        # OCR trên từng trang và nhận diện chữ tiếng Việt
        print(f'Processing page {i+1}/{len(pages)}')
        text = pytesseract.image_to_string(page, lang='vie')
        
        # Ghi kết quả nhận diện vào file .txt
        f.write(f"Trang {i + 1}:\n")
        f.write(text)
        f.write("\n" + "="*80 + "\n")


print(f"Kết quả OCR đã được xuất ra file: {output_txt_path}")

with open(output_txt_path, 'r', encoding='utf-8') as file:
    text_content = file.read()
    
doc = Document()
pages = text_content.split('================================================================================')
for page in pages:
    doc.add_paragraph(page.strip())
    doc.add_page_break()
    
doc.save(r'C:\Users\Lenovo\Desktop\PICCOLI PROGETTI\OCR-PDF\result.docx')