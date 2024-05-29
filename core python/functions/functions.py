'''
def my_function():
    print("This is my first function")


my_function()


def my_function(fname):
    print(fname, "Gupta")


my_function("Ram")
my_function("Shyam")
my_function("Raju")

country_name = input("Enter a country name:")


def my_function(country=country_name):
    print("I am from", country)


my_function("India")
my_function()


def my_function(food):
    for x in food:
        print(x)


fruits = ['apple', 'orange', 'cherry']
my_function(fruits)


def my_function(x):
    return 5 * x


print(my_function(2))
print(my_function(4))
print(my_function(6))

def sum(a, b):
    print(a + b)


sum(10, 20)


def substract(a, b):
    print(a - b)


substract(20, 10)


def multiply(a, b):
    return a * b


print(multiply(10, 20))


def divide(a, b):
    return a / b


print(divide(20, 10))
'''
