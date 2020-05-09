import numpy as np 
from tkinter import Tk
from tkinter.filedialog import askopenfilename

option = "TXT" #input("Ali želiš text file ali live stream? (TXT/STREAM) ").upper()
readData = False #a berem podatke al ne?


if option=="TXT":
    root = Tk()
    root.withdraw()
    filename = askopenfilename()
    f = open(filename)
    root.destroy()
    
    f = open(filename)
    
    arr = []
    
    row = 0 #da vem katere vrstice spustit
    for line in f:
        line = line.split(", ")
        print(line)
        list_floats = []
        if line[0] == 'Data':
            readData = True #začnem brati ko se začnejo podatki
        #list_floats = [float(x) for x in line]
        if readData:
            for j in range(8):
                print(line[j])
                list_floats.append(float(line[j]))
            tmparr = np.asarray(list_floats, dtype=np.float64)
            arr = np.vstack(tmparr)
        
    print(list_floats)
    print(arr)

            





