strana_podstavy = int(input("Zadejte stranu a: "))
vyska_jehlanu = int(input("Zadejte výšku v: "))

if strana_podstavy == 0 or vyska_jehlanu == 0:
    print("Zadal jsi nulu pro výšku v nebo stranu a.")
else:
    V = 1/3 * (strana_podstavy ** 2) * vyska_jehlanu
    print(f"V = {V:.2f}")

