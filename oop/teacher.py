class Teacher:

    def __init__(self, fname, lname, nickname, age, status, grade):
        self.fname = fname
        self.lname = lname
        self.nickname = nickname
        self.age = age
        self.status = status
        self.grade = grade

    def getInfo(self):
        return f"{self.fname} {self.nickname} {self.grade}"
    
    def printAllTeachers(sborType):
        for teachers in sborType.values():
            print(teachers.getInfo())
    

sbor = {
    "kozina" : Teacher("Petr", "Kozák", "žumpa", 52, "married", 1),
    "herman" : Teacher("Petr", "Heřmanský", "Berta", 60, "angry", 1),
    "cyril" : Teacher("Cyril", "Kochrda", "Walter White", 52, "aktivní", 2.5)
}

# print(sbor["kozina"].status)

if (sbor["kozina"].status == "married"):
    print("Sakra už si ho nevezmu")
else:
    print("Yes vezmu si ho")

# print(sbor["herman"].getInfo())

Teacher.printAllTeachers(sbor)