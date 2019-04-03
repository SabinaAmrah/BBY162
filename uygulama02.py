__author__="Sabina Amrahova"
""""03.04.2019/place:Hacettepe Üniversitesi, Beytepe Kampüsü, Parlar Cafe, Caribou Coffee, Yelken Cafe / with Müberra Yılmaz """
questions= ['HTML kodları aşağıdaki metin düzenleyicilerinden hangisinde yazılabilir?: ',
          'Dünyada en büyük ülke neresidir? ',
          'Mona Lisa portresi kimin eseridir? ',
          'Pycharm aşağıdaki işletim sistemlerinden hangisinde çalışıyor? ',
          'Dünyada en yaygın şekilde kullanılan programlama dili hangisidir? ']
answers= ['E', 'C', 'A', 'D', 'E']
answersA=['Brackets', 'İspanya', 'Leonardo Da Vinci', 'Linux', 'C++']
answersB=['Notepad++', 'Fransa', 'Vincent Van Gogh', 'Windows', 'Python']
answersC=['Atom', 'Rusya', 'Pablo Picasso', 'MacOS', 'R language']
answersD=['BBEdit', 'Avustraliya', 'Frida Kahlo', 'Bunların hepsinde', 'C']
answersE=['Bunların hepsinde', 'İtalya', 'Salvador Dali', 'Unix', 'Java']
grade = 0
for i in range(len(questions)):
    print("Soru "+str(i+1) + ":" + questions[i])
    print("A) " + answersA[i])
    print("B) " + answersB[i])
    print("C) " + answersC[i])
    print("D) " + answersD[i])
    print("E) " + answersE[i])
    answer=input("Cevabınızı giriniz: ")
    if answers[i] == answer.upper():
        grade += 1
print("Testi tamamladınız. Puanınız: " + str(int((grade/len(questions))*100)))
input()