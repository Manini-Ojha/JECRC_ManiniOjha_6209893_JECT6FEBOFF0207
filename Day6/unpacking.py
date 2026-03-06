#create a function which will take n no. of inputs from the user and return the sum of onl int and floating point numbers. Please make sure user is capable of passing all types of values
def add_nums(*args):
    sum=0
    for i in args:
        if type(i) in (int,float):
            sum+=i
    print(f'addition:{sum}')

add_nums(*eval(input("enter a list of values")))
