#to je glavna skripta
import bisijao as bci
import numpy as np
import matplotlib.pyplot as plt 


option = input("Read .txt file or start stream? Type 'txt' or 'stream' >> ")
nepopkolan = bci.start(option)
data = bci.popcol(nepopkolan, 8)
print(data)

#file_object  = open("c:\Users\Nal\RobotskaRoka\BCI-Robotska-Roka\data\OpenBCISession_2020-01-21_17-04-57\OpenBCI-RAW-2020-01-21_17-12-11.txt", "r")



# x axis values 
x = [1,2,3] 
# corresponding y axis values 
y = [2,4,1] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show() 




'''
fajl = open(pot + "/OpenBCI-RAW-2020-01-21_17-12-11.txt")
a = np.array()
for line in fajl:
    a.append(line)
a = np.array([1, 2, 3])
print(a)
'''

#parsanje in čuda
pot = r"c:\Users\Nal\RobotskaRoka\BCI-Robotska-Roka\data\OpenBCISession_2020-01-21_17-04-57"
ime =  "/OpenBCI-RAW-2020-01-21_17-12-11.txt"
celapot = pot + ime

fajl = open(celapot, 'r')
print(celapot, 'OPENED\n')

#Shranim posamezne vrstice
lines = np.array([])
for line in fajl:
    lines = np.append(lines, line)

print(lines[6])
prva_vrstica = lines[6].split(',')

print(prva_vrstica)
print(prva_vrstica.pop(8))
print(prva_vrstica)
print(int(lines[6].split(',')[0]))
