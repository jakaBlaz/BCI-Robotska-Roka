#to je glavna skripta
import bisijao as BCI

option = input("Read .txt file or start stream? Type 'txt' or 'stream' >> ")
nepopkolan = BCI.start(option)
data = BCI.popcol(nepopkolan, 8)
print(data)