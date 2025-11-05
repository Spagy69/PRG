class Nuts:

    total_weight = 0

    def __init__ (self, weight):
        self.weight = weight
        Nuts.total_weight += weight

    def __del__(self):
        Nuts.total_weight -= self.weight

order_1 = Nuts(10)
order_2 = Nuts(15)
order_3 = Nuts(100)

# Should be 10 + 15 + 100 = 125

print(str(Nuts.total_weight) + " kg")

del order_2

# Should be 125 - 15 = 110

print(str(Nuts.total_weight) + " kg")