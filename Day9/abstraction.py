'''
Abstraction: Hiding the internal impleentation and showing only functionality to the end user. ##half the time we use it to hide some things from the developers

Abstract Method: If a method/function consists of only declaration, not definition

Abstract class: Class that consists of at least one abstract method

Concrete Class:
    It consists of zero(0) abstract method

abc: Module
ABC: Abstract base class
'''

from abc import ABC, abstractmethod

class ATM(ABC):     #abstract class
    @abstractmethod
    def generate_pin(self):
        pass

    @abstractmethod
    def forget_pin(self):
        pass

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass
    @abstractmethod
    def deposit(self):
        pass

class SBI_ATM(ATM): #Concrete class
    def generate_pin(self):
        print('It is used to generate ATM pin!')
        # return super().generate_pin()
    def forget_pin(self):
        print('Not able to remember the pin, forget now')
    def check_balance(self):
        # return super().check_balance()
        print('No balance in your account')
    def deposit(self):
        # return super().deposit()
        print('save your money by giving it to me')
    def withdraw(self):
        # return super().withdraw()
        print("Don't withdraw money!")

obj=SBI_ATM()
obj.generate_pin()
obj.forget_pin()
obj.check_balance()
obj.deposit()
obj.withdraw()