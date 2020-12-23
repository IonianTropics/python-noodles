"""
This is a 1D mock two body problem
"""

import sys
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

n = np.linspace(0, 100, 1000)
y0 = [1, -2,
      100, 1]
m_1 = 1000
m_2 = 100
G = 1


def func(t, y):
    return [y[1], (- G * (m_1 * m_2) * (y[0] - y[2]) / (abs(y[0] - y[2]) ** 3)) / m_1,
            y[3], (- G * (m_1 * m_2) * (y[2] - y[0]) / (abs(y[2] - y[0]) ** 3)) / m_2]


sol = solve_ivp(lambda t, y: func(t, y), t_span=[n[0], n[-1]], t_eval=n, y0=y0)
# sol.y[0] = p1, sol.y[1] = v1, sol.y[2] = p2, sol.y[3] = v2

if sol.success:
    plt.plot(sol.t, sol.y[0])
    plt.plot(sol.t, sol.y[2])
    plt.show()
else:
    print("Integration failure")
    sys.exit(-1)
