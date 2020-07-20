#to je glavna skripta
import bisijao as bci
import numpy as np
import matplotlib.pyplot as plt
from pylsl import StreamInlet, resolve_stream
import scipy.fftpack as sfp
import time

### Nastavitve analize signala ###
EMG_meja = 50 # uV
N = 200 # Sample size
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

"""Read a multi-channel time series from LSL."""

# first resolve an EEG stream on the lab network
print("looking for data stream...")
stream1 = resolve_stream('name', 'obci_eeg1')
#stream2 = resolve_stream('name', 'obci_eeg2')

# create a new inlet to read from the stream
inlet1 = StreamInlet(stream1[0])
#inlet2 = StreamInlet(stream2[0])

# prikažem dolžino vzorčnega vektorja
data = []
i = 0
start = time.time()
while True:
    # get a new sample (you can also omit the timestamp part if you're not
    # interested in it)
    while i<N:
        sample1, timestamp = inlet1.pull_sample()
        data.append(sample1[1])
        i = i+1
    #sample2, timestamp = inlet2.pull_sample()
    i = 0

    print(data)  # sproti po 1 vzorec
    #time.sleep(1)