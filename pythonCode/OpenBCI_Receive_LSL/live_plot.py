import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

import csv

import bisijao as bci
import numpy as np
from pylsl import StreamInlet, resolve_stream
import scipy.fftpack as sfp
import datetime as dt

### Nastavitve analize signala ###
EMG_meja = 50 # uV
N = 20 # Sample size
toleranca = 0.01 # Med 0 in 1 - določa kakšna odstopanja od EMG_meje spremenijo bool vrednost
i = 0 # iterator za posodabljanje vzorcev v vektorju signal
signal = np.zeros(N) # vektor dolžine N, kamor se shranjujejo vzorci 
flag = False # flag to notify when vector signal is filled with samples
previousBOOL = False # na začetku je roka odprta - RMS signala je pod EMG_mejo

style.use('fivethirtyeight')

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):

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


option = input("Read .txt file or start streaming from OpenBCI-GUI? Type 'txt' or 'stream' >> ")
if option.strip() == "stream":
    print("looking for data stream...")
    stream1 = resolve_stream('name', 'obci_eeg1')
    #stream2 = resolve_stream('name', 'obci_eeg2')
    # create a new inlet to read from the stream
    inlet1 = StreamInlet(stream1[0])
    #inlet2 = StreamInlet(stream2[0])
    # prikažem dolžino vzorčnega vektorja
    #while True:
    # get a new sample (you can also omit the timestamp part if you're not
    # interested in it)
    sample1, timestamp = inlet1.pull_sample()
    #sample2, timestamp = inlet2.pull_sample()
    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=10)
    plt.show()
    print(xs)  # sproti po 1 vzorec
    print(ys)
    #time.sleep(0.5)
elif option.strip() == "txt":
    podatki,knjiznica = bci.importData(option)
    print(podatki)

else:
    raise ValueError('Unknown argument "option" in main.py, line 13') 