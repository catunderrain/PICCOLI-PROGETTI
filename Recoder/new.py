import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import queue
import threading

# Thiết lập các tham số âm thanh
sample_rate = 44100  # Tần số mẫu (Hz)
channels = 1         # Số kênh (1 cho mono)
block_size = 1024    # Kích thước khối dữ liệu
duration = 10        # Thời gian ghi âm (giây)

# Tạo một hàng đợi để lưu trữ dữ liệu âm thanh
audio_queue = queue.Queue()

# Thiết lập đồ thị
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Biểu đồ biên độ theo thời gian
time_data = np.zeros(block_size)
time_line, = ax1.plot(time_data)
ax1.set_ylim(-1, 1)
ax1.set_xlim(0, block_size)
ax1.set_title("Amplitude over Time")
ax1.set_xlabel("Samples")
ax1.set_ylabel("Amplitude")

# Biểu đồ phổ tần số
freq_data = np.zeros(block_size // 2 + 1)
freq_line, = ax2.plot(freq_data)
ax2.set_xlim(0, sample_rate / 2)
ax2.set_ylim(0, 100)
ax2.set_title("Frequency Spectrum")
ax2.set_xlabel("Frequency [Hz]")
ax2.set_ylabel("Amplitude")

def audio_callback(indata, frames, time, status):
    if status:
        print(status)
    audio_queue.put(indata.copy())

def record_audio():
    with sd.InputStream(samplerate=sample_rate, channels=channels, blocksize=block_size, callback=audio_callback):
        sd.sleep(int(duration * 1000))

def update_plot(frame):
    if not audio_queue.empty():
        data = audio_queue.get()
        time_line.set_ydata(data)
        freq_data = np.abs(np.fft.rfft(data[:, 0]))
        freq_line.set_ydata(freq_data)
    return time_line, freq_line

# Tạo và bắt đầu luồng ghi âm
record_thread = threading.Thread(target=record_audio)
record_thread.start()

# Sử dụng FuncAnimation để cập nhật đồ thị
ani = FuncAnimation(fig, update_plot, interval=50, blit=True)

plt.tight_layout()
plt.show()

# Chờ luồng ghi âm hoàn thành
record_thread.join()
