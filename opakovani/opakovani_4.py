# 4. Máš seznam čísel. Pomocí for a if zjisti, kolik čísel je sudých (využij count() pro kontrolu).

cisla = [4,2,6,7,8,6,6]
pocetCisel = len(cisla)
sudeCisla = 0
kontrolaCisel = 0

for i in range(0, pocetCisel):
    if cisla[i] % 2 == 0:
        sudeCisla += 1

print("Počet sudých čísel: " + str(sudeCisla))

for i in range(0, 1000, 2):
    x = cisla.count(i)
    if x > 0:
        kontrolaCisel += x

if kontrolaCisel == sudeCisla:
    print("Kontrola proběhla úspešně")
else:
    print("Kontrola neproběhla úspešně")