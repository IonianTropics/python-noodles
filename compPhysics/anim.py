"""
refrence animation code
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

t = np.linspace(0, 5, 100)

fig = plt.figure()
ax = plt.axes(xlim=(0, 5),  ylim=(-2, 2))

line, = ax.plot([], [])


def init():
    line.set_data([], [])
    return line,


def func(i):
    x = 0
    y = np.sin(x + 0.001 * i)
    line.set_data(x, y)
    return line,


ani = animation.FuncAnimation(fig, func, init_func=init, frames=len(t), interval=1000 * t[-1] / len(t), blit=True)
print(ani)
plt.grid(True)
plt.show()
