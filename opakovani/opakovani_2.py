# 2. Zeptej se uživatele na pět jmen, ulož je do seznamu a následně seznam seřaď abecedně.

list = []

for i in range(0, 5):
    userName = str(input("Zadej jmeno: "))
    list.append(userName)

list.sort()
print(list)