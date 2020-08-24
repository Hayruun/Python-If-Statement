# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme 
#    durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu 
#    lise ya da üniversite olmalıdır.

name = input("İsminizi giriniz: ")
gir = input('Yaşınız: ')
age = int(gir)
education = input('Eğitim Durumu: ')


#if (age<18):
#    print("Ehliyet Alamazsınız")
#elif education == "Lise" :
#    print("Ehliyet Alabilirsiniz")
#elif education == "Üniversite" :
#    print("Ehliyet Alabilirsiniz")
#else:
#    print("Ehliyet Alamazsınız.")

if (age>=18):
    if (education == 'lise' or 'üniversite'):
        print(f'{name} isimli kişi ehliyet alabilir.')
    else:
        print(f'{name} isimli kişi ehliyet almak için eğitim durumu yeterli değildir.')
else:
    print(f'{name} isimli kişinin ehliyet için yaşı tutmamaktadır.')



