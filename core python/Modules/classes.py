'''
class Hello:
    pass


print(Hello())


class Person:
    def __init__(self):
        print("Hello")


h = Person()


class Shape:
    name = "Circle"


shape = Shape()
print(shape.name)


class Shape:
    name = "Circle"

    def change_name(self, new_name):
        self.name = new_name


shape_obj = Shape()
print(shape_obj.name)
Shape.change_name("Triangle")
print(shape_obj.name)





class MyClass:
    x = 10


obj = MyClass()
print(obj.x)
'''