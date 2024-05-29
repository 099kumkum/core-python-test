'''
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


class Hexagon(Polygon):
    def noofsides(self):
        print("I have six sides")


class Quadrilateral(Polygon):
    def noofsides(self):
        print("I have four sides")


tri_obj = Triangle()
tri_obj.noofsides()
qua_obj = Quadrilateral()
qua_obj.noofsides()
penta_obj = Pentagon()
penta_obj.noofsides()
hexa_obj = Hexagon()
hexa_obj.noofsides()
'''

'''
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def area(self, radius):
        print(3.14 * radius)


obj = Circle()
obj.area(5)

'''