import math

polomer = int(input("Zadejte poloměr r: "))
vyska = int(input("Zadejte výšku v: "))

if polomer == 0 or vyska == 0:
    print("Zadal jsi nulu ve výšce nebo v poloměru.")
else:
    V = 1/3*math.pi*polomer**2*vyska
    print(f"V = {V:.2f}")
