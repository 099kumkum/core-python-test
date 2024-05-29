'''
file = open("C:/Users/hp/Desktop/Test/kumkum.txt", 'w')
file.write("Here is your file\n")
file.write("Here is your code")
print("done")
print(type(file))
file.close()


file = open("C:/Users/hp/Desktop/Test/kumkum.txt", 'r')
print("File name", file.name)
print("File.mode", file.mode)
print("Is file closed", file.closed)
file.close()

file = open("C:/Users/hp/Desktop/Test/kumkum.txt")
text = file.read()
print(text)
print(type(text))
file.close()

file = open("C:/Users/hp/Desktop/Test/kumkum.txt")
for line in file:
    print(line)
file.close()


with open("C:/Users/hp/Desktop/Test/statement.txt", 'w') as file:
    file.write("here is your with statement\n")
    file.write("this is text file")
print("Done")



file = open("testing.py", 'w')
file.write("Here is your file")
print("Done")
file.close()

f = open("C:/Users/hp/Desktop/Test/kumkum.txt")
fo = f.read(5)
f1 = f.tell()
f2 = f.seek(2)
print(fo)
print(f1)
print(f2)
f.close()
'''


