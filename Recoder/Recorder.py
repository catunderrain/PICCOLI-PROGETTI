import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import time
import threading

freq = 44100
duration = 5

def record():
    print("Recording started...")
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    sd.wait()
    filename = rf"C:\Users\Lenovo\Desktop\PICCOLI PROGETTI\Recoder\Results\{time.time()}.wav"
    write(filename, freq, recording)
    print(f"Recording saved to {filename}")
    wv.write("recording1.wav", recording, freq, sampwidth=2)

def ctime():
    for i in range(duration):
        print(i + 1)
        time.sleep(1)
    print("Countdown finished.")

# Tạo các luồng riêng biệt để thu âm và đếm thời gian
rc = threading.Thread(target=record)
ct = threading.Thread(target=ctime)

# Bắt đầu các luồng
rc.start()
ct.start()

# Chờ các luồng hoàn thành
rc.join()
ct.join()

print("Both threads have finished.")
