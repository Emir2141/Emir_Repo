#araba sınıfı
class Araba:
    def __init__(self, marka, model, yıl):
        self.marka = marka
        self.model = model
        self.yıl = yıl

    def bilgi_ver(self):
        print("\n_______________ARABA BİLGİLERİ_______________")
        print("*********************************************")
        print(f"Arabanın markası: {self.marka} Modeli: {self.model} Yılı: { self.yıl}")
        print()



araba1 = Araba("Brodway", 1990, 1995)
araba2 = Araba("Reno", 2016, 2025)

araba1.bilgi_ver()
araba2.bilgi_ver()