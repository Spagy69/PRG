class Pozemek:

    total_area = 0
    total_build = 0
    total_agri = 0

    def __init__(self, id, area, kind):
        self.id = id
        self.area = area
        self.kind = kind

        Pozemek.total_area += area
        
        if kind == "stavebni":
            Pozemek.total_build += area

        elif kind == "zpf":
            Pozemek.total_agri += area

    def set_kind(self, new_kind):
            
            # Odečte
            if self.kind == "stavebni":
                Pozemek.total_build -= self.area

            elif self.kind == "zpf":
                Pozemek.total_agri -= self.area
            
            # Přidá
            if new_kind == "stavebni":
                Pozemek.total_build += self.area

            elif new_kind == "zpf":
                Pozemek.total_agri += self.area
        
            self.kind = new_kind

    def __del__(self):

        Pozemek.total_area -= self.area

        if self.kind == "stavebni":
            Pozemek.total_build -= self.area

        elif self.kind == "zpf":
            Pozemek.total_agri -= self.area

    def summary():
        print(f"{Pozemek.total_area} m2 celkem, {Pozemek.total_build} m2 stavební, {Pozemek.total_agri} m2 ZPF")
    

p1 = Pozemek(1, 500, "stavebni")
p2 = Pozemek(2, 1000, "zpf")
p3 = Pozemek(3, 200, "stavebni")

Pozemek.summary()

p3.set_kind("zpf")
Pozemek.summary()

del p1
Pozemek.summary()