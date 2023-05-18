from islemler import yeni_kullanici,kullanici_getir,kullaniciAdi_sifre_uret,anlik_uret

def menu_goruntule():
    secim = int(input("1-Yeni Kullanıcı Ekle\n2-Kullanıcı Bilgilerini Getir\n3-Kullanıcı Adı ve Şifre Oluştur\n4-Anlık Kullanıcı Adı ve Güçlü Şifre Oluştur\n5-Çıkış\nYanıt:"))
    return secim

def main():                                         # Menüdeki seçime göre fonksiyonlara iletiliyor.
    while True:                                     
        secim = menu_goruntule()
        if secim == 1:
            yeni_kullanici()
        elif secim == 2:
            kullanici_getir()
        elif secim == 3:
            kullaniciAdi_sifre_uret()
        elif secim == 4:
            anlik_uret()
        elif secim == 5:                            # Bu seçenekte program kapanıyor.
            break
        else:
            print("Hatalı Seçim!!!\n")
    
main()