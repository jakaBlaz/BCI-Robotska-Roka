#to je glavna skripta
import numpy as np


filepath = "D:\Personal\Programiranje\Ledinska_roka\data\OpenBCISession_2020-01-21_17-04-57\OpenBCI-RAW-2020-01-21_17-12-11.txt"
file = open(filepath,"r")
vrstice = file.readlines()
zeljeniInfo = vrstice[-1].split(",")
print(zeljeniInfo[2])