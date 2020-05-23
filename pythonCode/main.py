#to je glavna skripta
import bisijao as bci
import numpy as np
import matplotlib.pyplot as plt
import os
plt.close('all')

plt.style.use('/Users/iripuga/Documents/1.Delo/404/_bci_/BCI-Robotska-Roka/pythonCode/stylelib/bci-style.mplstyle')

# Uvoz podatkov
altfile = '../a-very-light-test.txt'
option = altfile #input("Read .txt file or start stream? Type 'txt' or 'stream' >> ")
nepopkolan = bci.start(option) #uvozi offline podatke ali pa začne stream
data = np.array(bci.popcol(nepopkolan, 8)) #rešimo se stolpca z datumom - data je že numpy array
data = data[0, :, :] #3D matriko damo v 2D
print('Velikost numpy podatkovnega polja:', data.shape)

x = data[:, 0] # indeksi vrstic

# podatki
y1 = data[:, 1] # [vrstica, stolpec]
y2 = data[:, 2]
y3 = data[:, 3]
y4 = data[:, 4]
ax = data[:, 5]
ay = data[:, 6]
az = data[:, 7]

plt.figure(1)
plt.subplot(4, 1, 1); plt.plot(x, y1, color='#ff1080')
plt.subplot(4, 1, 2); plt.plot(x, y2)
plt.subplot(4, 1, 3); plt.plot(x, y3)
plt.subplot(4, 1, 4); plt.plot(x, y4)

plt.show(block=False) # ne blokira zapiranja figure
plt.pause(3)  # počakam 3s...
plt.close(fig='all')   # ... in zdaj jo lahko zaprem.

#še en komentar
