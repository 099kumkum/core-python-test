'''
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length + self.width


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)


class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 + self.base + self.height


r = Rectangle("Rectangle", 4, 5)
c = Circle("Circle", 3)
t = Triangle("Triangle", 5, 6)
print(r.name, "Area:", r.area())
print(c.name, "Area:", c.area())
print(t.name, "Area:", t.area())


class University:
    def __init__(self, name):
        self.name = name

    def total(self):
        pass


class College(University):
    def __init__(self, name, students, teachers):
        super().__init__(name)
        self.students = students
        self.teachers = teachers

    def total(self):
        return self.students + self.teachers


college = College("SICA", 1000, 20)
print(college.name, "Total:", college.total())


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("Ram", "Kumar")
x.printname()


class Persons:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Persons):
    pass


x = Student("Shyam", "Pandey")
x.printname()


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


s = Student("Shyam", "Pandey")
x.printname()


class MyClass:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def get_max_value(x, y):
        return max(x, y)


obj = MyClass(10)

print(MyClass.get_max_value(20, 30))

print(obj.get_max_value(98,34))
'''
