'''
class Person:
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address


p = Person()
p.set_name("Kumkum")
p.set_age(21)
p.set_address("Vijay Nagar")
print(p.get_name(), p.get_age(), p.get_address())


class Account:
    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number = number

    def get_type(self):
        return self.__type

    def set_type(self, type):
        self.__type = type

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance


a = Account()
a.set_number(26739)
a.set_type("Savings")
a.set_balance(2000)
print(a.get_number(), a.get_type(), a.get_balance())


class Automobile:
    def get_colour(self):
        return self.__colour

    def set_colour(self, colour):
        self.__colour = colour

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    def get_type(self):
        return self.__type

    def set_type(self, type):
        self.__type = type


x = Automobile()
x.set_colour("white")
x.set_speed(100)
x.set_type("SUV")
print(x.get_colour(), x.get_speed(), x.get_type())


class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("name:", self.name, "salary:", self.salary)


k = Employee("Kumkum", 5000)
k.displayEmployee()


class Persons:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Persons("Ram", 36)
print(p.name)
print(p.age)


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is", self.name)


p1 = People("Ram", 36)
p1.myfunc()


class People:
    def __init__(my_silly_object, name, age):
        my_silly_object.name = name
        my_silly_object.age = age

    def myfunc(abc):
        print("Hello my name is", abc.name)


p1 = People("Ram", 36)
p1.myfunc()

'''
