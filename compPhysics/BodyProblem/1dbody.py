"""
This is a 1D mock 1.5 body problem
"""

import sys
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

n = np.linspace(0, 10, 100)
y0 = [90, 1]
m = 100

G = 10


def func(t, y):
    return y[1], - G * m * y[0] / (abs(y[0]) ** 3)


sol = solve_ivp(lambda t, y: func(t, y), t_span=[n[0], n[-1]], t_eval=n, y0=y0)

if sol.success:
    plt.plot(sol.t, sol.y[0])
    plt.grid
    plt.show()
else:
    print("Integration failure")
    sys.exit(-1)
