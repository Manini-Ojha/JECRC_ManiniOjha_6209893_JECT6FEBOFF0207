#multiple
#It is a type of inheritance in which the properties will be derived from multiple parent class to a single child class

class Class1:
    a=10

class Class2:
    b=100

class Class3:
    c=1000

class Class4:
    d=10000

class Child(Class1,Class2,Class3,Class4):
    pass

#we can use the child directly to access properties but that doesn't work for methods cause they need self
print(Child.a,Child.b,Child.c,Child.d)