from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def whoami(self):
        pass

class Girrafe(Animal):
    def whoami(self):
        print("I am a girrafe")

g = Girrafe()
g.whoami()