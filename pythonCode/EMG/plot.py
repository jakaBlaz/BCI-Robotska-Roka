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
def animate(i, xs, ys):
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
    plt.ylabel('EMG signal')

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = signal.butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = signal.lfilter(b, a, data)
    return y

def plotGraphFromTxt(Fs,low,high,Q, N_min,N_max):
    # Sample rate and desired cutoff frequencies (in Hz).
    fs = Fs
    lowcut = low
    highcut = high

    f0 = 50.0  # Frequency to be removed from signal (Hz)
    Q = Q  # Quality factor
    w0 = f0/(Fs/2)  # Normalized Frequency
    # Design notch filter
    b, a = signal.iirnotch(w0, Q)
    zi = signal.lfilter_zi(b, a)
    
    #Import data
    podatki,knjiznica = bci.importData("txt")
    podatki = knjiznica["EXG Channel 0"]
    podatki = podatki [N_min:N_max]
    #print(podatki)

    #Initialize plot diagram
    #plt.xkcd()
    fig, (ax_orig, ax_fft,ax_fft_bandpassFilters,ax_fft_filtfilt) = plt.subplots(4, 1)
    N = podatki.size
    T = 1.0 / Fs
    x = np.linspace(0.0,N,N) #preposto razporedim vse vzorce po času (kar je prb 48 min + 60s + 200Hz = 576000, kar je skor realna številka ki je 576178
    ax_orig.plot(x,podatki)
    ax_orig.set_title('Original Signal')

    y = fft(podatki)
    x = np.linspace(0.0,100,N//2)
    ax_fft.plot(x, 2.0/N * np.abs(y[0:N//2]))
    ax_fft.set_title('FFT Signal (not filtered)')
    ax_fft.grid()
    ax_fft.set_xlim([-5, 60])
    
    xn = podatki #lahko bi isto naredil sfp.ifft(y) pa bi bil na istem

    #Bandpass filter, da se znebiš motenj pri nizkih in visokih frekvencah
    y = fft(butter_bandpass_filter(sfp.ifft(y), lowcut, highcut, fs, order=6))
    x = np.linspace(0.0,100,N//2)
    ax_fft_bandpassFilters.plot(x , 2.0/N * np.abs(y[0:N//2]))
    ax_fft_bandpassFilters.set_title('FFT Signal bandpass filter')
    ax_fft_bandpassFilters.grid()
    ax_fft_bandpassFilters.set_xlim([-5, 60])

    #Notch filter da se znebiš 50Hz motnje (ki jo dobiš iz omrežne frekvence/napetosti/elektrike)
    y = fft(signal.filtfilt(b, a, xn))
    y = fft(butter_bandpass_filter(sfp.ifft(y), lowcut, highcut, fs, order=6))
    x = np.linspace(0.0,100,N//2)
    ax_fft_filtfilt.plot(x , 2.0/N * np.abs(y[0:N//2]))
    ax_fft_filtfilt.set_title('FFT Signal w/ notch and bandpass filter')
    ax_fft_filtfilt.grid()
    ax_fft_filtfilt.set_xlim([-5, 60])

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
    plt.show()
    return y,f,Pxx

def PowerFromTxt(Fs,low,high,Q, N_min,N_max,knjiznica):
        # Sample rate and desired cutoff frequencies (in Hz).
    fs = Fs
    lowcut = low
    highcut = high

    
    f0 = 50.0  # Frequency to be removed from signal (Hz)
    Q = Q  # Quality factor
    w0 = f0/(Fs/2)  # Normalized Frequency
    # Design notch filter
    b, a = signal.iirnotch(w0, Q)
    zi = signal.lfilter_zi(b, a)
    
    #Prepare data
    podatki = knjiznica["EXG Channel 0"]
    #print(podatki.size)
    podatki = podatki [N_min:N_max]
    xn = podatki
    
    #print(podatki)

    #Initialize plot diagram
    #plt.xkcd()
    T = 1.0 / Fs
    #Notch filter da se znebiš 50Hz motnje (ki jo dobiš iz omrežne frekvence/napetosti/elektrike)
    y = fft(signal.filtfilt(b, a, xn))
    y = fft(butter_bandpass_filter(sfp.ifft(y), lowcut, highcut, fs, order=6))

    y = sfp.ifft(y) #da iz frekvenčnega prostora prideš nazaj v časovni prostor
    f, Pxx = signal.periodogram(y,fs = fs,return_onesided = False)

    #Gledanje vsote vrednosti v za nas zanimivem območju
    zanimivo_obmocje = int((f.size/2)*0.2)
    moc = np.sum(Pxx[0:zanimivo_obmocje]) / podatki.size

    return moc