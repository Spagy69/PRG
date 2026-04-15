class Query:
    def __init__(self, data):
        self.data = data
    
    def filter_by(self, field, value):
        self.data = [item for item in self.data if item.get(field) == value]
        return self

    def sort_by(self, field):
        self.data = sorted(self.data, key=lambda x: x.get(field))
        return self

    def limit(self, n):
        self.data = self.data[:n]
        return self
        
    def execute(self):
        return self.data

data = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 17},
    {"name": "Emily", "age": 18},
    {"name": "John", "age": 21},
    {"name": "Jack", "age": 22},
    {"name": "Kevin", "age": 18},
    {"name": "Annie", "age": 20},
    {"name": "Charlotte", "age": 17},
    {"name": "Wanda", "age": 18},
    {"name": "Adam", "age": 16},
    {"name": "Fiona", "age": 17},
    {"name": "Charlie", "age": 18},
    {"name": "Charlie", "age": 29}
]

result = Query(data).filter_by("age", 18).sort_by("name").limit(2).execute()

print(result)
