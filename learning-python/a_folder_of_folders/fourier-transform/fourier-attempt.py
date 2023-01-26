# % actual fourier transform:
# g^(t) = int(t2,t1) ( g(t) * e^-2pi*i*freq*time ) dt
# numpy.trapz(y, x=None, dx=1.0, axis=- 1)

# generate signal
# transform signal
# plot

import numpy as np
from matplotlib import pyplot as plt
import scipy

# Frequency Step and Time
Fs = 10000000
t = np.linspace(0, 1, Fs , False)

# Sets up a figure with 4 subplots of varying sizes
COLUMNS = 2
ROWS = 5
plt.figure(figsize=(COLUMNS*6,ROWS*4))
ax1 = plt.subplot2grid((ROWS, COLUMNS), (0, 0), colspan=1)
ax2 = plt.subplot2grid((ROWS, COLUMNS), (0, 1), colspan=1)
ax3 = plt.subplot2grid((ROWS, COLUMNS), (1, 0), colspan=2, rowspan=2)
ax4 = plt.subplot2grid((ROWS, COLUMNS), (3, 0), colspan=2, rowspan=2)

# Function that generates a signal of frequency "freq" which is passed in as an argument
def gen_sig(freq):
    sig = np.sin(2*np.pi*freq*t)
    return sig

# Procedures that sets labels for ax1, ax2 and ax3
def set_labels(ax):
    ax.set_xlabel("Time")
    ax.set_ylabel("Intensity")

# calls the functions to create two signals
sig1 = gen_sig(10)
sig2 = gen_sig(20)

plt.suptitle("Fourier Transformation")

# plots the 10Hz sine plot
set_labels(ax1)
ax1.set_title("10Hz")
ax1.plot(t,sig1)

# plots the 20Hz sine plot
set_labels(ax2)
ax2.set_title("20Hz")
ax2.plot(sig2)

# creates and plots the combined plot
combined_sig = sig1 + sig2
set_labels(ax3)
ax3.set_title("Combined Signal")
ax3.plot(t,combined_sig)

# attempt to implement my own fourier transform however nope
# ft = np.trapz(combined_sig)
# #print(ft)
# ft = ft * (np.e ** -2j*np.pi*t*Fs)
# print(np.e ** -2j*np.pi*t*Fs)
#print(ft)

# transforms the combined signal
# plots relevant area 
ft = np.fft.fft(combined_sig)
plt.xlim(0,50)
ax4.set_title("Fourier Transformed Signal")
ax4.plot(-ft)

# Reference lines at the anticipated peaks
ax4.axvline(10,color="r",linestyle="--",alpha=0.5)
ax4.axvline(20,color="r",linestyle="--",alpha=0.5)

# saves as png and shows
plt.savefig("ft.png",dpi=500)
plt.show()