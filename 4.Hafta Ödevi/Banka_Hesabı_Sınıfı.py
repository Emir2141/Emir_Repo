class BankaHesabi:
    def __init__(self, owner, bakiye=0):
         self.owner = owner
         self.bakiye = bakiye

    def bilgi_ver(self):
         print("\n--------------Hesap Bilgileri-------------------")
         print()
         print(f"Hesap sahibi {self.owner} ve bakiyesi {self.bakiye}")

    def para_yatır(self):
         x = int(input("Hesabına ne kadar para yatırmak istersin: "))
         self.bakiye += x

    def para_çek(self):
         y = int(input("Hesabından ne kadar para çekmek istersin: "))
        
         if self.bakiye < y :
              print("\n Hesapta o kadar para yok. :(")
         else:
              self.bakiye -= y
              print(f"Hesapta kalan para: {self.bakiye}")

o1 = BankaHesabi("Emir")

seçenekler = {
     "Hesap Bilgileri": "1",
     "Para Yatırma": "2",
     "Para Çekme": "3",
     "Çıkış": "4"
}
print()
print("__________Seçenekler____________")
for x, y in seçenekler.items():
     print(f"{x}: {y}")


while True:
    print()
    p = int(input("Hangi seçeneği seçeceksin numarayı gir: "))

    if p == 1 :
        o1.bilgi_ver()
    elif p == 2:
        o1.para_yatır()
    elif p == 3:
        o1.para_çek()
    elif p == 4:
        print("Çıkış yapıldı.")
        break