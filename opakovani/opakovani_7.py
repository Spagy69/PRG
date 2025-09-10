# 7. Ze seznamu slov odstraň jedno konkrétní slovo (metoda remove). Pokud tam není, vypiš hlášku.

list = ["Jablko", "Chleba", "Počítač"]

print(list)

odstarnit = input(str("Jaké slovo chcete odstranit?: "))

if list.count(odstarnit) == 1:
    list.remove(odstarnit)
    print(f"Slovo {odstarnit} bylo úspešně odstraněno")
    print(list)
else:
    print(f"Slovo {odstarnit} se tam nenachází")
