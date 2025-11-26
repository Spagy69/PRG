class Osoba:
    def __init__(self, jmeno, prijmeni, vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek

    def pozdrav(self):
        return f"Ahoj, jmenuji se {self.jmeno} {self.prijmeni} a je mi {self.vek} let."
    
print(Osoba("Vít", "Machač", 16).pozdrav())

matej = Osoba("Matěj", "Adamec", 16)

print(matej.pozdrav())