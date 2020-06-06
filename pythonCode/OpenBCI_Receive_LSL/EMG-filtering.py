# TODO - Stream TimeSeries pošilja surov signal in ga je potrebno filtrirat preden računamo RMS #

#to je glavna skripta
import bisijao as bci
import numpy as np
import matplotlib.pyplot as plt
from pylsl import StreamInlet, resolve_stream
import scipy.fftpack as sfp
import time

### Nastavitve analize signala ###
EMG_meja = 50 # uV
N = 20 # Sample size
toleranca = 0.01 # Med 0 in 1 - določa kakšna odstopanja od EMG_meje spremenijo bool vrednost
i = 0 # iterator za posodabljanje vzorcev v vektorju signal
signal = np.zeros(N) # vektor dolžine N, kamor se shranjujejo vzorci 
flag = False # flag to notify when vector signal is filled with samples
previousBOOL = False # na začetku je roka odprta - RMS signala je pod EMG_mejo
##################################
#print(plt.style.available)
##plt.style.use('/Users/iripuga/Documents/1.Delo/404/_bci_/BCI-Robotska-Roka/pythonCode/stylelib/bci-style.mplstyle')

# Uvoz podatkov
altfile = 'a-very-light-test.txt'
option = 'stream' #input("Read .txt file or start stream? Type 'txt' or 'stream' >> ")

print('option >>>', option)

if option == 'txt':
    """Read a multi-channel time series from file."""
    nepopkolan = bci.importData(option) #uvozi offline podatke
    data = np.array(bci.popcol(nepopkolan, 8)) #rešimo se stolpca z datumom - data je že numpy array
    data = data[0, :, :] #3D matriko damo v 2D
    print('Velikost numpy podatkovnega polja:', data.shape)

    samples = data.shape[0]
    x = np.arange(0, samples, 1)

    print(x.shape)

    # podatki
    y1 = data[:, 1] # [vrstica, stolpec]
    y2 = data[:, 2]
    y3 = data[:, 3]
    y4 = data[:, 4]
    ax = data[:, 5]
    ay = data[:, 6]
    az = data[:, 7]
    print(az[15])

    plt.figure(1)
    plt.subplot(3, 1, 1); plt.plot(x, ax, color='red'); plt.title('X')
    plt.subplot(3, 1, 2); plt.plot(x, ay, color='green'); plt.title('Y')
    plt.subplot(3, 1, 3); plt.plot(x, az, color='blue'); plt.title('Z')
    #plt.subplot(4, 1, 4); plt.plot(x, y4)
    '''''
    axes.xmargin: 0.5
    axes.ymargin: 0.5
    '''
    plt.show(block=True) # ne blokira zapiranja figure
    #plt.pause(3)  # počakam 3s...
    #plt.close()   # ... in zdaj jo lahko zaprem.

    idx = 1
    while idx > 0:
        idx = int(input('Select index: '))
        print(ax[idx])
        command = bci.analyze_data(ax[idx], ay[idx], az[idx])
        print(command)
        print()
elif option == 'stream':
    """Read a multi-channel time series from LSL."""

    # first resolve an EEG stream on the lab network
    print("looking for data stream...")
    stream1 = resolve_stream('name', 'obci_eeg1')
    #stream2 = resolve_stream('name', 'obci_eeg2')
    
    # create a new inlet to read from the stream
    inlet1 = StreamInlet(stream1[0])
    #inlet2 = StreamInlet(stream2[0])

    # prikažem dolžino vzorčnega vektorja
    print("sample size:", len(signal)) 
    time.sleep(3)

    start = time.time()
    while True:
        # get a new sample (you can also omit the timestamp part if you're not
        # interested in it)
        sample1, timestamp = inlet1.pull_sample()
        #sample2, timestamp = inlet2.pull_sample()

        if i < N:   # signal dolžine N
            #tmp = signal[0:-1]
            #signal[1:] = tmp
            signal[i] = sample1[0]  # sproti dodajam po 1 vzorec na 1.mesto
            #print(sample1)
            i = i + 1
            if signal[-1] != 0.0 and not flag: # preverjam, kdaj bo vektor "signal" napolnjen z vzorci
                print('\n################# Sample Ready #################')
                flag = True
                end = time.time()
                print(f"Sample filled in {end - start}s, starting stream...")
                #time.sleep(0.5)
        else:
            i = 0;
            print(f"RMS na {N} vzorcih meja {EMG_meja} uV >>> ", end="")
            currentBOOL = bci.analyze_EMG(signal, EMG_meja, toleranca, previousBOOL)
            previousBOOL = currentBOOL
            print(" ", currentBOOL)
            #time.sleep(1)
else:
    raise ValueError('Unknown argument "option" in main.py, line 13') 