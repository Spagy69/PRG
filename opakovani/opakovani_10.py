# 10. Vytvoř seznam náhodných čísel a otoč jeho pořadí metodou reverse().

import random
import math

list = []

for i in range(0, 10):
    list.append(random.randint(1,100))

list.reverse()
print(list)