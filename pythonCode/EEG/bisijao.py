import numpy as np 
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import csv

import scipy.fftpack as sfp
from scipy.fft import fft
import scipy.signal as signal
from scipy.integrate import simps

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

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

def find_band(iFreq, iPxx, FrequencyBand='alpha'):
    '''
    Returns only EEG band which you are interested in.\n
    In: 
        iFreq: periodogram x-axis
        iPxx: periodogram y-axis
        FrequencyBand: string to choose which EEG frequency band you want to get from signal, 
              options are 'alpha', 'beta', 'gamma', 'delta' or 'theta'
    Out: 
        oFreq: periodogram x-axis for chosen frequency band, only positive frequency
        oPx: periodogram y-axis, only positive frequency
    '''
    l = int(np.floor(len(iFreq) / 2)) # vzamem samo pozitivne frekvence
    freq = iFreq[0:l]
    Px = iPxx[0:l]
    fmax = freq[-1]

    # določim lo in hi - spodnjo in zgornji frekvenčno mejo izbranega pasu
    if FrequencyBand == 'delta':
        lowcut = 0.5
        highcut = 4.0
    elif FrequencyBand == 'theta':
        lowcut = 4.1
        highcut = 8.0
    elif FrequencyBand == 'alpha':
        lowcut = 8.1
        highcut = 13.0
    elif FrequencyBand == 'beta':
        lowcut = 13.1
        highcut = 32.0
    elif FrequencyBand == 'gamma':
        lowcut = 32.1
        highcut = fmax
    else:
        raise ValueError("This frequency band doesn't exist. Choose between 'delta', 'theta', 'alpha', 'beta' or 'gamma'.")    

    # poiščem dejansko vrednost lowcut in highcut v seznamu frekvenc 'freq'
    #flowcut = find_nearest(freq, lowcut) 
    #fhighcut = find_nearest(freq, highcut)

    # najdem na katerih indeksih se nahajata frekvenčni meji
    idx1, = np.where(np.isclose(freq, lowcut))[0] # floating-point search by epsilon
    idx2, = np.where(np.isclose(freq, highcut))[0]
    
    # Izrežem frekvenčni pas
    oFreq = freq[idx1:idx2]
    oPx = Px[idx1:idx2]

    return oFreq, oPx

def averageP(f, Px, fs):
    '''
    Calculate average band power by Simps method.\n
    In:
        f...band frequency array
        Px...periodogram values
        fs...sampling frequency used with fft and periodogram
    Out:
        oP...absolute power of frequency band
    '''
    fres = fs / np.floor(len(f)) # izračunam frekvenčno resolucijo periodograma
    oP = simps(Px, dx=fres) # izračunam površino pod periodogramom po simpsovi formuli

    return oP

def relativeP(band_f, band_Px, full_Pxx, fs):
    '''
    Calculate relative band power according to total power.
    In:
        band_f...chosen frequency band
        band_Px...real part of bands periodogram
        full_Pxx...the whole thing
        fs...sampling frequency 
    Out:
        relP...relative power for band_f (0.0 - 1.0), normalized
    '''
    N = np.floor(len(full_Pxx))

    # total power
    Px = full_Pxx[0:int(N / 2)] # real part of whole periodogram
    fres = fs / N
    total_power = simps(Px, dx=fres)

    # band power
    band_power = averageP(band_f, band_Px, fs)

    # relative power
    relP = band_power / total_power

    return relP
