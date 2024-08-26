import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Đường dẫn đến thư mục chứa ảnh và file xuất kết quả
image_dir = r'C:\Users\Lenovo\Desktop\PICCOLI PROGETTI\OCR-PDF\images'
output_txt_path = r'C:\Users\Lenovo\Desktop\PICCOLI PROGETTI\OCR-PDF\result.txt'

# Mở file kết quả để ghi
with open(output_txt_path, 'w', encoding='utf-8') as f:
    for image_file in sorted(os.listdir(image_dir)):
        image_path = os.path.join(image_dir, image_file)
        
        # OCR trên từng trang và nhận diện chữ tiếng Việt
        print(f'Processing {image_file}...')
        text = pytesseract.image_to_string(image_path, lang='vie')
        
        # Ghi kết quả nhận diện vào file .txt
        f.write(f"{image_file}:\n")
        f.write(text)
        f.write("\n" + "="*80 + "\n")

print(f"Kết quả OCR đã được xuất ra file: {output_txt_path}")
