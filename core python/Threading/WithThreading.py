'''
import threading


from WithoutThreading import *

t1 = threading.Thread(target=hello)
t2 = threading.Thread(target=hi)

t1.start()
t2.start()
'''

'''
def hello():
    for i in range(10):
        print("Hello", i)


t1 = threading.Thread(target=hello)


def hello(name):
    for i in range(10):
        print(name, i)


t2 = threading.Thread(target=hello, args=("Kumkum",))
t3 = threading.Thread(target=hello, args=("Priya",))
t1.start()
t2.start()
t3.start()
'''
