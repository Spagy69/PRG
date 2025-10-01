class Auto:
    def __init__(self, brand, model, year, used):
        self.brand = brand
        self.model = model
        self.year = year
        self.used = used

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}, Condition: {self.used}"

print(Auto("Toyota", "Corolla", 2020, "New").display_info())

myCar = Auto("Škoda", "100", 1970, "Used")
print(myCar.display_info())