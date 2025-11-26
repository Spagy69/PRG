import random
import time
tries = 0

timer = 0

while True:
        random_int = random.randint(1,1000000)
        if random_int == 69:
            print("haha")
            print(f"pocet pokusu: {tries}")
            print(timer)
            break
        else:
            print(random_int)
            tries += 1

