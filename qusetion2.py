import numpy as np
import matplotlib.pyplot as plt
from pyparsing import line
import itertools

SAMPLING_TIME = 100
SMALL_INTERVAL = 0.1
CONTINOUS_TIME_LIMIT = 100

def plot_sample_signal(signal, sampling_interval, sampling_time, axis):
    sampling_times = np.arange(sampling_time, step=sampling_interval)
    continues_times = np.arange(sampling_time, step=SMALL_INTERVAL)
    axis.plot(sampling_times, signal(sampling_times), "o")
    axis.plot(continues_times, signal(continues_times))
    axis.set_title("Sampled signal".format(sampling_interval))
    return sampling_times, signal(sampling_times)

def plot_ffts(times, signals, axis):
    signal_fft = np.fft.fft(signals)
    freq = np.fft.fftfreq(times.shape[-1])

    #Sorting the freq and the fft samples for the plot to look normal
    freq, signal_fft = zip(*sorted(zip(freq, signal_fft)))
    axis.plot(freq, np.absolute(signal_fft))
    axis.set_title("Fourier Transform")

def plot_reconstructed_signal(signal, sampling_interval, axis):
    continues_times = np.arange(CONTINOUS_TIME_LIMIT, step=SMALL_INTERVAL).transpose()[np.newaxis, :]
    n = np.arange(len(signal))[:, np.newaxis]
    signal = signal[:, np.newaxis]
    reconstructed_signal = np.transpose(np.sum(signal * np.sinc((continues_times - n * sampling_interval) / sampling_interval), axis=0))
    axis.plot(np.squeeze(np.transpose(continues_times), axis=1), reconstructed_signal, label="reconstructed")
    axis.set_title("reconstructed signal")

def main():
    signals  = [(lambda t: np.sinc(t/6), "sinc(t/6)"), (lambda t: np.power(np.sinc(t/12), 2), "sinc(t/12)^2"), (lambda t: np.cos(np.pi * t / 12), "cos(pi*t/12)")]
    sampling_intervals = [4, 8]
    for (signal, name), sampling_interval in itertools.product(signals, sampling_intervals):
        fig, axis = plt.subplots(2, 2)
        times, signal = plot_sample_signal(signal, sampling_interval, SAMPLING_TIME, axis[0,0])
        plot_ffts(times, signal, axis[1,0])
        plot_reconstructed_signal(signal, sampling_interval, axis[0, 1])
        fig.suptitle(f'{name} Sampling: {sampling_interval}')
        fig.tight_layout()
        fig.show()

if __name__ == "__main__":
    main()