import numpy as np 
import matplotlib as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename

option = input("Read .txt file or start stream? Type 'txt' or 'stream' >> ")
altfile = '/Users/iripuga/Documents/1.Delo/404/_bci_/BCI-Robotska-Roka/data/a-very-light-test.txt'
'''
a = np.loadtxt(altfile)
print(a)
print(type(a))
'''

if option=='txt':
    print('Reading data...')
    root = Tk()
    root.withdraw()
    filename = askopenfilename()
    f = open(filename)
    root.destroy()

    data = np.genfromtxt(filename, delimiter=",", skip_header=6) #prvih 6 vrstic so metapodatki
    print(data)
elif option == 'stream':
    print('Starting stream...')
else:
    print('Alternative...')
    filename = altfile
    f = open(filename)

    test = np.genfromtxt(filename, delimiter=",", skip_header=6) #prvih 6 vrstic so metapodatki
    print(type(test))

f.close()