#to je glavna skripta
import bisijao as bci
import numpy as np
import matplotlib.pyplot as plt


filepath = "D:\Personal\Programiranje\Ledinska_roka\data\OpenBCISession_2020-01-21_17-04-57\OpenBCI-RAW-2020-01-21_17-12-11.txt"
file = open(filepath,"r")
while True:
    continue

# Uvoz podatkov

option = input("Read .txt file or start stream? Type 'txt' or 'stream' >> ")
nepopkolan = bci.start(option)
data = bci.popcol(nepopkolan, 8)
print(data)

#file_object  = open("c:\Users\Nal\RobotskaRoka\BCI-Robotska-Roka\data\OpenBCISession_2020-01-21_17-04-57\OpenBCI-RAW-2020-01-21_17-12-11.txt", "r")


arr0 = np.array([[0,1,2,3,4,5]])
arr1 = np.array([[5.77,4.55,5.74,5.02,2.32,110.30]]) 

# x axis values 
x = (arr0)
# corresponding y axis values 
y = (arr1)
  
plt.figure()
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('x - čas') 
# naming the y axis 
plt.ylabel('y - podatki') 
  
# giving a title to my graph 
plt.title('Graf podatkov vlomljeno s časom!') 
  
# function to show the plot 
plt.show() 


# bla

'''
fajl = open(pot + "/OpenBCI-RAW-2020-01-21_17-12-11.txt")
a = np.array()
for line in fajl:
    a.append(line)
a = np.array([1, 2, 3])
print(a)
'''
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
'''