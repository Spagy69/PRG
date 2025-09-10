# 8. Zeptej se uživatele na seznam čísel, seřaď je sestupně pomocí sort(reverse=True).

list = []

kolikCisel = int(input("Kolik čísel chcete zadat?: "))

for i in range(0, kolikCisel):
    cislo = int(input("Jaké číslo chcete zadat?: "))
    list.append(cislo)

list.sort(reverse=True)
print(list)