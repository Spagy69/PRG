from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def whoami(self):
        pass
    
    @abstractmethod
    def max_speed(self, speed):
        pass

    @abstractmethod
    def fuel(self, f):
        pass

# Vytvoř třídu Bugatti jako potomka třídy Vehicle.
# Přepiš abstraktní metody whoami, max_speed a fuel.

class Bugatti(Vehicle):
    def whoami(self):
        print("I am a Bugatti")
    def max_speed(self, speed):
        print("Max speed is", speed)
    def fuel(self, f):
        print("Fuel is", f)

# Vytvoř objekt třídy Bugatti a zavolej metody whoami, max_speed a fuel.
# whoami().

b = Bugatti()
b.whoami()
b.max_speed(200)
b.fuel("Petrol")