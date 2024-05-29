'''
# AbstractMethod
from abc import ABC, abstractmethod


class Polygon(ABC):
    def noofsides(self):
        pass


class Triangle(Polygon):
    def noofsides(self):
        print("I have three sides")


class Pentagon(Polygon):
    def noofsides(self):
        print("I have five sides")


t = Triangle()
t.noofsides()
p = Pentagon()
p.noofsides()
'''

'''
# builtinFunction
class Student:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

    def display(self):
        print("Name:%s, ID:%d, age:%d")


s = Student("John", 101, 22)
print(s.__doc__)
print(Student.__name__)
print(s.__dict__)
print(s.__module__)
'''

'''
# Circle
class Circle:
    PI = 3.14

    def __init__(self, r, c='', b=0):  # Constructer receiving two parameters
        self.radius = r  # Instance variable
        self.color = c
        self.borderWidth = b

    def area(self):
        return self.radius * self.radius * Circle.PI


c = Circle(12.5, 'blue', 3)
print(c.area(), c.color, c.borderWidth)
'''

'''
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print("Name: %s \nAge: %s\nSalary : %s"%(self.name, self.age, self.salary) )


emp1 = Employee("Kumkum", 20, 40000)
emp2 = Employee("Priya", 28, 45000)
emp1.display()
emp2.display()
'''

'''
# createclass
class Employee:
    id = 10
    name = "Ram"

    def display(self):
        print("id:%d, name:%s" % (self.id, self.name))


emp = Employee()
emp.display()
'''

'''
# encapsulation
class Person:
    def __init__(self):
        self.name = "no name"

    def display(self, name):
        print("Hello", name)


p = Person()
p.display("Ram")
p.display("Shyam")
'''

