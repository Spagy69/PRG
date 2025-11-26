class Elf:

    pocet_elfu = 0

    def __init__(self, jmeno, vyrobek):
        self.jmeno = jmeno
        self.vyrobek = vyrobek
        Elf.pocet_elfu += 1
        print(f"Elf {self.jmeno} začal vyrábět {self.vyrobek}.")

    def __del__(self):
        Elf.pocet_elfu -= 1
        print(f"Elf {self.jmeno} dokončil práci a odešel od stolu.")
        
    def pracuj(self):
        return f"Elf {self.jmeno} vyrábí {self.vyrobek}..."
    
    def vypis_pocet():
        print(f"V dílně pracuje {Elf.pocet_elfu} elfové")
    
e1 = Elf("Arwen", "dřevěného koníka")
e2 = Elf("Borin", "plyšového medvídka")
e3 = Elf("Lina", "autíčko")
Elf.vypis_pocet()

e2.pracuj()
del e3

Elf.vypis_pocet()