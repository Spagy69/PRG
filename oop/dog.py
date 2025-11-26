class Dog:

    count = 0
    money = 0

    def __init__(self, race, sex, age, price):
        self.race = race
        self.sex = sex
        self.age = age
        self.price = price
        Dog.count += 1

    def __del__(self):
        Dog.count -= 1
        Dog.money += self.price
    
shiba_inu = Dog("Shiba-Inu", "Male", 1, 15000)
shih_tzu = Dog("Shih-tzu", "Female", 2, 10000)
husky = Dog("Husky", "Female", 2, 20000)
chrt = Dog("Chrt", "Male", 3, 15000)

del shih_tzu

print(Dog.count)

print(Dog.money)