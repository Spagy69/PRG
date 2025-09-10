# 1. Vytvoř prázdný seznam a postupně do něj pomocí append() přidej pět čísel zadaných uživatelem.

list = []

for i in range(0, 5):
    userNumber = int(input("Zadej cislo: "))
    list.append(userNumber)

print(list)