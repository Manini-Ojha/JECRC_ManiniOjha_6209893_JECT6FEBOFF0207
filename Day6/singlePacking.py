#create a function which can take n no. of int/float and returns only their addition
def add_nums(*args):
    print(args,type(args))
    sum=0
    for i in args:
        sum+=i
    print(f'addition:{sum}')

add_nums()

add_nums(1,2,3,4,5,1.9,98.2,1)
