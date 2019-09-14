print("*************************************")
print("SAYI TAHMİN OYUNUMA HOŞGELDİN REİS")
print("*************************************")
from random import randint
x= randint(1,100)
tahmin=False
while not tahmin:
    try:
        Sayı=int(input("100 ile 1 arasında sayı yazınız."))
    except ValueError:
        print("Geçerli bir sayı girin.")
        continue
    if  Sayı>x:
        print("Büyük,Biraz daha küçük bi sayı yaz")
    elif Sayı<x:
        print("Küçük,Biraz daha büyük bi sayı yaz.")
    else:
        tahmin=True
print("Helal reis, başardın!")
