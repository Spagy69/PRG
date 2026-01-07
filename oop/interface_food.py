from abc import ABC, abstractmethod

class FastFood(ABC):
    
    @abstractmethod
    def accept_order(self, what, deliver_number):
        pass

    @abstractmethod
    def cook(self, what, deliver_number):
        pass
    
    @abstractmethod
    def pack(self, deliver_number):
        pass
    
    @abstractmethod
    def deliver(self, deliver_number):
        pass
    
class KFC(FastFood):
    def accept_order(self, what, deliver_number):
        print(f"Accepting order {what} for deliver number {deliver_number}")
    def cook(self, what, deliver_number):
        print(f"Cooking {what} for deliver number {deliver_number}")
    def pack(self, deliver_number):
        print(f"Packing for deliver number {deliver_number}")
    def deliver(self, deliver_number):
        print(f"Delivering for deliver number {deliver_number}")
    pass

class McDonald(FastFood):
    def accept_order(self, what, deliver_number):
        print(f"Accepting order {what} for deliver number {deliver_number}")
    def cook(self, what, deliver_number):
        print(f"Cooking {what} for deliver number {deliver_number}")
    def pack(self, deliver_number):
        print(f"Packing for deliver number {deliver_number}")
    def deliver(self, deliver_number):
        print(f"Delivering for deliver number {deliver_number}")
    pass

class BurgerKing(FastFood):
    def accept_order(self, what, deliver_number):
        print(f"Accepting order {what} for deliver number {deliver_number}")
    def cook(self, what, deliver_number):
        print(f"Cooking {what} for deliver number {deliver_number}")
    def pack(self, deliver_number):
        print(f"Packing for deliver number {deliver_number}")
    def deliver(self, deliver_number):
        print(f"Delivering for deliver number {deliver_number}")
    pass

kfc = KFC()

kfc.accept_order("Chicken Wings", 1)
kfc.cook("Chicken Wings", 1)
kfc.pack(1)
kfc.deliver(1)

print("\n")

mcdonald = McDonald()

mcdonald.accept_order("Big Mac", 2)
mcdonald.cook("Big Mac", 2)
mcdonald.pack(2)
mcdonald.deliver(2)

print("\n")

burger_king = BurgerKing()

burger_king.accept_order("Whopper", 3)
burger_king.cook("Whopper", 3)
burger_king.pack(3)
burger_king.deliver(3)
