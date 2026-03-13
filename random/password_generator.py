import random

print("=" * 50)
print("Generátor hesel 3000 approved by Voldemort")
print("=" * 50)

znaky = int(input("Zadej počet znaků: "))
velka_a_mala_pismena = str(input("Chcete přidat velká a malá písmena? (a/n): ")).lower()
cisla = str(input("Chcete přidat čísla? (a/n): ")).lower()
spec_znaky = str(input("Chcete přidat speciální znaky? (a/n): ")).lower()

heslo = ""
list_znaku = ""

if velka_a_mala_pismena == "a" or velka_a_mala_pismena == "ano":
    list_znaku += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
if cisla == "a" or cisla == "ano":
    list_znaku += "0123456789"
if spec_znaky == "a" or spec_znaky == "ano":
    list_znaku += "!@#$%^&*()_+-=,."
elif velka_a_mala_pismena == "n" and cisla == "n" and spec_znaky == "n" or velka_a_mala_pismena == "ne" and cisla == "ne" and spec_znaky == "ne":
    print("Musíš zadat alespoň jednu možnost přeci. bruh")
    exit()

for i in range(znaky):
    heslo += random.choice(list_znaku)

print("\n" + heslo + "\n")