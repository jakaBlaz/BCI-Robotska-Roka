import bisijao as bci
import plot
import sendToArduino as roka
import time
### Nastavitve analize signala ###
EMG_meja = 50 # uV
Fs = 200 #Sample rate
# Number of sample points
N = 200*5
# sample spacing
toleranca = 0.01 # Med 0 in 1 - določa kakšna odstopanja od EMG_meje spremenijo bool vrednost
i = 0 # iterator za posodabljanje vzorcev v vektorju signal
#signal = np.zeros(N) # vektor dolžine N, kamor se shranjujejo vzorci 
flag = False # flag to notify when vector signal is filled with samples
previousBOOL = False # na začetku je roka odprta - RMS signala je pod EMG_mejo

#initialize Serial connection
serial = roka.initializeServo()

#Acquire data
matrika = []
N_min = 0
N_max = N
podatki,knjiznica = bci.importData("txt")
size = knjiznica["EXG Channel 0"].size
for i in range(int(size/N)):
    moc = (plot.PowerFromTxt(200,1.0,50.0,35.0,N_min,N_max,knjiznica))
    N_min = N_max
    N_max = N_max + N
    matrika.append(moc)
    if(moc < 5.0):
        roka.sendData("120,120,120,120,120",serial)
        print("relax")
    elif moc<30.0:
        roka.sendData("60,60,60,60,60",serial)
        print("medium")
    else:
        roka.sendData("40,30,30,30,30",serial)
        print("contracted")
    time.sleep(5)