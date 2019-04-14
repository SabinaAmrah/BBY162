__author__= "Sabina Amrahova"
from random import choice
name=input("Please, enter your name: ")
print("Welcome to the game, ", name)
print("In this game you will be asked to find country names. Good Luck!")
while True:
    words = choice(["Albania", "Algeria", "Angola", "Argentina", "Azerbaijan", "Australia", "Austria", "Bahamas", "Bahrain",
"Bangladesh", "Belarus", "Belgium", "Bhutan", "Botswana", "Brazil", "Bulgaria", "Burkina Faso", "Canada", "Colombia",
"Czech Republic", "Cyprus", "Cuba", "Croatia", "Costa Rica" "Denmark", "Dominican Republic", "Estonia", "Egypt", "Ecuador",
"Fiji", "Finland", "France", "Germany", "Gambia", "Georgia", "Greece", "Guinea", "Hungary", "Haiti", "Iceland", "India", "Iran",
"Ireland", "Italy", "Indonesia", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea", "Kyrgyzstan"
"Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macedonia",
"Madagascar", "Malawi", "Malaysia", "Maldives", "Malta", "Mauritania", "Mauritius", "Mexico", "Moldova", "Monaco", "Mongolia",
"Montenegro", "Morocco", "Mozambique", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nigeria", "Norway", "Oman",
"Pakistan", "Palestine", "Panama", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia",
"Rwanda", "Eswatini", "Samoa", "San Marino", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Singapore", "Slovakia",
"Slovenia", "Somalia", "Spain", "Sri Lanka", "Sudan", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania",
"Thailand", "Tonga", "Tunisia", "Turkey", "Turkmenistan", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom",
"United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"])

    words = words.upper()
    wordlength = len(words)
    print("Word you are looking for contains {} characters.\n".format(wordlength))
    guesses = []
    error = []
    life = 6

    while life > 0:
        if life == 6:
            print("_________")
            print("|	 |")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|________")
        elif life == 5:
            print("_________")
            print("|	 |")
            print("|	 O")
            print("|")
            print("|")
            print("|")
            print("|________")
        elif life == 4:
            print("_________")
            print("|	 |")
            print("|	 O")
            print("|	 |")
            print("|	 |")
            print("|")
            print("|________")
        elif life == 3:
            print("_________")
            print("|	 |")
            print("|	 O")
            print("|	\|")
            print("|	 |")
            print("|")
            print("|________")
        elif life == 2:
            print("_________")
            print("|	 |")
            print("|	 O")
            print("|	\|/")
            print("|	 |")
            print("|")
            print("|________")
        elif life == 1:
            print("_________")
            print("|	 |")
            print("|	 O")
            print("|	\|/")
            print("|	 |")
            print("|	/")
            print("|________")

        empty = ""
        for ch in words:
            if ch in guesses:
                empty = empty + ch

            else:
                empty = empty + " _ "

        if empty == words:
            print("Congratulations, you guessed the word!")

            break
        print("Guess the word", empty)
        print(life, "lives left")
        guess = input("Enter one character >>")
        guess = guess.upper()
        if guess == words:
            print("\n\nYour guess is correct, congratulations!\n\n")

            break
        if guess in guesses or guess in error:
            print("{} You have already said this character, please, say another character".format(guess))

        elif guess in words:
            rpt = words.count(guess)
            print("Correct.{0} character appears in the word only {1} time/times".format(guess, rpt))

            guesses.append(guess)
        else:
            print("Unfortunately your guess is incorrect. There is no such character in the word.")

            error.append(guess)
            life = life - 1
    if life == 0:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|	/ \ ")
        print("|________")
        print("\n\nYou have used all your lives :( ")

        print("The word you were trying to guess was {}\n\n".format(words))
    print("If you want to quit the game click \n'Q'\nIf you want to continue, press any other button")
    quitgame = input(">>")
    quitgame = quitgame.upper()
    if quitgame == "Q":
        break
    else:
        continue