import cv2
import numpy as np
import pygame
from pygame.locals import *
import tkinter as tk
from tkinter import filedialog

# Khởi tạo Pygame
pygame.init()

# Thiết lập kích thước cửa sổ
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Image Processing Interface")

# Khởi tạo tkinter
root = tk.Tk()
root.withdraw()

# Hàm chọn file
def select_image():
    file_path = filedialog.askopenfilename()
    return file_path

# Load ảnh và chuyển sang định dạng phù hợp với Pygame
image_path = select_image()
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = cv2.resize(image, (width, height))
image_surface = pygame.surfarray.make_surface(image.swapaxes(0, 1))

# Các biến điều khiển
contrast = 1.0
brightness = 0
blur = 0
fourier = False

def apply_filters(image, contrast, brightness, blur, fourier):
    # Áp dụng độ tương phản và độ sáng
    new_image = cv2.convertScaleAbs(image, alpha=contrast, beta=brightness)
    
    # Áp dụng làm mờ
    if blur > 0:
        new_image = cv2.GaussianBlur(new_image, (blur, blur), 0)
    
    # Áp dụng Fourier Transform
    if fourier:
        dft = cv2.dft(np.float32(new_image), flags=cv2.DFT_COMPLEX_OUTPUT)
        dft_shift = np.fft.fftshift(dft)
        magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
        new_image = cv2.normalize(magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX)
    
    return new_image

def main():
    global contrast, brightness, blur, fourier, image, image_surface
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_o:
                    image_path = select_image()
                    image = cv2.imread(image_path)
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    image = cv2.resize(image, (width, height))
                    image_surface = pygame.surfarray.make_surface(image.swapaxes(0, 1))

        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            contrast += 0.1
        if keys[K_DOWN]:
            contrast -= 0.1
        if keys[K_LEFT]:
            brightness -= 5
        if keys[K_RIGHT]:
            brightness += 5
        if keys[K_b]:
            blur = (blur + 1) if blur < 10 else 0
        if keys[K_f]:
            fourier = not fourier

        filtered_image = apply_filters(image, contrast, brightness, blur, fourier)
        filtered_surface = pygame.surfarray.make_surface(filtered_image.swapaxes(0, 1))
        
        window.blit(filtered_surface, (0, 0))
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
