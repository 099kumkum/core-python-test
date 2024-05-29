'''
import pickle


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


e = Employee('Kumkum', 'Bhadoriya')
f = open("C:/Users/hp/Desktop/Test/Serialization.txt", "wb")
pickle.dump(e, f)
f.close()

f = open("C:/Users/hp/Desktop/Test/Serialization.txt", "rb")
e = pickle.load(f)
f.close()
print("Employee name is", e.fname, e.lname)


'''