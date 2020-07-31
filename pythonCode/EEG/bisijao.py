import numpy as np 
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import csv
from __future__ import division

import scipy.fftpack as sfp
from scipy.fft import fft
import scipy.signal as signal

def popcol(my_array,pc):
    """ column popping in numpy arrays
    Input: my_array: NumPy array, pc: column index to pop out
    Output: [new_array,popped_col] """
    i = pc
    pop = my_array[:,i]
    new_array = np.hstack((my_array[:,:i],my_array[:,i+1:]))

    return [new_array]

def importData(option):
    altfile = 'a-very-light-test.txt'

    if option == 'txt':
        print('Reading data...')
        root = Tk()
        root.withdraw()
        filename = askopenfilename()
        f = open(filename)
        root.destroy()
    else:
        print('Alternative...')
        filename = altfile
        f = open(filename)

    #generira numpy array
    data = np.genfromtxt(filename, delimiter=",", skip_header=5) #prvih 6 vrstic so metapodatki
    
    header = csv.DictReader(filter(lambda row: row[0]!='%', f))
    dictionary = {
        "test" : "value"
    }
    for i in range(len(header.fieldnames)):
        dictionary[header.fieldnames[i].strip()] = data[:,i]

    f.close()
    dictionary.pop("test")
    dictionary.pop("Timestamp (Formatted)")
    dictionary.pop("Sample Index")
    return data,dictionary

def analyze_ACCEL(ax, ay, az):
    '''
        Funkcija vrne BOOL glede na postavitev pospeškometra. (Meje so določene 
        eksperimentalno s pospeškometrom pritrjenim na zatilje.)
    '''
    if ax < -0.14 and ay > -0.87 and az < -0.11: 
        return True     # premik glave naprej
    else:
        return False    # glava pokonci

def analyze_EMG(signal, meja, toleranca, previousBOOL):
    '''
        Funkcija izračuna RMS na vhodnem vektorju meritev in vrne BOOL vrednost 
        glede na mejo, ki jo določimo ob klicu funkcije.
        Input:
            signal...vzorec v realnem času, ki ga obravnavamo
            meja...določa odpiranje/zapiranje roke
            toleranca...definira kakšna odstopanja od meje so dopustna
            previousBOOL...prejšnje logično stanje robotske roke, vpliva na novo stanje
        Output:
            BOOL
    '''

    # ROOT MEAN SQUARE   
    rms = np.sqrt(np.mean(signal**2)) #np.sqrt(np.mean(np.square(signal)))

    e = np.std(signal) * toleranca # napaka se določi kot delež std vrednosti
    print("{0:5.2f} uV".format(rms), end="")

    if previousBOOL is True: # roka odprta, torej je bil rms signala prej nad mejo
        if rms < meja - e: 
            return False    # RMS mora zdaj pasti pod nižjo vrednost od meje, če hočemo v drugo logično stanje
        else: 
            return True     # drugače stanje ostane isto
    else:
        if rms > meja + e:
            return True     # zdaj mora biti RMS zrasti nekoliko višje od meje da se zamenja stanje
        else:
            return False

#Filters
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

def notch_filter(data,f0,Q,Fs):
    # f0 = Frequency to be removed from signal (Hz)
    # Q = Quality factor
    w0 = f0/(Fs/2)  # Normalized Frequency
    # Design notch filter
    b, a = signal.iirnotch(w0, Q)
    zi = signal.lfilter_zi(b, a)
    y = signal.filtfilt(b, a, data)
    return y

def bandpass_filter(low,high,transition,fs,s):
    fL = low/fs  # Cutoff frequency as a fraction of the sampling rate (in (0, 0.5)).
    fH = high/fs  # Cutoff frequency as a fraction of the sampling rate (in (0, 0.5)).
    b = transition/fs  # Transition band, as a fraction of the sampling rate (in (0, 0.5)).
    N = int(np.ceil((4 / b)))
    if not N % 2: N += 1  # Make sure that N is odd.
    n = np.arange(N)
    
    # Compute a low-pass filter with cutoff frequency fH.
    hlpf = np.sinc(2 * fH * (n - (N - 1) / 2))
    hlpf *= np.blackman(N)
    hlpf = hlpf / np.sum(hlpf)
    
    # Compute a high-pass filter with cutoff frequency fL.
    hhpf = np.sinc(2 * fL * (n - (N - 1) / 2))
    hhpf *= np.blackman(N)
    hhpf = hhpf / np.sum(hhpf)
    hhpf = -hhpf
    hhpf[(N - 1) // 2] += 1
    
    # Convolve both filters.
    h = np.convolve(hlpf, hhpf)

    #apply filter to signal
    s = np.convolve(s, h)
    return s


def bandreject_filter(low,high,transition,fs,s):
    fL = low/fs  # Cutoff frequency as a fraction of the sampling rate (in (0, 0.5)).
    fH = high/fs  # Cutoff frequency as a fraction of the sampling rate (in (0, 0.5)).
    b = transition/fs  # Transition band, as a fraction of the sampling rate (in (0, 0.5)).
    N = int(np.ceil((4 / b)))
    if not N % 2: N += 1  # Make sure that N is odd.
    n = np.arange(N)
    
    # Compute a low-pass filter with cutoff frequency fL.
    hlpf = np.sinc(2 * fL * (n - (N - 1) / 2))
    hlpf *= np.blackman(N)
    hlpf /= np.sum(hlpf)
    
    # Compute a high-pass filter with cutoff frequency fH.
    hhpf = np.sinc(2 * fH * (n - (N - 1) / 2))
    hhpf *= np.blackman(N)
    hhpf /= np.sum(hhpf)
    hhpf = -hhpf
    hhpf[(N - 1) // 2] += 1
    
    # Add both filters.
    h = hlpf + hhpf

    #apply filter to signal
    s = np.convolve(s, h)

    return s