import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
from scipy.io.wavfile import write


class Audio:

    def __init__(self):
        return


def normalize_tone(signal):
    return np.int16((signal / signal.max()) * 2 ** 16 / 2 - 1)


SAMPLE_RATE = 44100
START = 0
END = 10
DELTA = END - START

t = np.linspace(END, START, DELTA*SAMPLE_RATE)

SIGNAL = np.sin(4 * t) + np.sin(440 * t) + np.sin(9000 * t)

AMP = fft(normalize_tone(SIGNAL))
FREQ = fftfreq(DELTA*SAMPLE_RATE, 1 / SAMPLE_RATE)

write("annoying_sound.wav", SAMPLE_RATE, normalize_tone(SIGNAL))

plt.plot(FREQ[:10000], np.abs(AMP)[:10000])
plt.show()
