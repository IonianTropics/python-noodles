
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-1, 1, 1000)
t2 = np.linspace(2 * t[0], 2 * t[-1], 2*len(t)-1)
t3 = np.linspace(4 * t[0], 4 * t[-1], 2*len(t2)-1)

r = np.heaviside(t + 0.5, 1) - np.heaviside(t - 0.5, 1)

f = np.convolve(r, r) * (t[1] - t[0])

f2 = np.convolve(f, f) * (t2[1] - t2[0])

plt.plot(t, r)
plt.plot(t2, f)
plt.plot(t3, f2)
plt.show()

