"""
Computes pi with monte carlo like stuff
"""

import numpy as np
import matplotlib.pyplot as plt


def lcg(size, seed, mod, multiplier, increment):
    if not 0 < mod:
        raise ValueError("Modulus is less than 0")
    elif not 0 < multiplier < mod:
        raise ValueError("Invalid multiplier")
    elif not 0 <= increment < mod:
        raise ValueError("Invalid increment")
    elif not 0 <= seed < mod:
        raise ValueError("Invalid Seed")

    for i in range(size):
        seed = (multiplier * seed + increment) % mod
        yield seed


def is_inside(a, b):
    return True if np.sqrt(a ** 2 + b ** 2) < 1 else False


if __name__ == '__main__':
    m = 0
    size = 100000
    Xin = []
    Yin = []
    Xout = []
    Yout = []
    for i, u in zip(lcg(size, 2798196071, 2**32, 1103515245, 34567), lcg(size, 1526587307, 2**32, 1103515245, 34567)):
        x = i / 2 ** 32 * 1
        y = u / 2 ** 32 * 1
        if is_inside(x, y):
            m += 1
            Xin.append(x)
            Yin.append(y)
        else:
            Xout.append(x)
            Yout.append(y)

    print(4*m/size)
    plt.scatter(Xin, Yin, s=1, c='r')
    plt.scatter(Xout, Yout, s=1)
    plt.show()
