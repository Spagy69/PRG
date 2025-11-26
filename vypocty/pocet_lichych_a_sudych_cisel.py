cisla = [4,2,6,7,8,6]
pocet_cisel = len(cisla)

liche_cisla = 0
sude_cisla = 0

for i in range(0, pocet_cisel):
    if cisla[i] % 2 == 0:
        sude_cisla += 1
    else:
        liche_cisla += 1

print("Počet lichých čísel: " + str(liche_cisla))
print("Počet sudých čísel: " + str(sude_cisla))