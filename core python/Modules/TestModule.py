'''
import module as test

test.greet("Kumkum")
a = test.Person['name']
print(a)
print(type(a))
b = test.Person['age']
print(b)
print(type(b))
c = test.Person['gender']
print(c)
print(type(c))
print(test.Person.keys())
print(test.Person.values())
print(test.Person.items())

import platform

x = platform.platform()
print(x)
print(type(x))
a = dir(platform)
print(a)

from math import sqrt, factorial

print(sqrt(81))
print(factorial(4))

from module import user
print(user)
'''