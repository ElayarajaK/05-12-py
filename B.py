from abc import ABC, abstractmethod
from unicodedata import name


class Bank(ABC):
    @abstractmethod
    def balance(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
    @abstractmethod
    def deposit(self):
        pass

class ICICI(Bank):
    def balance(self):
        print("ICICI Bank Accout Balance ");
    def deposit(self):
        print("ICICI Bank Accout deposit ");
       
    def withdraw(self):
        print("ICICI with drowing..")
class IND(Bank):
    def balance(self):
        print("ind Bank Accout Balance ");
    def deposit(self):
        print("ind Bank Accout deposit ");
       
    def withdraw(self):
        print("ind with drowing..")
bank = input("eneter the bank");

obj1=  globals()[bank];

obj1.withdraw(None);


class A:
    def __init__(self,name):
        self.name=name;
class B(A):
    def printval():
        print(name)

