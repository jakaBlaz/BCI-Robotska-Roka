<<<<<<< HEAD
#to je glavna skripta
import numpy as np


filepath = "D:\Personal\Programiranje\Ledinska_roka\data\OpenBCISession_2020-01-21_17-04-57\OpenBCI-RAW-2020-01-21_17-12-11.txt"
file = open(filepath,"r")
while True:
    continue
=======
import bisijao as bci

# Uvoz podatkov
option = input("Read .txt file or start stream? Type 'txt' or 'stream' >> ")
data = bci.start(option)
>>>>>>> 3330012fd145356a2e35a8171285be1faa24039a
