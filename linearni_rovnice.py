a = float(input("Zadej koeficient a: "))
b = float(input("Zadej koeficient b: "))

if a != 0:
    x=-b/a
    print("Kořen rovnice je:", x)
else:
    print("Zadal jsi nulu pro koeficient. Rovnice nemá řešení.")
