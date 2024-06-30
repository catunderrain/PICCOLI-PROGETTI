'''#------------------------------------------------#"""
|                                                      |
|      XXXX        XXX       XXXXXXXXX  X          X   |
|    XX    XX    XX   XX       XX       X X      X X   |
|   XX          XX     XX      XX       X   X  X   X   |
|   XX          XXXXXXXXX      XX       X  _    _  X   |
|    XX    XX   XX     XX      XX        X    _,  X    |
|      XXXX     XX     XX      XX         ===<>===     |
|                                                      |
|              HINZU & MOCHI PRESENTATION              |
'''#------------------------------------------------#"""

import cv2
import os
import time
import imageio

A = time.time()
image_folder = r"C:\Users\Lenovo\Desktop\PICCOLI PROGETTI\Conway's Game of Life\Pics"
video_name = r"C:\Users\Lenovo\Desktop\PICCOLI PROGETTI\Conway's Game of Life\game_of_life.avi"

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
images.sort(key=lambda x: int(x.split('.')[0]))

first_image_path = os.path.join(image_folder, images[0])
frame = cv2.imread(first_image_path)
height, width, layers = frame.shape

scale_factor = 6
height *= scale_factor
width *= scale_factor

fourcc = cv2.VideoWriter_fourcc(*'avc1')
'''
CODEC
avi: avc1, x264, MJPG
mp4: mp4v
'''

video = cv2.VideoWriter(video_name, fourcc, 30, (width, height))  

for i, image in enumerate(images):
    image_path = os.path.join(image_folder, image)
    frame = cv2.imread(image_path)
    frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_NEAREST) 
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    position = (20, 50)
    font_scale = 1
    font_color = (0, 255, 0)
    line_type = 3
    cv2.putText(frame, f'{i}', position, font, font_scale, font_color, line_type)
    
    video.write(frame)

video.release()

print("Video đã được tạo thành công.")
B = time.time()
print(B-A)


def playvid():
    video_path = r"C:\Users\Lenovo\Desktop\PICCOLI PROGETTI\Conway's Game of Life\game_of_life.mp4"
    video_reader = imageio.get_reader(video_path)

    for frame in video_reader:
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        cv2.imshow('Video', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()