class RailFence:
    
    # počáteční inicializace vlastností objektu
    def __init__(self, rails = 3):
        self.__rails = rails    # počet kolejnic == 3
        self.__ot = ""          # otevřený text
        self.__ot_len = 0       # délka otevřeného textu
        self.__ct = ""          # šifrovaný text
        self.__ct_len = 0       # délka šifrovaného textu
         
    # šifruje open_text
    def encrypt(self, open_text):

        self.__ot = open_text                   # vlastnosti self.__ot přiřadíme hodnotu paramteru open_text
        self.__ot_len = len(self.__ot)          # vlastsnosti self.__ot_len přiřadíme délku řetězce selt.__ot
        self.__ct = ""
        
        row, asc = 0, True                      # row = aktuální řádek, col = aktuální sloupec, asc = True / False (vzestupně / sestupně)
        ct = [""] * self.__rails                # list s požadovaným počtem prázdných řetězců 
        
        for i in range(0, self.__ot_len):       # iterace otevřeného textu znak po znaku, zjišťujeme pozici řádku pro každý znak
            
            # tady je implementace šifrování            
            ct[row] += self.__ot[i]

            # zde určujeme číslo řádku pro každý znak otevřeného textu
            if (asc == True and row < self.__rails - 1):
                row += 1
            elif (asc == True and row == self.__rails - 1):
                asc = False
                row -= 1
            elif (asc == False and row > 0):
                row -= 1
            else:
                asc = True
                row += 1
        self.__ct = "".join(ct)
        return self.__ct
                      
    # dešifruje cypher_text
    def decrypt(self, cypher_text):
        self.__ct = cypher_text
        self.__ct_len = len(self.__ct)
        self.__ot = ""
        
        # Vytvoříme matici pro simulaci "cik-cak" pohybu
        # Inicializujeme prázdnými znaky (None nebo '\n')
        rail_matrix = [['\n' for i in range(self.__ct_len)] for j in range(self.__rails)]
        
        # Nejprve označíme pozice v matici, kam patří znaky (simulace pohybu)
        row, asc = 0, True
        for i in range(self.__ct_len):
            rail_matrix[row][i] = '*' # Značka
            
            # Posun na další řádek (stejná logika jako v encrypt)
            if (asc == True and row < self.__rails - 1):
                row += 1
            elif (asc == True and row == self.__rails - 1):
                asc = False
                row -= 1
            elif (asc == False and row > 0):
                row -= 1
            else:
                asc = True
                row += 1
                
        # Nyní vyplníme označené pozice znaky ze šifrovaného textu
        idx = 0
        for r in range(self.__rails):
            for c in range(self.__ct_len):
                if rail_matrix[r][c] == '*' and idx < self.__ct_len:
                    rail_matrix[r][c] = self.__ct[idx]
                    idx += 1
                    
        # Přečteme matici znovu v "cik-cak" pořadí pro získání otevřeného textu
        result = []
        row, asc = 0, True
        for i in range(self.__ct_len):
            result.append(rail_matrix[row][i])
            
            if (asc == True and row < self.__rails - 1):
                row += 1
            elif (asc == True and row == self.__rails - 1):
                asc = False
                row -= 1
            elif (asc == False and row > 0):
                row -= 1
            else:
                asc = True
                row += 1
                
        self.__ot = "".join(result)
        self.__ot_len = len(self.__ot)
        return self.__ot
    
    # getter vrátí počet kolejnic
    def getRails(self):
        return self.__rails
    
    # getter vrátí otevřený text
    def getOpenText(self):
        return self.__ot
    
    # getter vrátí délku otevřeného textu
    def getOpenTextLen(self):
        return self.__ot_len

    # getter vrátí šifrovaný text
    def getCypherText(self):
        return self.__ct
    
    # getter vrátí délku šifrovaného textu
    def getCypherTextLen(self):
        return self.__ct_len

cypher = RailFence()
print(cypher.encrypt("AHOJEVO"))

cypher2 = RailFence(4)
print(cypher2.encrypt("MATEJADAMECJEFEMBOY"))

print(cypher.decrypt("AEHJVOO"))
print(cypher2.decrypt("MDEYAAAJFOTJMCEBEEM"))