
import numpy as np
from scipy.fft import fft, fftfreq, ifft
import matplotlib.pyplot as plt

SAMPLE_RATE = 44100
D = 1 / SAMPLE_RATE  # sample spacing
MAX_FREQ = SAMPLE_RATE / 2
DURATION = 5
N = SAMPLE_RATE * DURATION  # window length
t = np.linspace(0, DURATION, N)
tau = 2 * np.pi

SIGNAL = np.cos(0 * tau * t)
NORM = np.int16((SIGNAL / SIGNAL.max()) * ((2 ** 16) / 2 - 1))

x = fftfreq(N, D)
y = fft(NORM)

c = 3.63*10**9

y[0] = 0.0

print(len(x) / MAX_FREQ)
print(x)

# plt.plot(x, np.real(y), 'b')
# plt.plot(x, np.imag(y), 'r')
# plt.show()
