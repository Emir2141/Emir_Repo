#Toplama yapan fonk
def toplama():
    t = input("Toplamak istediğin sayıların aralarında boşluk bırakarak gir: ")
    n1 = list(map(float, t.split()))
    toplam = sum(n1)
    
    print("Girilen sayılar: ", n1)
    print("Toplamın sonucu: ", toplam)

#Çarpma yapan fonk
def çarpma():
    çarpım = 1
    ç = input("Çarpmak istediğin sayıların aralarında boşluk bırakarak gir: ")
    n2 = list(map(float, ç.split()))
    for i in n2:
        çarpım *= i
    print("Çarpılan sayılar: ", n2)
    print("Çarpım sonucu: ", çarpım)

#Bölme yapan fonk
def bölme():
    b = input("Bölmek istediğin sayıları bölüm sırasıyla aralarında boşluk bırakarak gir: ")
    n3 = list(map(float, b.split()))
    bolum =n3[0]
    for i in n3[1:]:
        bolum /= i
    print("Bölünen sayılar: ", n3)
    print("Bölme sonucu: ", bolum)

#Çıkartma yapan fonk
def çıkartma():
    e = input("Çıkartmak istediğin sayıların aralarında boşluk bırakarak gir: ")
    n4 = list(map(float, e.split()))
    eksi = n4[0]
    for i in n4[1:]:
        eksi -= i
    print("Çıkartılan sayılar: ", n4)
    print("Çıkartma sonucu: ", eksi)

#Bölenleri bulan fonk
def bolen(n):
    bolenler = []
    for i in range(1,int(n ** 0.5 + 1)):
        if n % i == 0:
            bolenler.append(i)
            if i != n // i:   
                bolenler.append(n // i)
    return(bolenler)
    # sonuc = bolen(int(input("Bölenlerini bulmak istediğin sayıyı gir: ")))
    # print(sonuc)

#Asal olup olmadığında bakan fonk
def asal_kontrol():
    number = int(input("Bir sayı giriniz:"))

    if number > 1 :
        for i in range(2,int(number ** 0.5 + 1)):
            if number % i == 0:
                print("Asal değil.")
                break
        else:
            print("Asal.")
    else:
        print("1'den büyük bir sayı gir.")

#Asal sayı üreten fonk
def asal_uretec():
    number = 2
    howmanynumber = int(input("Kaç tane asal sayı istiyorsun: "))
    asal_sayilar = []
    while len(asal_sayilar) != howmanynumber:
            for i in range(2,int(number**0.5 +1)):
                if number % i == 0:
                    number += 1
                    break
            else:
                asal_sayilar.append(number)
                number += 1

    for x in range(len(asal_sayilar)):
        for i in range(len(asal_sayilar) - 1):
            if asal_sayilar[i] > asal_sayilar[i +1]:
                asal_sayilar[i],asal_sayilar[i +1] = asal_sayilar[i +1],asal_sayilar[i]

    print(asal_sayilar)

hesap_makinesi = {
    "Toplama": "1",
    "Çıkarma": "2",
    "Çarpma": "3",
    "Bölme": "4",
    "Sayının bölenlerini bulma": "5",
    "Asal sayı olup olmadığına bakma": "6",
    "Asal sayı üretme": "7"
}
print("")
print("")
print("Hesap makinesi yazılımına hoş geldin.")
print("Bu hesap makinesinde değişik özellikler bulunmaktadır.")
print("")
for x, y in hesap_makinesi.items():
    print(x, y)

print("")
p = int(input("İsteğin özelliğin numarasını yaz: "))

if p == 1:
    toplama()
if p == 2:
    çıkartma()
if p == 3:
    çarpma()
if p == 4:
    bölme()
if p == 5:
    sonuc = bolen(int(input("Bölenlerini bulmak istediğin sayıyı gir: ")))
    print(sonuc)
if p == 6:
    asal_kontrol()
if p == 7:
    asal_uretec()