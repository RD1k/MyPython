x = 1
print(id(x))
x = 2
print(id(x))

l =[1, 2, 3]
print(l)
print(id(l))
l.append(4)
print(l)
print(id(l))

x = 1
print(type(x))

x = 1
print(x)
print(type(x))

x = 10
print(x)
y = 5
print(x + y)

x = 100000000000000000000000000000000
y = 5
print(x + y)

f = 0.1
print(type(f))
print(f)

i1 = 2
i2 = 3
f1 = 2.1
f2 = 3.1
print(i1 + i2)
print(f1 + f2)
print(i1 + f2)
print(type(i1 + f2))

import math
print(math.sqrt(121))

user_input = input()
print(type(user_input))
print(user_input / 2)
number = int(user_input)
print(number / 2)

user_input = input("Please enter the integer number: ")

print(2**32)