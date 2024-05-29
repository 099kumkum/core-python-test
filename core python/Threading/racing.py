from time import sleep
from threading import *
import threading


class Account:
    Balance = 0

    def __init__(self):
        self.lock = threading.Lock()

    def get_balance(self):
        sleep(2)
        return self.Balance

    def set_balance(self, amount):
        sleep(2)
        self.Balance = amount

    def deposite(self, amount):
        self.lock.acquire()
        bal = self.get_balance()
        self.set_balance(bal + amount)
        self.lock.release()


class Racing(Thread):
    account: Account
    name = "no name"

    def __init__(self, account, name):
        super(Racing, self).__init__()

        self.account = account
        self.name = name

    def run(self):
        for i in range(5):
            self.account.deposite(100)
            print(self.name, self.account.get_balance())


def main_task():
    acc = Account()

    t1 = Racing(acc, "Ram")
    t2 = Racing(acc, "Shyam")

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Finish")


main_task()
