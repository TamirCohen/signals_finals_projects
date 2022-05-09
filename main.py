import numpy as np
import matplotlib.pyplot as plt

#test comment
def sample_signal(sampling_interval, sampling_time):
    sampling_times = np.arange(sampling_time, step=sampling_interval)[:, np.newaxis]
    k = np.arange(-4,5).transpose()[np.newaxis, :]
    ak = (5 + k)
    signal = np.sum(ak * np.exp(2j*np.pi*k * sampling_times), axis=1)
    dtft = np.fft.fft(signal) 
    plt.stem(signal.imag)
    plt.show()
    plt.stem(signal.real)
    plt.show()
    plt.stem(dtft)
    plt.show()
if __name__ == "__main__":
    sample_signal(1/8, 1)