'''
# table using for loop
for i in range(1, 11):
    print(2 * i)

# armstrong or not
num = str(31)
length = len(num)
sum = 0
for digit in num:
    sum += int(digit) ** length
if num == sum:
    print("It is armstrong number")
else:
    print("Not armstrong number")

# max of two numbers
a = [10, 70, 90, 65]
print("Max number is", max(a))


# calculate age
def age(current_year, birth_year):
    print("Age is", current_year - birth_year)


age(2024, 2003)

# smaller number using conditional operator
a = 30
b = 44
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")

# reverse digit of number
s = 12345
print(str(s)[::-1])

# concatenate two strings
name = 'Vijay'
surname = 'Chouhan'
print(name + surname)

# extracting lastname
name = "Vijay Chouhan"
print(name[0:5])

# counting occurrence
name = "kumkum"
print(name.count('k'))

# random integers
import random

print(random.sample(range(1, 100), 5))


# simple interest
def simple_interest(p, r, t):
    print("Simple interest is", p * r * t / 100)


simple_interest(1000, 10, 2)

# generate triangle
rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i + 1):
        print(j, end="")
    print()

# sum of integers between 100 and 200 divisible by 7
sum = 0
for i in range(100, 201):
    if i % 7 == 0:
        sum += i
print(sum)

# number is prime or not
num = 31
for i in range(2, num):
    if num % i == 0:
        print("It is not a prime number")
    else:
        print("It is a prime number")
        break

# number is  palindrome or not
num = 1234
if num == str(num)[::-1]:
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")

# generating harmonic series
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += 1 / i
    print(f'1/{i}')



from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person("Kumkum", 20)
person2 = Person.fromBirthYear("kumkum", 2003)
print(person1.age)
print(person2.age)
'''
