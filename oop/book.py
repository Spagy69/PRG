class Book:
    def __init__(self, name, author, num_of_pages):
        self.name = name
        self.author = author
        self.num_of_pages = num_of_pages

    def about(self):
        return f"Název knihy: {self.name}, Autor: {self.author}, Počet stran: {self.num_of_pages}."
    
    def read(self, reader):
        return f"{reader} čte knihu {self.name} od {self.author}."
    
trabantBook = Book("Trabantem kolem světa: Velký deník z cest", "Daniel Přibáň", 624)
twistedBook = Book("Twisted Games", "Ana Huang", 478)

print(trabantBook.about())
print(trabantBook.read("Vít"))

print(twistedBook.about())
print(twistedBook.read("Maru"))