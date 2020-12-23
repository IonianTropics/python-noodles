
import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

hz = 100

t = np.linspace(-2, 2, 4 * hz)
rect = np.heaviside(t + 0.5, 1) - np.heaviside(t - 0.5, 1)

fx = fftfreq(4 * hz, 1 / hz)
fy = fft(rect)

plt.plot(fx, np.real(fy))
plt.plot(fx, np.imag(fy))
plt.show()
