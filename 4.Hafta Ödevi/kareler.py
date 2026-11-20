
metin = "1'den ona kadar olan sayıların kareleri" 
for i in range (1,11):
    arti = f"{metin} {i}: {i **2} "
    metin = arti
print(arti)