import numpy as np
import matplotlib.pyplot as plt
from pyparsing import line
import itertools

SAMPLING_TIME = 100
SMALL_INTERVAL = 0.1

def plot_sample_signal(signal, sampling_interval, sampling_time):
    sampling_times = np.arange(-sampling_time/2, sampling_time/2, step=sampling_interval)
    continues_times = np.arange(-sampling_time/2, sampling_time/2, step=SMALL_INTERVAL)
    plt.plot(sampling_times, signal(sampling_times), "o")
    plt.plot(continues_times, signal(continues_times))
    plt.show()
    return sampling_times, signal(sampling_times)

def plot_ffts(times, signals):
    signal_fft = np.fft.fft(signals)
    freq = np.fft.fftfreq(times.shape[-1])

    #Sorting the freq and the fft samples for the plot to look normal
    freq, signal_fft = zip(*sorted(zip(freq, signal_fft)))
    plt.plot(freq, np.absolute(signal_fft))
    plt.show()

def main():
    signals  = [lambda t: np.sinc(t/6), lambda t: np.power(np.sinc(t/12), 2), lambda t: np.cos(np.pi * t / 12)]
    sampling_intervals = [1, 4, 8]
    for signal, sampling_interval in itertools.product(signals, sampling_intervals):
        times, signal = plot_sample_signal(signal, sampling_interval, SAMPLING_TIME)
        plot_ffts(times, signal)
if __name__ == "__main__":
    main()