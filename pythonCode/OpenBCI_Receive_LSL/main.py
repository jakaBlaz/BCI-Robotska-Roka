#to je glavna skripta
import bisijao as bci
import numpy as np
import matplotlib.pyplot as plt
from pylsl import StreamInlet, resolve_stream
import time
plt.close('all')

#print(plt.style.available)
##plt.style.use('/Users/iripuga/Documents/1.Delo/404/_bci_/BCI-Robotska-Roka/pythonCode/stylelib/bci-style.mplstyle')

# Uvoz podatkov
altfile = 'a-very-light-test.txt'
option = input("Read .txt file or start stream? Type 'txt' or 'stream' >> ")

print(option)

if option == 'txt':
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
    """Example program to show how to read a multi-channel time series from LSL."""

    # first resolve an EEG stream on the lab network
    print("looking for data stream...")
    stream1 = resolve_stream('name', 'obci_eeg1')
    #stream2 = resolve_stream('name', 'obci_eeg2')
    
    # create a new inlet to read from the stream
    inlet1 = StreamInlet(stream1[0])
    #inlet2 = StreamInlet(stream2[0])
    i = 0
    data = []
    while True:
        # get a new sample (you can also omit the timestamp part if you're not
        # interested in it)
        sample1, timestamp = inlet1.pull_sample()
        
        #sample2, timestamp = inlet2.pull_sample()
        if i < 10:
            data.append(sample1)
            i = i+1
        else:
            i = 0;
            print("standardna deviacija na desetih vzorcih")
            print(np.std(data))
            print(data)
            data = []
            time.sleep(2)

else:
    raise ValueError('Unknown argument "option" in main.py, line 13')