'''
# NameError
try:
    print(name)

except NameError as e:
    print(e)

else:
    print("Something else went wrong")
'''

'''
# RaisingException
number = int(input("Enter a number: "))
if number > 10:
    raise Exception("x should not exceed 10. The number is {}".format(number))
'''
'''
# ZeroDivisionError
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = num1 / num2
    print("num1/num2=", num3)

except ZeroDivisionError:
    print("Can't divide by zero")

else:
    print("It is else block")
'''

'''
# FinallyClause
def hello():
    try:
        return 1
    finally:
        return 2

k=hello()
print(k)
'''
'''
# ValueError
while True:
    try:
        x = int(input("Enter a number: "))
        print("%s squared is %s" % (x, x ** 2))
    except ValueError:
        print("Please enter a only number")
'''