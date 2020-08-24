# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#    not aralığına karşılık gelen not bilgisini yazdırınız.
#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

yazili1 = input('İlk yazılı notunuzu giriniz: ')
y1 = float(yazili1)
yazili2 = input('İkinci yazılı notunuzu giriniz: ')
y2 = float(yazili2)
sozlu = input('Sözlü notunuzu giriniz: ')
s1 = float(sozlu)

ort = ((y1+y2+s1)/3)
if (0<=ort<25):
    print('Not Bilgisi:0')
elif (25<ort<45):
    print('Not Bilgisi:1')
elif  (45<ort<55):
    print('Not Bilgisi:2')
elif (55<ort<70):
    print('Not Bilgisi:3')
elif (70<ort<84):
    print('Not Bilgisi:4')
elif (85<ort<=100):
    print('Not Bilgisi:5')
else:
    print('Girilen değerlerde hata var.')