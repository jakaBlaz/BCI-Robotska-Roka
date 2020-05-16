#to je glavna skripta
import bisijao as bci
import numpy as np
import matplotlib.pyplot as plt

# Uvoz podatkov
option = input("Read .txt file or start stream? Type 'txt' or 'stream' >> ")
nepopkolan = bci.start(option) #uvozi offline podatke ali pa začne stream
data = bci.popcol(nepopkolan, 8) #rešimo se stolpca z datumom - data je že numpy array
print(data)
