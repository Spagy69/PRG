class Jewel:

    __instance = None
    
    @staticmethod
    def buy(name, price): 
        if Jewel.__instance is None:
            if name and price <= 1000:
                Jewel()
            else:
                print("Too expensive, honey!")
        else:
            print("Only one jewel, honey!")
        return Jewel.__instance
        
    
    def __init__(self):
        if Jewel.__instance is not None:
            raise Exception("Only one Jewel, honey!")
        else:
            Jewel.__instance = self
        
j1 = Jewel.buy("Ring", 1001)
j2 = Jewel.buy("Bracelet", 999)
print(j1, j2)