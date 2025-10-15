class Lady:
    def __init__(self, height, weight, age, sex, status, skin):
        self.height = height
        self.weight = weight
        self.age = age
        self.sex = sex
        self.status = status
        self.skin = skin

    def pozdrav(self):
        return f"Měří {self.height}cm, váží {self.weight}kg, je jí {self.age} let, je {self.sex}, a je {self.status}, je {self.skin}."

print(Lady(170, 60, 25, "žena", "svobodná", "bílá").pozdrav())

black_lady = Lady(165, 55, 30, "žena", "vdaná", "černá")

print(black_lady.pozdrav())

print(black_lady.height)