#Kullanıcı bilgilerini gösterme
def bilgi():
    name = str(input("Adınızı giriniz: "))
    surname = str(input("Soyadınızı giriniz: "))
    memleket = str(input("Memleketinizi giriniz: "))

    bilgiler = {
        "Ad": name.upper(),
        "Soyad": surname.upper(),
        "Memleket": memleket.upper()
    }

    for i in bilgiler:
        print(i, ":", bilgiler[i])

#fiyat al indirim al indirimi uygula

def indirim_hesapla():
    print("İndirimli fiyat hesaplama")
    price = float(input("Ürünün fiyatını giriniz: "))
    discount = float(input("İndirim oranını giriniz: "))
    price = price - (price * discount / 100)
    return print("İndirimli fiyat: ", price)


#ehliyet alabiliyonmu
def ehliyet():
    year = 2026
    birth = int(input("Doğum yılınızı giriniz: "))

    if year - birth >= 18:
        print("Ehliyet alabilirsiniz.")
    else:
        print("Ehliyet alamazsınız.")

#Puan hesaplama
def harf_notu_hesapla():
    
    vize = float(input("Vizeden kaç aldın : "))
    final = float(input("Finalden kaç aldın : "))
    puan = vize * 0.4 + final * 0.6
    print("Toplam puanın bu: ", puan)

    if puan >= 90:
        print("AA aldın")
    elif puan >= 85:
        print("BA aldın")
    elif puan >= 80:
        print("BB aldın")
    elif puan >= 75:
        print("CB aldın")
    elif puan >= 70:
        print("CC aldın")
    elif puan >= 65:
        print("DC aldın")
    elif puan >= 60:
        print("DD aldın")
    elif puan >= 50:
        print("FD aldın")
    else:
        print("FF aldın")


ödev = {
    "Bilgi Göster": "1",
    "İndirim Hesaplama": "2",
    "Ehliyet Kontrol": "3",
    "Puan Hesaplama": "4"
}

for x, y in ödev.items():
    print(x, y)

p = int(input("Hangi özelliği kullanmak istiyorsun: "))

if p == 1:
    bilgi()
if p == 2:
    indirim_hesapla()
if p == 3:
    ehliyet()
if p == 4:
    harf_notu_hesapla()


