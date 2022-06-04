import numpy as np
import matplotlib.pyplot as plt

#test comment
def sample_signal(sampling_interval, sampling_time):
    sampling_times = np.arange(sampling_time, step=sampling_interval)[:, np.newaxis]
    k = np.arange(-4,5).transpose()[np.newaxis, :]
    ak = (5 + k)
    signal = np.sum(ak * np.exp(2j*np.pi*k * sampling_times), axis=1)
    freq = np.fft.fftfreq(n=signal.size)
    freq = 2 * np.pi * np.arange(0, signal.size) / signal.size
    dtft = np.fft.fft(signal)
    fig, axis = plt.subplots(2, 2, figsize=(10,10))
    axis[0,1].stem(sampling_times, signal.imag)
    axis[0,1].set_title("imaginary signal")
    axis[0,0].stem(sampling_times, signal.real)
    axis[0,0].set_title("real signal")
    axis[1,1].stem(freq, dtft.real)
    axis[1,1].set_title(f"dtft signal")
    fig.suptitle(f'Signals, Sampling interval {sampling_interval}')
    fig.tight_layout()
    fig.show()

if __name__ == "__main__":
    sample_signal(1/9, 1)
    sample_signal(4/9, 4)