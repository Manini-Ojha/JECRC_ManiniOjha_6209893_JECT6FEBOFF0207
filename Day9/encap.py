'''
encapsulation: 
1. It is used to provide security to the data(data means variables/properties and methods present in a class)
2. Security is provided by access specifiers(who can access the class members):
    a)private
    b)protected:It is a soft barrier. adult's consent, we won't access it as a mature person.
    c)public: by default all methods and variables in a class will be accessible outside of class
'''

#public
class Temp:
    a,b,*c,d='Hello'#works cause of packing
    def greeting(self):
        print('Good Afternoon user: ')
class C2(Temp):
    pass
obj=C2()
print(obj.greeting())

#protected
class Temp1:
    _a=10   #_ indicates protected variable but it will act as protected 
    _b='I LOVE PYTHON!'

obj1=Temp1()
print(obj1._a)
print(obj1._b)

#private
class Temp2:
    __a=100
    def __status(self):
        print('class name is Temp2!')
obj2=Temp2()
# print(obj2.__a)   #Can't access it, attribute error shows up
# obj2.__status()   #Can't access it, same as above

#how to access them then?
#1. By using Syntax
#2. get and set method
#3. by using @property  decorator(setter)


#1. Syntax
#objName/className._className__propName/methodName (Accessing)
#objname/className._className__memberName (Modifying)

print(Temp2._Temp2__a)
print(obj2._Temp2__a)
obj2._Temp2__status()

obj2._Temp2__a='012356789'


def new_method():
    print('method definition got modified')

obj2._Temp2__status=new_method #assigning new method 
obj2._Temp2__status() 

#2.Get/Set Method

class New:
    __a=100
    def get(self):
        print(self.__a)
    def set(self, new_val):
        self.__a=new_val

o=New()
o.get()
o.set(1)
o.get()
print(o._New__a)

#3. @property decorator
class New2:
    __a=10

    @property
    def get(self):
        print(self.__a)
    @get.setter
    def set(self, new_val):
        self.__a=new_val
ob=New2()
ob.get  #methods act like properties
ob.set=10000 #methods assign like properties too
ob.get
print(ob._New2__a)