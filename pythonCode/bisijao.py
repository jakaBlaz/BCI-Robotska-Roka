import bisijao as bci
import numpy as np 
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def popcol(my_array,pc):
    """ column popping in numpy arrays
    Input: my_array: NumPy array, pc: column index to pop out
    Output: [new_array,popped_col] """
    i = pc
    pop = my_array[:,i]
    new_array = np.hstack((my_array[:,:i],my_array[:,i+1:]))
    return [new_array]

def start(option):
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

    f.close()
    return data