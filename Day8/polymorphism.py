#polymorphism
#
#in python we can't perform method overloading, only mmethod overriding

class Temp:
    def sum(self,a,b):
        print(a+b)

    add_two_nums=sum #monkey patching

    def sum(self,a,b,c):#python will take the latest function definition.
        print(a+b+c)
obj=Temp()
# obj.sum(10,20) #will display error asking for a missing third argument.This is solved by monkey patching
obj.sum(10,20,30)
obj.add_two_nums(10,20)