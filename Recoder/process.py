

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft, fftfreq

# Đọc file ghi âm
filename = r'C:\Users\Lenovo\Desktop\PICCOLI PROGETTI\Recoder\Results\a.wav'
sample_rate, data = wavfile.read(filename)

# Kiểm tra dữ liệu âm thanh có nhiều kênh hay không
if data.ndim > 1:
    data = data.mean(axis=1)  # Chuyển đổi thành mono nếu cần

# Thời gian của mẫu
times = np.arange(len(data)) / float(sample_rate)

# Biểu diễn đồ thị biên độ theo thời gian
plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 1)
plt.plot(times, data)
plt.title("Amplitude over Time")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

# Biểu diễn đồ thị phổ tần số
N = len(data)
yf = fft(data)
xf = fftfreq(N, 1 / sample_rate)

plt.subplot(3, 1, 2)
plt.plot(xf, np.abs(yf))
plt.title("Frequency Spectrum")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")

# Biểu diễn một số đặc trưng khác của âm thanh
# Đồ thị phổ công suất
plt.subplot(3, 1, 3)
plt.specgram(data, Fs=sample_rate, NFFT=1024, noverlap=512)
plt.title("Spectrogram")
plt.xlabel("Time [s]")
plt.ylabel("Frequency [Hz]")

plt.tight_layout()
plt.show()
