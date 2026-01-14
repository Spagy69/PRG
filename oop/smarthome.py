from abc import ABC, abstractmethod

class SmartHome(ABC):

    @abstractmethod
    def setProperties(self, **kwargs):
        pass

    @abstractmethod
    def getProperties(self, **kwargs):
        pass

class Lights(SmartHome):

    def __init__(self, name, room, type_of_light, luminosity, color):
        self.name = name
        self.room = room
        self.type_of_light = type_of_light
        self.luminosity = luminosity
        self.color = color

    def setProperties(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                print(f"Vlastnost '{key}' u světla '{self.name}' neexistuje a nemůže být nastavena.")

    def getProperties(self, **kwargs):
        all_props = {
            "name": self.name,
            "room": self.room,
            "type_of_light": self.type_of_light,
            "luminosity": self.luminosity,
            "color": self.color
        }
        
        if not kwargs:
            return all_props
        
        selected_props = {}
        for key in kwargs:
            if key in all_props:
                selected_props[key] = all_props[key]
        return selected_props

    def __str__(self):
        return f"Light(Name: {self.name}, Room: {self.room}, Type: {self.type_of_light}, Luminosity: {self.luminosity}, Color: {self.color})"

class Routers(SmartHome):
    def __init__(self, name, room, IP, supported_frequencies, mesh):
        self.name = name
        self.room = room
        self.IP = IP
        self.supported_frequencies = supported_frequencies
        self.mesh = mesh

    def setProperties(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                print(f"Vlastnost '{key}' u routeru '{self.name}' neexistuje a nemůže být nastavena.")

    def getProperties(self, **kwargs):
        all_props = {
            "name": self.name,
            "room": self.room,
            "IP": self.IP,
            "supported_frequencies": self.supported_frequencies,
            "mesh": self.mesh
        }
        
        if not kwargs:
            return all_props
            
        selected_props = {}
        for key in kwargs:
            if key in all_props:
                selected_props[key] = all_props[key]
        return selected_props

    def __str__(self):
        return f"Router(Name: {self.name}, Room: {self.room}, IP: {self.IP}, Frequencies: {self.supported_frequencies}, Mesh: {self.mesh})"


light1 = Lights("Stropní světlo", "Obývák", "LED", 80, "Teplá bílá")
print(f"Původní stav: {light1}")

# Test setProperties
light1.setProperties(luminosity=100, color="Studená bílá")
print(f"Nový stav: {light1}")

# Test getProperties (vše)
print(f"Všechny vlastnosti: {light1.getProperties()}")

# Test getProperties (jednotlivé vlastnosti)
print(f"Jednotlivé vlastnosti: {light1.getProperties(name=True, room=True)}")

print(150 * "-")

router1 = Routers("Main Router", "Chodba", "192.168.1.1", [2.4, 5], True)
print(f"Původní stav: {router1}")

# Test setProperties
router1.setProperties(IP="10.0.0.1")
print(f"Nový stav: {router1}")

# Test getProperties (vše)
print(f"Všechny vlastnosti: {router1.getProperties()}")

# Test getProperties (jednotlivé vlastnosti)
print(f"Jednotlivé vlastnosti: {router1.getProperties(name=True, room=True)}")
