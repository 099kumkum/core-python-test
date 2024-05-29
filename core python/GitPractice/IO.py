'''
# fileinfo
def fileInfo():
    fo = open("C:/Users/hp/Desktop/Test/kumkum.txt", "wb")
    print("File name:", fo.name)
    print("Mode of opening:", fo.mode)
    print("Is closed:", fo.closed)
    return


fileInfo()
'''

'''
# KeyboardToFileCopy
def file():
    file = open("Testing.txt", "w")
    text = input("Enter your message:")

    while (text != "Quit"):
        file.write(text)
        file.write(" ")
        file.write(' ')

    file.close()
file()
'''
