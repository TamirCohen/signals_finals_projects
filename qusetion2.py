import numpy as np
import matplotlib.pyplot as plt
import itertools

SAMPLING_TIME = 100
SMALL_INTERVAL = 0.1
CONTINOUS_TIME_LIMIT = 100

def plot_sample_signal(signal, sampling_interval, sampling_time, axis):
    sampling_times = np.arange(sampling_time, step=sampling_interval)
    continues_times = np.arange(sampling_time, step=SMALL_INTERVAL)
    axis.stem(sampling_times, signal(sampling_times), "o")
    axis.plot(continues_times, signal(continues_times))
    axis.set_title("Sampled signal".format(sampling_interval))
    return sampling_times, signal(sampling_times)

def plot_ffts(sampling_interval, signals, axis):
    signal_fft = np.fft.fft(signals)
    freq = np.fft.fftfreq(n=signals.size, d=sampling_interval)

    #Sorting the freq and the fft samples for the plot to look normal
    freq, signal_fft = zip(*sorted(zip(freq, signal_fft)))
    axis.plot(freq, np.absolute(signal_fft))
    axis.set_title("Fourier Transform")

def plot_reconstructed_signal(signal, sampling_interval, axis, signal_function):
    continues_times = np.arange(CONTINOUS_TIME_LIMIT, step=SMALL_INTERVAL)
    transposed_continues_times = np.arange(CONTINOUS_TIME_LIMIT, step=SMALL_INTERVAL).transpose()[np.newaxis, :]
    n = np.arange(len(signal))[:, np.newaxis]
    signal = signal[:, np.newaxis]
    reconstructed_signal = np.transpose(np.sum(signal * np.sinc((transposed_continues_times - n * sampling_interval) / sampling_interval), axis=0))
    axis.plot(continues_times, reconstructed_signal, label="reconstructed")
    axis.plot(continues_times, signal_function(continues_times), label="original")
    axis.legend()
    axis.set_title("reconstructed signal")

def main():
    signals  = [(lambda t: np.sinc(t/6), "sinc(t/6)"), (lambda t: np.power(np.sinc(t/12), 2), "sinc(t/12)^2"), (lambda t: np.cos(np.pi * t / 12), "cos(pi*t/12)")]
    sampling_intervals = [4, 8]
    for (signal, name), sampling_interval in itertools.product(signals, sampling_intervals):
        fig, axis = plt.subplots(2, 2, figsize=(10,10))
        _, sampled_signal = plot_sample_signal(signal, sampling_interval, SAMPLING_TIME, axis[0,0])
        plot_ffts(sampling_interval, sampled_signal, axis[1,0])
        plot_reconstructed_signal(sampled_signal, sampling_interval, axis[0, 1], signal)
        fig.suptitle(f'{name} Sampling: {sampling_interval}')
        fig.tight_layout()
        fig.show()

if __name__ == "__main__":
    main()