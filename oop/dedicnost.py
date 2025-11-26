class Polygon:
    def __init__(self, sides):
        self.__sides = sides # Private attribute - (__PREFIX)

    def get_sides(self):
        return self.__sides
    
    def set_sides(self, sides):
        self.__sides = sides

    def __str__(self):
        return f"Počet stran polygonu je: {self.get_sides()}"
    
class Triangle(Polygon):
    
    def __init__(self):
        Polygon.__init__(self, 3)

    def __str__(self):
        return super().__str__() + " Trojúhelník má tři strany. Vždycky trojúhelník"
    
class Pentagon(Polygon):
    
    def __init__(self):
        Polygon.__init__(self, 5)

    def __str__(self):
        return super().__str__() + " Pětiúhelník má pět stran. Vždycky pětiúhelník"

t = Triangle()
print(t)

p = Polygon(7)
# print(p.__sides) - chybně, nelze volat private vlastnost
print(p.get_sides())  # Output: 7
# p.__sides = 8 - chybně, nelze volat private vlastnost
p.set_sides(10)
print(p.get_sides())  # Output: 10