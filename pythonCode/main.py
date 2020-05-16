#to je glavna skripta
import bisijao as bci
import numpy as np
import matplotlib.pyplot as plt

# Uvoz podatkov
altfile = 'a-very-light-test.txt'
option = altfile #input("Read .txt file or start stream? Type 'txt' or 'stream' >> ")
nepopkolan = bci.start(option) #uvozi offline podatke ali pa začne stream
data = np.array(bci.popcol(nepopkolan, 8)) #rešimo se stolpca z datumom - data je že numpy array
data = data[0, :, :] #3D matriko damo v 2D
print(data.shape)

x = data[:, 0]
print(x)

y = data[:, 1] # [vrstica, stolpec]
print(y)

#plt.figure()
plt.plot(x, y)
plt.show()