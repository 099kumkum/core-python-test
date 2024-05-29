
import threading


class Hi(threading.Thread):
    def run(self):
        for i in range(5):
            print("Hi", i)


t1 = Hi()
t1.start()
