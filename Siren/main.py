import numpy as np
import simpleaudio as sa

# Hàm tạo âm thanh sin
def generate_sine_wave(frequency, duration, sample_rate=44100, amplitude=0.5):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    audio = amplitude * np.sin(2 * np.pi * frequency * t)
    return audio

# Hàm tạo âm thanh còi báo động mượt
def create_siren_sound():
    sample_rate = 44100  #  Tần số mẫu (Hz)
    duration = 2  # Thời lượng của âm thanh (giây)
    
    # Các tần số âm thanh (Hz)
    def make(n):
        return [x for x in range(n, n + 51,5)]
    def maken(n):
        return [x for x in range(n, n - 51, -5)]
    
    frequencies = maken(800) + make(755)
    print(frequencies)
    # Số lượng mẫu cho mỗi tần số
    samples_per_freq = int(sample_rate * duration / len(frequencies))
    
    # Tạo mảng tần số nội suy mượt
    interpolated_frequencies = np.interp(
        np.linspace(0, len(frequencies) - 1, len(frequencies) * samples_per_freq),
        np.arange(len(frequencies)),
        frequencies
    )
    
    # Giới hạn tần số trong khoảng 300-800 Hz sau khi nội suy
    interpolated_frequencies = np.clip(interpolated_frequencies, 300, 800)
    # interpolated_frequencies = np.concatenate((interpolated_frequencies,interpolated_frequencies,interpolated_frequencies))
    # Tạo âm thanh sin mượt
    t = np.linspace(0, duration, len(interpolated_frequencies), endpoint=False)
    audio_data = 0.5 * np.sin(2 * np.pi * interpolated_frequencies * t)
    
    # Chuẩn bị dữ liệu âm thanh để phát
    audio_data = (audio_data * 32767).astype(np.int16)  # Chuyển đổi thành 16-bit PCM
    
    return audio_data, sample_rate

# Tạo và phát âm thanh còi báo động
audio_data, sample_rate = create_siren_sound()
play_obj = sa.play_buffer(audio_data, 1, 2, sample_rate)
play_obj.wait_done()  # Đợi cho đến khi âm thanh phát xong
