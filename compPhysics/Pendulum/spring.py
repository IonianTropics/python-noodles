"""
Sprong
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

n = np.linspace(0, 10, 200)

m = 1  # spring mass
k = 1  # spring stiffness
r = 1  # rest length of spring
b = 1  # air friction

#  variables
y0 = 1, -1  # x, v


def func(t, y):
    return y[1], -k / m * (y[0] - r) - b / m * y[1]


sol = solve_ivp(lambda t, y: func(t, y), t_span=[n[0], n[-1]], t_eval=n, y0=y0)
print(sol)

plt.plot(sol.t, sol.y[0])
plt.plot(sol.t, sol.y[1])
plt.grid(True)
plt.show()
