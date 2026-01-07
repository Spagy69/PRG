from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def calculate(self, *args):
        pass

class Sum(Operation):
    def calculate(self, *args):
        return sum(args)

class Multiply(Operation):
    def calculate(self, *args):
        result = 1
        for x in args:
            result *= x
        return result

# Vytvoř objekt sum třídy Sum, zavolej metodu calculate(1, 3, 5, 0.1) a vypiš výsledek.
sum_obj = Sum()
print(sum_obj.calculate(1, 3, 5, 0.1))

# Vytvoř objekt mul třídy Multiply a zavolej metodu calculate(1, 3, 5, 0.1) a vypiš výsledek.
mul_obj = Multiply()
print(mul_obj.calculate(1, 3, 5, 0.1))
