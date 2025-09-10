# 9. Vytvoř seznam a pomocí while cyklu vypisuj a zároveň odstraňuj první prvek (pop(0)), dokud není prázdný.

list = [4,5,3,1,9,5]
print(list)

while True:
    x = len(list)

    if x != 0:
        list.pop(0)
        print(list)
    else:
        break

        
