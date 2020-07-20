import bisijao as bci
import plot
import sendToArduino as roka
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

#Acquire data
moc = []
N_min = 0
N_max = N
podatki,knjiznica = bci.importData("txt")

for i in range(int(576178/N)):
    moc.append(plot.PowerFromTxt(200,1.0,50.0,35.0,N_min,N_max,knjiznica))
    N_min = N_max
    N_max = N_max + N

for x in moc:
    print(x)
exit()
#send data
serial = roka.initializeServo()
vrnjeno, uspesno = roka.sendData("125",serial)
print(uspesno)
serial.close()