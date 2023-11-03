import numpy as np
import matplotlib.pyplot as plt

# Hàm biến đổi Fourier rời rạc
def discrete_fourier_transform(signal):
    N = len(signal)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    return np.dot(e, signal)

# Hàm vẽ biểu đồ tín hiệu và biến đổi Fourier
def plot_signal_and_fft(signal, sample_rate):
    # Biến đổi Fourier
    fft = discrete_fourier_transform(signal)

    # Tạo trục thời gian
    time = np.arange(len(signal)) / sample_rate

    # Tạo trục tần số
    freq = np.fft.fftfreq(len(signal), d=1/sample_rate)

    # Vẽ biểu đồ tín hiệu
    plt.subplot(2, 1, 1)
    plt.plot(time, signal)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Input Signal')

    # Vẽ biểu đồ biến đổi Fourier
    plt.subplot(2, 1, 2)
    plt.plot(freq, np.abs(fft))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title('Fourier Transform')

    # Hiển thị biểu đồ
    plt.tight_layout()
    plt.show()

# Hàm chính
def support_signal_processing():
    # Nhập tín hiệu từ người dùng
    signal_str = input("Nhập tín hiệu (các giá trị cách nhau bằng dấu cách): ")
    signal = np.array(signal_str.split(), dtype=float)

    # Nhập tỷ lệ mẫu từ người dùng
    sample_rate = float(input("Nhập tỷ lệ mẫu (số lần mẫu hóa trong 1 giây): "))

    # Vẽ biểu đồ tín hiệu và biến đổi Fourier
    plot_signal_and_fft(signal, sample_rate)

# Chạy chương trình
support_signal_processing()
