
metin = "Açık bilim, araştırma çıktılarına ve süreçlerine herkesin serbestçe erişmesini, bunların ortak kullanımını, dağıtımını ve üretimini kolaylaştıran bilim uygulamasıdır."
print(metin[0:20])

liste = ["Açık Bilim", "Açık Erişim", "Açık Lisans", "Açık Eğitim", "Açık Veri", "Açık Kültür"]
for i in liste:
    print(i)
    i+=i


sozluk = {"Elma": "Ağaçta yetişen bir tür meyve", "Salatalık": "Fidan üzerinde büyüyen bir tür sebze"}
a=input("Kelimeyi gir: ")
if a=="Elma":
    print(sozluk['Elma'])
elif a=="Salatalık":
    print(sozluk['Salatalık'])
else:
    print("Böyle bir kelime listede yok. Lütfen başka bir kelime giriniz")



