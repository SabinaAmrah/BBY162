grade=0
"""ders notu sıfırdan hesaplanmaya başlasın diye grade=0 yazıyoruz"""
print("HTML kodları yalnız Notepad++ metin düzenleyicisinde yazılabilir. Doğru mu yoksa Yanlış mı?")
n = input("Cevabınızı giriniz: ").casefold()
if n == "Yanlış".casefold():
    """"".casefold(), cevabı hem büyük hem küçük hem de karşık harflerle yazabilmemizi sağlıyor"""
    grade +=20
    print("Cevabınız doğru")
    print("Şu anki notunuz: " + " " + str(grade))
else:
    print("Cevabınız yanlış")
    print("Bu sorudan 0 puan kazandınız")
    print("Şu anki notunuz: " + " " + str(grade))


print("Dünyada en büyük ülke neresidir?")
n = input("Cevabınızı giriniz: ").casefold()
if n == "Rusya".casefold():
    grade += 20
    print("Cevabınız doğru")
    print("Şu anki notunuz: " + " " + str(grade))

else:
    print("Cevabınız yanlış")
    print("Bu sorudan 0 puan kazandınız")
    print("Şu anki notunuz: " + " " + str(grade))

print("Mona Lisa portresi kimin eseridir?")
n = input("Cevabınızı giriniz: ").casefold()
if n == "Leonardo Da Vinci".casefold():
    grade += 20
    print("Cevabınız doğru")
    print("Şu anki notunuz: " + " " + str(grade))

else:
    print("Cevabınız yanlış")
    print("Bu sorudan 0 puan kazandınız")
    print("Şu anki notunuz: " + " " + str(grade))


print("Pycharm yalnız Linux işletim sisteminde çalışıyor. Doğru mu Yanlış mı?")
n = input("Cevabınızı giriniz: ").casefold()
if n == "Yanlış".casefold():
    grade += 20
    print("Cevabınız doğru")
    print("Şu anki notunuz: " + " " + str(grade))
else:
    print("Cevabınız yanlış")
    print("Bu sorudan 0 puan kazandınız")
    print("Şu anki notunuz: " + " " + str(grade))


print("Dünyada en yaygın şekilde kullanılan programlama dili hangisidir?")
n = input("Cevabınızı giriniz: ").casefold()
if n == "Java".casefold():
    grade += 20
    print("Cevabınız doğru")
    print("Şu anki notunuz: " + " " + str(grade))

else:
    print("Cevabınız yanlış")
    print("Bu sorudan 0 puan kazandınız")
    print("Şu anki notunuz: " + " " + str(grade))

print("Final notunuz: " + str(grade))

input()
""""Python interpreter kod bitince hemen kapanmasın diye sonda input() yazıyoruz ve herhangi bir düğmeye tıklamadan interpreter kapanmıyor"""







