#to je glavna skripta
import bisijao as bci
import numpy as np
import matplotlib.pyplot as plt
plt.style.use((r'C:\Users\Nal\RobotskaRoka\BCI-Robotska-Roka\pythonCode\stylelib\bci-style.mplstyle'))



# Uvoz podatkov

altfile = 'a-very-light-test.txt'
option = altfile #input("Read .txt file or start stream? Type 'txt' or 'stream' >> ")
nepopkolan = bci.start(option) #uvozi offline podatke ali pa začne stream
data = np.array(bci.popcol(nepopkolan, 8)) #rešimo se stolpca z datumom - data je že numpy array
data = data[0, :, :] #3D matriko damo v 2D
print(data.shape)








x = data[:, 0] # indeksi vrstic



# podatki
y1 = data[:, 1] # [vrstica, stolpec]
y2 = data[:, 2]
y3 = data[:, 3]
y4 = data[:, 4]
ax = data[:, 5]
ay = data[:, 6]
az = data[:, 7]

plt.rcParams['lines.linewidth'] = 2
plt.rcParams['lines.linestyle'] = '--'


#plt.rcParams['figure.figsize']  = [100.4, 100.8]
plt.rcParams['lines.linewidth'] = 3
plt.rcParams['lines.markersize'] = 29
plt.rcParams['figure.autolayout'] = True
#plt.rcParams['xstick.labelsize'] = 16
#plt.rcParams['ystick.labelsize'] = 16

plt.figure(figsize=(20,15))
plt.subplot(4, 1, 1); plt.plot(x, y1, color = '#ff8000')          #prvi subplot
# naming the x axis 
#plt.xlabel('x - indeksi(N)') 
# naming the y axis 
#plt.ylabel('y - EEG kanal(uV)') 
plt.title('Prvi EEG kanal vlomljeno s časom') 

plt.subplot(4, 1, 2); plt.plot(x, y2, color = 'red')           #drugi subplot
# naming the x axis 
#plt.xlabel('x - indeksi(N)') 
# naming the y axis 
#plt.ylabel('y - EEG kanal(uV)') 
plt.title('Drugi EEG kanal vlomljeno s časom') 


plt.subplot(4, 1, 3); plt.plot(x, y3, color = 'blue')           #tretji subplot
# naming the x axis 
#plt.xlabel('x - indeksi(N)') 
# naming the y axis 
#plt.ylabel('y - EEG kanal(uV)') 
plt.title('Tretji EEG kanal vlomljeno s časom') 

plt.subplot(4, 1, 4); plt.plot(x, y4, color = '#bf00ff')           #četrti subplot
# naming the x axis 
#plt.xlabel('x - indeksi(N)') 
# naming the y axis 
#plt.ylabel('y - EEG kanal(uV)') 
plt.title('Četri EEG kanal vlomljeno s časom') 

plt.show(block=True) # ne blokira zapiranja figure


#plt.pause(100000000)  # počakam 3s...

#plt.close()   # ... in zdaj jo lahko zaprem.

#še en komentar

