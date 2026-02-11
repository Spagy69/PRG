class System:
    def __init__(self):
        self.__projektor = Projektor()
        self.__reproduktory = Reproduktory()
        self.__platno = Platno()
    
    def zapnout_prezentaci(self, hlasitost, vstup):
        result = self.__projektor.zapnout()
        result += self.__projektor.nastavit_vstup(vstup)
        result += self.__reproduktory.zapnout()
        result += self.__reproduktory.nastavit_hlasitost(hlasitost)
        result += self.__platno.spusit_dolu()
        return result

    def vypnout_prezentaci(self):
        result = self.__projektor.vypnout()
        result += self.__reproduktory.vypnout()
        result += self.__platno.vytahnout_nahoru()
        return result

    def sledovat_video(self):
        result = self.__reproduktory.nastavit_hlasitost(100)
        return result

class Projektor:
    def zapnout(self):
        return "Projektor zapnut"
    
    def vypnout(self):
        return "Projektor vypnut"
    
    def nastavit_vstup(self, vstup):
        return f"Byl nastaven vstup {vstup}"

class Reproduktory:
    def zapnout(self):
        return "Reproduktory zapnuty"
    
    def vypnout(self):
        return "Reproduktory vypnuty"
    
    def nastavit_hlasitost(self, hlasitost):
        return f"Byla nastavena hlasitost reproduktorů na {hlasitost}"

class Platno:
        def spusit_dolu(self):
            return "Platno bylo spusteno"
    
        def vytahnout_nahoru(self):
            return "Platno bylo vytahnuto nahoru"


projektorovy_system = System()
print(projektorovy_system.zapnout_prezentaci(50, "VGA"))
print(projektorovy_system.sledovat_video())
print(projektorovy_system.vypnout_prezentaci())