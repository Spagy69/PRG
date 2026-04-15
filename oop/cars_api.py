# prijmeni (bez diakritiky): Machac
# Dataset: cars
# Povolene operatory: ['>=', '<=', '!=']
# Rozsireni: Query(data).sort_by("age").first() - Vrátí první záznam z aktuálního výsledku. 
# Poznámka pro pana učitele: klíč 'age' v listu není, proto použiju klíč 'year'.
# Data:
# {'model': 'Skoda', 'speed': 180, 'year': 2018}
# {'model': 'BMW', 'speed': 240, 'year': 2020}
# {'model': 'Audi', 'speed': 220, 'year': 2019}
# {'model': 'Mercedes', 'speed': 250, 'year': 2021}
# {'model': 'Volkswagen', 'speed': 200, 'year': 2017}

class Query:
    def __init__(self, data):
        self.data = data
    
    def filter(self, field, operator, value):
        if operator == ">=":
            self.data = [item for item in self.data if item.get(field) >= value]
        elif operator == "<=":
            self.data = [item for item in self.data if item.get(field) <= value]
        elif operator == "!=":
            self.data = [item for item in self.data if item.get(field) != value]
        return self

    def sort_by(self, field, descending=False):
        self.data = sorted(self.data, key=lambda x: x.get(field), reverse=descending)
        return self

    def limit(self, count):
        self.data = self.data[:count]
        return self

    def first(self):
        return self.data[0]

    def execute(self):
        return self.data


data = [
    {'model': 'Skoda', 'speed': 180, 'year': 2018},
    {'model': 'BMW', 'speed': 240, 'year': 2020},
    {'model': 'Audi', 'speed': 220, 'year': 2019},
    {'model': 'Mercedes', 'speed': 250, 'year': 2021},
    {'model': 'Volkswagen', 'speed': 200, 'year': 2017}
]

result = (
    Query(data)
    .filter("model", "!=", "Skoda")
    .sort_by("year")
    .limit(2)
    .execute()
)

print(result)
print("-"*100)

result1 = Query(data).sort_by("year").first()
print(result1)

