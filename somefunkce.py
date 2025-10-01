list1 = []

def fixa(**fixa):
    list1 = [fixa["Color"], fixa["State"]]
    return list1

print(fixa(Color="Red", State="Open"))

def mabs(x):
    if x >= 0:
        return x
    else:
        return -x
    
    
def mpi():
    return 3.141592653589793
    
def lichecislo(x):
    if x % 2 != 0:
        return True
    else:
        return False

print(lichecislo(2))
print(5 * mpi())
print(3 + mabs(-5) * 2)