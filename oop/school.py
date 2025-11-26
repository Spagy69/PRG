class School:

    men = 0
    women = 0
    students = 0

    def __init__ (self, name, men, women):
        self.name = name
        self.men = men
        self.women = women

        School.men += self.men
        School.women += self.women
        School.students += self.women + self.men

    def __del__(self):
        School.men -= self.men
        School.women -= self.women
        School.students -= self.women + self.men

c1a = School("Class 1A", 10, 15)
c2a = School("Class 2A", 20, 30)
c1b = School("Class 1B", 0, 50)
c2b = School("Class 2B", 15, 5)

print(str(School.students) + " students")
print(str(School.men) + " men")
print(str(School.women) + " women")
print("—" * 15)
del c2a
print(str(School.students) + " students")
print(str(School.men) + " men")
print(str(School.women) + " women")