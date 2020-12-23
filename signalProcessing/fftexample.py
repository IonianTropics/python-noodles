"""
TODO: implement scipy.fft filtering instead of this ass backwards mess***
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from scipy.fft import rfft, rfftfreq, irfft

SAMPLE_RATE = 44100
DURATION = 5


def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    freqencies = x * freq
    y = np.sin(2 * np.pi * freqencies)
    return x, y


x, y = generate_sine_wave(2, SAMPLE_RATE, DURATION)

_, nice_tone = generate_sine_wave(400, SAMPLE_RATE, DURATION)
_, noise_tone = generate_sine_wave(4000, SAMPLE_RATE, DURATION)
noise_tone *= 0.3

mixed_tone = nice_tone + noise_tone

normalized_tone = np.int16((mixed_tone / mixed_tone.max()) * 32767)  # int16 has a range of -32767 to 32767

N = SAMPLE_RATE * DURATION

xf = rfftfreq(N, 1 / SAMPLE_RATE)
yf = rfft(normalized_tone)

# # len(xf) = (SAMPLE_RATE / 4) * 10 + 1
# points_per_freq = len(xf) / (SAMPLE_RATE / 2)
# target_idx = int(points_per_freq * 4000)
#
# yf[target_idx] = 0
#
# new_sig = irfft(yf)

fig, ax = plt.subplots(nrows=1, ncols=1)
fig.patch.set_facecolor('#575267')
ax.set_facecolor('#222035')
plt.plot(xf, np.abs(yf), '#25dc58')
plt.show()
