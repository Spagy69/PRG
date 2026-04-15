# math a numpy pro výpočty a převody souřadnic
import math as m
import numpy as n

# Příklad dat pro výpočet vzdálenosti mezi městy
cities = [
    {"name": "Varnsdorf", "lat": 50.9110, "lon": 14.6180},
    {"name": "Rumburk", "lat": 50.9515, "lon": 14.5570},
    {"name": "Liberec", "lat": 50.7671, "lon": 15.0562},
    {"name": "Hrádek nad Nisou", "lat": 50.8528, "lon": 14.8446},
    {"name": "Děčín", "lat": 50.7816, "lon": 14.2148},
    {"name": "Ústí nad Labem", "lat": 50.6607, "lon": 14.0323},
    {"name": "Česká Kamenice", "lat": 50.7978, "lon": 14.4173},
    {"name": "Krásná Lípa", "lat": 50.9130, "lon": 14.5080},
    {"name": "Česká Lípa", "lat": 50.6855, "lon": 14.5376},
    {"name": "Nový Bor", "lat": 50.7570, "lon": 14.5560}
]

# Třída pro výpočet sférické vzdálenosti mezi dvěma městy pomocí fluent API
# s použitím Haversinovy formule

class Geo:
    def __init__(self, cities):
        self._cities = {city["name"]: city for city in cities}
        self._start_point = None
        self._end_point = None

    # Výběr výchozího bodu podle názvu města a vrácení instance pro další volání
    def from_point(self, city_name):
        self._start_point = self._cities.get(city_name)
        return self

    # Převod názvu města na souřadnice a vrácení instance pro další volání
    def to_point(self, city_name):
        self._end_point = self._cities.get(city_name)
        return self
    
    # Výpočet sférické vzdálenosti mezi dvěma body a vrácení výsledku v kilometrech
    def in_km(self):
        if not self._start_point or not self._end_point:
            raise ValueError("Výchozí i cílový bod musí být platná města.")

        R = 6371.0 # Poloměr Země v km

        lat1 = m.radians(self._start_point["lat"])
        lon1 = m.radians(self._start_point["lon"])
        lat2 = m.radians(self._end_point["lat"])
        lon2 = m.radians(self._end_point["lon"])

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = m.sin(dlat / 2)**2 + m.cos(lat1) * m.cos(lat2) * m.sin(dlon / 2)**2
        c = 2 * m.atan2(m.sqrt(a), m.sqrt(1 - a))

        return R * c

# Otestování nového API pro výpočet vzdálenosti mezi Varnsdorfem a Libercem
distance = Geo(cities).from_point("Varnsdorf").to_point("Liberec").in_km()
print(distance)