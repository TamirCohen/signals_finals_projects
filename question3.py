import numpy as np
import matplotlib.pyplot as plt
from main import sample_signal



# section (a)

# this func pads the signal and sets its bandpass
def padded_signal(N, n):
    x1 = np.ones((N,), dtype=int)
    return np.pad(x1, (n, n), 'constant', constant_values=(0, 0))

# Problem to debate about - section (a) calls for an infinitely padded discrete signal which i'm not sure python
# can do, just want to make sure if just padding it to a large number is good enough

# Also - unsure on how to find a proportional sin(ax)/sin(bx)


# parameters
n = 50000
N = 5
inf_x1 = padded_signal(N, n)

# t is a variable for our sin function
# x_compare is our proportional sin over sin function
t = np.linspace(0, n, 2 * n+N)
x_compare = np.sin(20 * t)/np.sin(t / 10)

# x_compare is divided by its amplitude - n
# if block used for testing and to catch potential errors
if t.shape == inf_x1.shape:
    compare = inf_x1 - (x_compare/n)
else:
    print("Wrong parameters set for t - readjust, t.shape is = ", t.shape, "inf_x1.shape is = ", inf_x1.shape)
    compare = 0

# x_compare plot - used for testing
plt.plot(x_compare)
plt.show()
plt.close()


print(t.shape)
print(inf_x1.shape)
dtft = np.fft.fft(inf_x1)


plt.plot(dtft)
plt.show()
plt.close()

plt.plot(compare)
plt.show()
plt.close()

# I think this section is pretty much done however - we might need to go in depth into the reasoning behind our
# proportional sin over sin function, which I found mostly by testing


# section (b)

# Something to make sure - the periodic expansion of x[n] is a constant 1 \ infinite rectangle?


x2 = np.ones((10000,), dtype=int)
