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
    altfile = '../a-very-light-test.txt'
    print(option)
    temp = option.split(".",1)

    if temp[1]=='txt':
        print('Reading data...')
        root = Tk()
        root.withdraw()
        filename = option
        f = open(filename)
        root.destroy()
        data = np.genfromtxt(filename, delimiter=",", skip_header=6) #prvih 6 vrstic so metapodatki
    elif temp[1] == 'stream':
        print('Starting stream...')
        data = None
    else:
        print('Alternative...')
        filename = altfile
        f = open(filename)

        #generira numpy array
        data = np.genfromtxt(filename, delimiter=",", skip_header=6) #prvih 6 vrstic so metapodatki
        
    f.close()
    return data


