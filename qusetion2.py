import numpy as np
import matplotlib.pyplot as plt
from main import sample_signal

# small tests nothing substantial, can be ignored
t = np.linspace(-4, 4, 100)
signal_1 = np.sinc(t/6)
signal_2 = np.sinc(t/12)
signal_2 = np.power(signal_2,2)
signal_3 = np.cos(np.pi * t / 12)
