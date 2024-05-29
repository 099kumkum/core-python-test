array_list = [1, 2, 3, 4, 5]
print(array_list)
print(array_list[0])
for i in array_list:
    print(i)

array1 = ["Ram", "Shyam", "Balram"]
print(array1)
print(array1[0])
print(array1[-1])
array1.insert(1, "Raj")
print(array1)
array1.remove("Raj")
print(array1)

array2 = int(input("Enter a number: "))
for i in range(1, 11):
    print(array2 * i)
