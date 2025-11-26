def sumOfNums(x, y):
    return x + y

def sumOfNums2(*nums):
    for i in nums:
        print(i, end = " * ")

print(sumOfNums(3, 21))
print(sumOfNums(3.11, 25))
print(sumOfNums("Čau", " Debile"))
print(sumOfNums(str(21), " Fichtl"))

# 3 -2, 17
print(sumOfNums(3, sumOfNums(-2, 17)))

# 5 -14 9 -6
s = sumOfNums
p = print

p(s(s(5, -14), s(9, -6)))

s2 = sumOfNums2

p(s2(5, -14, 9, -6, 9, 69, 42, 47, 987, 61, -9971))