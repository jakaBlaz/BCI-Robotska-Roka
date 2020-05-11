#to je glavna skripta
import numpy as np

#file_object  = open("c:\Users\Nal\RobotskaRoka\BCI-Robotska-Roka\data\OpenBCISession_2020-01-21_17-04-57\OpenBCI-RAW-2020-01-21_17-12-11.txt", "r")






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
