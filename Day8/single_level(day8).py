'''
Inheritance reduces the cost of an application
'''

#types of inheritence
'''
1.Single Level,
2.Multi-level,
3.Multiple
4.Hierarchial
5.Hybrid
'''

#1.Single level
#we will have a single parent and child class. The properties will be derived only once

#super class: class from which we derive the properties
class Parent:
    bank_balance='54L'

    #parent class constructor
    def __init__ (self,*members):
        self.members=members

    def desc(self):
        print('I am the parent class')
#sub class: class to which we derive the properties
class Child(Parent):
    #constructor chain
    #child class constructor
    def __init__(self, child_name,*args):
        super().__init__(*args) ##parent class's constructor called
        self.child_name=child_name

    #method chaining
    def display(self):
        super().desc()#parent class's method called

obj=Child('Mani','Mom','Dad')
print(obj.bank_balance)
obj.desc()
print(obj.members)
print(obj.child_name)
obj.display()

#constructor chaining:calling parent class's constructor from inside child class's constructor is known as constructor chaining.

#method chaining:calling 