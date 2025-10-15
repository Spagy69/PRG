class Auto:
    def __init__(self, brand, model, year, used):
        self.brand = brand
        self.model = model
        self.year = year
        self.used = used

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}, Condition: {self.used}"
    
    def drive(self, driver):
        return f"{driver} drives {self.brand} {self.model}."
    
    def crash(self, driver):
        return f"{self.brand} {self.model} crashed by {driver}!"

print(Auto("Toyota", "Corolla", 2020, "New").display_info())

skodovka = Auto("Škoda", "100", 1970, "Used")
print(skodovka.display_info()) 

print(skodovka.drive("Vít"))
print(skodovka.crash("Matěj"))

trabant = Auto("Trabant", "601", 1985, "Used")

print(trabant.display_info())
print(trabant.drive("Vít"))