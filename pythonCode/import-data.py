import numpy as np 
from tkinter import Tk
from tkinter.filedialog import askopenfilename

option = input("Read .txt file or start stream? Type 'txt' or 'stream' >> ")
altfile = '/Users/iripuga/Documents/1.Delo/404/_bci_/BCI-Robotska-Roka/data/a-very-light-test.txt'

if option=='txt':
    print('Reading data...')
    root = Tk()
    root.withdraw()
    filename = askopenfilename()
    f = open(filename)
    root.destroy()
    data = np.genfromtxt(filename, delimiter=",", skip_header=6) #prvih 6 vrstic so metapodatki
elif option == 'stream':
    print('Starting stream...')
    data = None
else:
    print('Alternative...')
    filename = altfile
    f = open(filename)

    data = np.genfromtxt(filename, delimiter=",", skip_header=6) #prvih 6 vrstic so metapodatki

print('...data imported!')
f.close()