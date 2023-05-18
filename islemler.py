import random
liste, kullaniciAdlari, kullaniciSifreleri = [], [], []
def yeni_kullanici():
    adGir = input("Kullanıcının Adı:")
    soyadGir = input("Kullanıcının Soyadı:")                                 # Kullanıcı oluşturmak için genel bilgiler alınıyor.
    dogumTarihiGir = (input("Kullanıcının Doğum Tarihi:"))
    dogumYeriGir = input("Kullanıcının Doğum Yeri:")
    try:
        with open("bil104--projekullanicilar.txt","r",encoding= "utf-8") as file: 
            for line in file:                                                                     # Sıradaki kullanıcının Id numarasını buluyor.
                data = line.strip().split(',')
                idGir = data[-5]
        with open("bil104--projekullanicilar.txt","r",encoding= "utf-8") as file:                # Dosyada bilgi varsa okunuyor.
            content = file.read()
            liste.append(content)
    except:
        print("Dosya açılırken bir hata oluştu lütfen tekrar deneyiniz.\n")                      # Herhangi bir sorunda böyle bir mesaj iletiliyor.
        
    try:
        with open("bil104--projekullanicilar.txt","a",encoding= "utf-8") as file:                # Dosyaya kullanıcıdan alınan bilgiler ekleniyor.
            ekle = file.write(f"\n{int(idGir)+1},{adGir},{soyadGir},{dogumTarihiGir},{dogumYeriGir}")
            liste.append(ekle)
    except:
        print("Dosya açılırken bir hata oluştu lütfen tekrar deneyiniz.\n")                      # Herhangi bir sorunda böyle bir mesaj iletiliyor.
    finally:
        print("Kullanıcı başarıyla eklendi.\n")
        
        
def kullanici_getir():    
    try:
        getir = int(input("\nKullanıcı bilgisini görmek istediğiniz kullanıcının Id numarasını giriniz:"))   
        with open("bil104--projekullanicilar.txt","r",encoding= "utf-8") as file:
            oku = file.read()                                                          
            rows = oku.split('\n')  
            istenilen_satir = rows[getir].split(",")              # Kullanıcının istediği Id numarasına ait bilgileri almak için işlemler
            id = istenilen_satir[0]
            adı = istenilen_satir[1]
            soyAdı = istenilen_satir[2]
            dogumTarihi = istenilen_satir[3]
            dogumYeri = istenilen_satir[4]
            print(f"\n{id} numaralı oyuncunun\nAdı: {adı}\nSoyadı: {soyAdı}\nDoğum Tarihi: {dogumTarihi}\nDoğum Yeri: {dogumYeri}\n")
    except ValueError:
        print("Lütfen sayısal değer giriniz\n")
    except:
        print("Dosya açılırken bir hata oluştu lütfen tekrar deneyiniz.\n")  
               
def kullaniciAdi_sifre_uret():
    if __name__ == "__ortakIslemler__":
        ortakIslemler()                               #Uzun kod olmaması için işlemler fonksiyondan çağrılıyor.
             
def anlik_uret():
    adGir = input("Kullanıcının Adı:")                      # Kullanıcıdan bilgi alımı
    soyadGir = input("Kullanıcının Soyadı:")
    dogumTarihiGir = (input("Kullanıcının Doğum Tarihi:"))
    dogumYeriGir = input("Kullanıcının Doğum Yeri:")
    try:       
        with open("bil104--projekullanicilar.txt","r",encoding= "utf-8") as file: 
            for line in file:                                       # Sıradaki kullanıcının Id numarasını buluyor.
                data = line.strip().split(',')
                idGir = data[-5]                                                                                         
        with open("bil104--projekullanicilar.txt","a",encoding= "utf-8") as file:         # Dosyaya alınan bilgiler işleniyor.
            ekle = file.write(f"\n{float(idGir)+1},{adGir},{soyadGir},{dogumTarihiGir},{dogumYeriGir}")
            liste.append(ekle)
    except:
        print("Dosya açılırken bir hata oluştu lütfen tekrar deneyiniz.\n")        # Herhangi bir sorunda böyle bir mesaj iletiliyor.
    finally:
        print("Kullanıcı başarıyla eklendi.\n")
    ortakIslemler()
    

def ortakIslemler():
    try:
        karakter_dizisi = ["*","/","!","_","(",")","&","%","+","-",".",",","<",">"]
        getir = int(input("\nKullanıcı bilgisini görmek istediğiniz kullanıcının Id numarasını giriniz:"))
        with open("bil104--projekullanicilar.txt","r",encoding='utf-8') as file:
            oku = file.read()
            kucult = oku.lower()
            rows = kucult.split('\n')
            istenilen_satir = rows[getir].split(",")    # Kullanıcının istediği Id numarasına ait bilgileri almak için işlemler
            id = istenilen_satir[0]
            adı = istenilen_satir[1]
            soyAdı = istenilen_satir[2]
            dogumTarihi = istenilen_satir[3]
            dogumYeri = istenilen_satir[4]
            
            change_name = str(adı)[1] + str(adı)[3]
            change_surname = str(soyAdı)[-3:]
            change_DT = float(dogumTarihi[3:5]) + float(dogumTarihi[6:10])
            change_dogumTarihi = str(change_DT) + str(dogumTarihi[-2:])
            kullanici_adi = str(change_surname) + str(change_name) + str(change_dogumTarihi) 
            print(f"Oluşturulan kullanıcı adınız :{kullanici_adi}")
            kullaniciAdlari.append(kullanici_adi)
            
            sifre_ad = str(adı[0]) + str(adı.upper()[-1])
            sifre_soyad = random.choice(karakter_dizisi) + str(soyAdı[-2])
            sifre_DTarihi = str(dogumTarihi[-2:]) + str(float(dogumTarihi[3:5])**2)
            sifre_DYeri = str(dogumYeri[1:-2]).capitalize() + str(dogumYeri.upper()[-2])
            sifre_randomSayi = random.randint(10,100)
            kullanici_sifre = sifre_DYeri + str(sifre_randomSayi) + sifre_ad + sifre_DTarihi + sifre_soyad
            kullaniciSifreleri.append(kullanici_sifre)
            print(f"Oluşturulan kullanıcı şifreniz: {kullanici_sifre}")
        
            with open("kullaniciAdi_sifre.txt","a",encoding='utf-8') as file:
                file.write(f"{id},{kullanici_adi},{kullanici_sifre}\n")
    except:
        print("Dosya açılırken bir hata oluştu lütfen tekrar deneyiniz.\n")
    finally:
        print("Kullanıcı başarıyla oluşturuldu.\n")