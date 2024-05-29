'''
def sum(a, b):
    return a + b


print(sum(3, 1))



def changelist(list):
    list.append(6)
    print(list)
    return


list = [1, 2, 3, 4, 5]
print(list)
changelist(list)
print(list)



def sumnum(a, *varg):
    t = a
    for n in varg:
        t += n
        return t


total = sumnum(1, 2, 3, 4, 5)
print('Total', total)



def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))


print("Output show passing value as a parameter : ")


def my_function(food):
    for x in food:
        print(x)


fruits = ["Ram", "Shyam", "Jerry"]
my_function(fruits)
'''