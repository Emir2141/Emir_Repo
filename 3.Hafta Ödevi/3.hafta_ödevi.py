import random
from datetime import datetime, date, timedelta


#geri sayım
def geri_sayim():

    b = int(input("Kaçtan geriye sayalım : "))

    for i in range(b ,0,-1):
        print(i)
    print("................")
    print("Ateşle!")

#n'e kadar toplama
def toplama():

    n = int(input("1'den kaça kadar toplayalım: "))
    print(f"1'den senin seçtiğin sayıya kadar olan sayıların toplamı: {n*(n +1)/2}")

#çarpım tablosu
def çarpım_tablosu():
    for x in range(1,10):
        print(x, end=" : ")
        for y in range(1,10):
            
            print(x*y, end=" | ")
        print()

#rastgele sayı bulmaca
def rastgele():
    print("Buradaki amacın bilgisayarın seçtiği 1 ile 100 arasındaki sayıyı bulmaya çalışmak")
    a = random.randint(1,100)
    b = 0 #bunun bir önemi yok
    while b != a :
        b = int(input("Tahminini alalım: "))
        if b < a :
            print("Daha yüksek bi sayı dene : ")
        elif b > a :
            print("Daha küçük bir sayı dene : ")
        elif b == a :
            print("Sayıyı buldun. TEBRİKLER!!!")

#vizeye kalan tarih
def vize():
    print("Vizelerinin tarihi ne? ")
    yil = int(input("Yıl girin (YYYY): "))
    ay = int(input("Ay girin (1-12): "))
    gun = int(input("Gün girin (1-31): "))

    kullanici_tarihi = date(yil, ay, gun)
    print("Vizenin tarihi:", kullanici_tarihi)
    print()
    şuan = date.today()
    print(f"Şuan {şuan} ")
    print()
    fark = kullanici_tarihi - şuan
    print(f"O zaman vizene kalan süre: {fark.days} gün.")

#sayı kontrol
def kontrol():
    while True:
        try:
            int(input("Bir sayı giriniz: "))
        except ValueError:
            print("Sayı gir lütfen.!!")
        else:
            print("Sayı girdin tebrikler.")
            break

neyapcan = {
    "Geri sayım": "1",
    "N'e kadar olan sayıların toplamı": "2",
    "Çarpım tablosu": "3",
    "Rastgele seçilen sayıyı bul": "4",
    "Vizeye kalan tarih": "5",
    "Sayı kontrol": "6"
}

for k,l in neyapcan.items():
    print(k,l)
print()
p = int(input("Hangisi: "))
print()
if p == 1:
    geri_sayim()
if p == 2:
    toplama()
if p == 3:
    çarpım_tablosu()
if p == 4:
    rastgele()
if p == 5:
    vize()
if p == 6:
    kontrol()