'''
#forloop
numbers = [1, 2, 4, 16, 20]
for val in numbers:
    square = val * val
    print(square)

# IfElse
price = 99
if price < 100:
    print("I can buy pizza")
else:
    print("I can not buy pizza")


# nestedifelse
age = int(input("Enter your age:"))
if age < 18:
    print("You are minor")
    print("You are not eligible to work")

else:
    if age >= 18 and age <= 60:
        print("You are eligible to work")
        print("Please fill in the details")
    else:
        print("You are too old to work as per the government rule")
        print("Please collect your pension")

# whileloop
i = 0
while i < 5:
    print(i)
    i += 1
    '''


