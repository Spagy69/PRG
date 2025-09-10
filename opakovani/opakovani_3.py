# 3. Vytvoř seznam čísel 1–10, pomocí pop() postupně odstraňuj poslední prvky, dokud není seznam prázdný.

list = [1,2,3,4,5,6,7,8,9,10]
x = len(list)


for i in range(0, x):
    print(list) 
    list.pop()   