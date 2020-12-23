
import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

DURATION = 5
SAMPLE_RATE = 8000

N = SAMPLE_RATE * DURATION

t = np.linspace(0, DURATION, DURATION * SAMPLE_RATE)
tau = 2 * np.pi

SIGNAL = np.cos(220 * tau * t + np.pi / 2)
NORM = np.int16((SIGNAL / SIGNAL.max()) * 32767)

xf = fftfreq(N, 1 / SAMPLE_RATE)
yf = fft(NORM)

plt.plot(xf, np.real(yf), 'b')
plt.plot(xf, np.imag(yf), 'r')
plt.show()
