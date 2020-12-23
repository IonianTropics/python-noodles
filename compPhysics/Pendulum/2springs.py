"""
mega  sprong
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

n = np.linspace(0, 10, 100)

m1, m2 = 1, 1  # weight mass
w1, w2 = 0.5, 0.5  # weight length
k1, k2 = 1, 1  # spring stiffness
r1, r2 = 1, 1  # rest length
b = 0.1  # air friction

y0 = [1, 0.5,
      2.5, 0]


def func(t, y):
    return [y[1],  - b / m1 * y[1] - (k1 / m1) * (y[0] - r1) + (k2 / m1) * (y[2] - y[0] - w1 - r2),
            y[3],  - b / m2 * y[3] - (k2 / m2) * (y[2] - y[0] - w1 - r2)]


sol = solve_ivp(lambda t, y: func(t, y), t_span=[n[0], n[-1]], t_eval=n, y0=y0)
print(sol.success)

plt.plot(sol.t, sol.y[0])
plt.plot(sol.t, sol.y[2])
plt.grid(True)
plt.show()
