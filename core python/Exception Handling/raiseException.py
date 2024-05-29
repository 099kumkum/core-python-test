''''
list = [1, 2, 3]
i = 2
if i > len(list):
    raise IndexError
else:
    print(list[i])

try:
    number = int(input("Enter a number: "))
    if number <=10:
        raise Exception("Number is less than 10")
except Exception as e:
    print(e)


try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    num3 = num1 / num2
    print("num1/num2=", num3)
except ZeroDivisionError:
    print("division by zero")
else:
    print("divisible")
'''
