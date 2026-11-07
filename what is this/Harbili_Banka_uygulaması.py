import time

kullanıcı_bilgileri = {}


def kullanıcı_ekle():
    isim = input("Yeni Hesabın İsmi: ")

    kullanıcı_bilgileri[isim] = {
        "Bakiye": float(input("Bakiyeni Gir: ")),
        "Ek Bakiye": float(input("Ek Bakiyeni Gir: "))
    }

    print("Hesap oluşturuldu.\n")


def para_cekme(isim):

    if isim in kullanıcı_bilgileri:

        hesap = kullanıcı_bilgileri[isim]

        miktar = float(input("Ne kadar çekcen: "))

        if miktar > hesap["Bakiye"]:

            print("Paran yetmedi. Ek bakiye kullanacan mı? (evet/hayır)")
            cevap = input().lower()

            toplam = hesap["Bakiye"] + hesap["Ek Bakiye"]

            if cevap == "evet" and toplam >= miktar:

                print(
                    f"Para çekildi. Kalan kullanılabilir para: {toplam - miktar}"
                )

            elif cevap == "evet" and toplam < miktar:

                print(
                    f"Paran yetmiyor. {miktar - toplam} TL daha bul."
                )

            elif cevap == "hayır":

                print("İşlem iptal edildi.")

            else:

                print("Geçersiz giriş.")

        else:

            hesap["Bakiye"] -= miktar

            print(
                f"Para çekildi. Kalan bakiye: {hesap['Bakiye']}"
            )

    else:

        print("Bu isimde hesap bulunamadı.")


# Hesap ekleme kısmı
while True:

    kullanıcı_ekle()

    cevap = input("Başka hesap eklemek ister misin? (e/h): ")

    if cevap.lower() != "e":
        break


print("\n--- Kayıtlı Hesaplar ---")

for isim, bilgiler in kullanıcı_bilgileri.items():

    print(f"\nHesap: {isim}")

    for anahtar, deger in bilgiler.items():

        print(f"{anahtar}: {deger}")


hesap_ismi = input("\nHangi hesaptan para çekcen: ")

para_cekme(hesap_ismi)