'''
# Single Level
class Parent:
    def show(self):
        print('Parent class is showing method')


class Child(Parent):
    def display(self):
        print('Child class is displaying method')


obj = Child()
obj.show()
obj.display()


# Multi Level
class GrandParent:
    def show(self):
        print('GrandParent class is showing method')


class Parent(GrandParent):
    def display(self):
        print('Parent class is displaying method')


class Child(Parent):
    def show_child(self):
        print('Child class is showing method')


obj = Child()
obj.show()
obj.display()
obj.show_child()



# Hierarchical Level
class Parent:
    def show(self):
        print('Parent class is showing method')


class Child1(Parent):
    def display(self):
        print('Child1 class is displaying method')


class Child2(Parent):
    def display2(self):
        print('Child2 class is displaying method')

obj1 = Child1()
obj2 = Child2()
obj1.display()
obj1.show()
obj2.display2()
obj2.show()


# Multiple level
class Parent1:
    def show(self):
        print('Parent1 class is showing method')


class Parent2:
    def show2(self):
        print('Parent2 class is showing method')


class Child(Parent1, Parent2):
    def display(self):
        print('Child class is displaying method')


obj = Child()
obj.show()
obj.show2()
obj.display()



class Employee:
    def __init__(self):
        self.name = "Ram"
        self._code = "E101"
        self.__salary = 25000


obj = Employee()
print(obj.name)
'''
