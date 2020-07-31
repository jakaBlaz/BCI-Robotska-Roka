import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

import csv

import bisijao as bci
import numpy as np
from pylsl import StreamInlet, resolve_stream
import scipy.fftpack as sfp
from scipy.fft import fft
import scipy.signal as signal
import datetime as dt

#style.use('fivethirtyeight')

# Create figure for plotting
xs = []
ys = []

# This function is called periodically from FuncAnimation
""" def animate(i, xs, ys):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # Add x and y to lists
    sample1, timestamp = inlet1.pull_sample()
    xs.append(timestamp)
    ys.append(sample1[0])

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('EMG over time')
    plt.ylabel('EMG signal') """

# Sample rate and desired cutoff frequencies (in Hz).
Fs = 200
fs = Fs

f0 = 50.0  # Frequency to be removed from signal (Hz)
Q = 35  # Quality factor
w0 = f0/(Fs/2)  # Normalized Frequency
# Design notch filter
b, a = signal.iirnotch(w0, Q)
zi = signal.lfilter_zi(b, a)
#initial bandpass filter
lowcut = 4
highcut = 60

#Import data
podatki,knjiznica = bci.importData("txt")
podatki = knjiznica["EXG Channel 0"]
#print(podatki)
podatki = podatki [8000:16000]

#Initialize plot diagram
#plt.xkcd()
fig, (ax_orig,ax_fft,ax_gamma,ax_beta,ax_alpha,ax_theta) = plt.subplots(6, 1)
N = podatki.size
T = 1.0 / Fs

xn = podatki #lahko bi isto naredil sfp.ifft(y) pa bi bil na istem
y = fft(podatki)
y = fft(signal.filtfilt(b, a, xn))
y = fft(bci.butter_bandpass_filter(sfp.ifft(y), lowcut, highcut, fs, order=6))

x = np.linspace(0.0,100,N//2)
ax_fft.plot(x, 2.0/N * np.abs(y[0:N//2]))
ax_fft.set_title('FFT Signal')
ax_fft.grid()
ax_fft.set_xlim([-2, 60])

x = np.linspace(0.0,N,N)
ax_orig.plot(x,sfp.ifft(y))
ax_orig.set_title('Original Signal')

#Gamma brain waves
lowcut = 32
highcut = 60

#Bandpass filter, da se znebiš motenj pri nizkih in visokih frekvencah
y_gamma = fft(bci.butter_bandpass_filter(sfp.ifft(y), lowcut, highcut, fs, order=6))
x = np.linspace(0.0,100,N//2)
ax_gamma.plot(x , 2.0/N * np.abs(y_gamma[0:N//2]))
ax_gamma.set_title('Gamma brain waves')
ax_gamma.grid()
ax_gamma.set_xlim([-2, 60])

#Beta brain waves
lowcut = 13
highcut = 32

#Notch filter da se znebiš 50Hz motnje (ki jo dobiš iz omrežne frekvence/napetosti/elektrike)
y_beta = fft(bci.butter_bandpass_filter(sfp.ifft(y), lowcut, highcut, fs, order=6))
x = np.linspace(0.0,100,N//2)
ax_beta.plot(x , 2.0/N * np.abs(y_beta[0:N//2]))
ax_beta.set_title('Beta brain waves')
ax_beta.grid()
ax_beta.set_xlim([-2, 60])

#Alpha brain waves
lowcut = 8
highcut = 13

#Notch filter da se znebiš 50Hz motnje (ki jo dobiš iz omrežne frekvence/napetosti/elektrike)
y_alpha = fft(bci.butter_bandpass_filter(sfp.ifft(y), lowcut, highcut, fs, order=6))
x = np.linspace(0.0,100,N//2)
ax_alpha.plot(x , 2.0/N * np.abs(y_alpha[0:N//2]))
ax_alpha.set_title('Alpha brain waves')
ax_alpha.grid()
ax_alpha.set_xlim([-2, 60])


#Theta brain waves
lowcut = 4
highcut = 8

#Notch filter da se znebiš 50Hz motnje (ki jo dobiš iz omrežne frekvence/napetosti/elektrike)
y_theta = fft(bci.butter_bandpass_filter(sfp.ifft(y), lowcut, highcut, fs, order=6))
x = np.linspace(0.0,100,N//2)
ax_theta.plot(x , 2.0/N * np.abs(y_theta[0:N//2]))
ax_theta.set_title('Theta brain waves')
ax_theta.grid()
ax_theta.set_xlim([-2, 60])

y_fft = y
y = sfp.ifft(y) #da iz frekvenčnega prostora prideš nazaj v časovni prostor
f, Pxx = signal.periodogram(y,fs = fs,return_onesided = False)
#print("f = ",f)
#print("Pxx = ",Pxx)
#print(len(f))
#plt.xkcd()
plt.figure(num=2)
#plt.xlim([0, 50])
plt.plot(f,Pxx) #močnostni diagram
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.grid()
plt.show()