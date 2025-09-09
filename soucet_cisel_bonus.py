pocet_zadanych_cisel = int(input("Kolik čísel chceš zadat: "))
cisla = []

for i in range(0, pocet_zadanych_cisel):
    zadane = int(input("Zadej číslo: "))
    cisla.append(zadane)

soucet = sum(cisla)
print(soucet)