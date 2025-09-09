import random

nahodnecislo = random.randint(1, 100)
hadani_list_hitorie = []
pocetpokusu = 1

while True:
    guess = int(input("Zadej cislo ktere si myslíš že to je: "))
    if guess > nahodnecislo:
        print("Hledej níže.")
        pocetpokusu += 1
        hadani_list_hitorie.append(guess)
    elif guess < nahodnecislo:
        print("Hledej výše.")
        pocetpokusu += 1
        hadani_list_hitorie.append(guess)
    elif guess == nahodnecislo:
        print("Uhadl jsi cislo!")
        print("Počet pokusů: " + str(pocetpokusu))
        print("Historie pokusů: " + str(hadani_list_hitorie))
        break