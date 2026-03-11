#multi-level inheritance
#propertiies are derived from one class to another class single time in more than one level(properties are derived in a sequential manner)

class Class_1:
    a='class_1'

class Class_2(Class_1):
    b='class_2'

class Class_3(Class_2):
    c='class_3'

class Class_4(Class_3):
    d='class_4'

class Class_5(Class_4):
    e='class_5'

obj=Class_5()
print(obj.a,obj.b,obj.c,obj.d, obj.e)