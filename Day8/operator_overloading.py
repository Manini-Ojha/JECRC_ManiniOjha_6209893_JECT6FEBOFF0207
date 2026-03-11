class MyDataType:
    def __init__ (self,val):
        self.val=val

    #solving the error by operator overloading
    def __add__(self,ano_obj):      #<------------------------------
        return self.val+ano_obj.val                                #|
obj1=MyDataType(10)                                                #|
obj2=MyDataType(20)                                                #|
print(obj1+obj2) #error: unsupported operand type for + operator ----