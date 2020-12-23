"""
Single particle orbiting around a point
But it ain't fuckin work
"""

import numpy as np
import scipy.linalg as linalg
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

n = np.linspace(0, 2, 100)
y0 = np.array([100, 1,
               1, 100])
G = 0.1
m_1 = 1000
m_2 = 10


def func(t, y):
    r2 = np.array([y[0], y[2]])
    norm = linalg.norm(r2)
    f21 = - G * (m_1 * m_2) * norm / norm ** 3
    return [y[1], f21, y[3], f21]


sol = solve_ivp(lambda t, y: func(t, y), t_span=[n[0], n[-1]], t_eval=n, y0=y0)

print(sol.success)

print(sol)


