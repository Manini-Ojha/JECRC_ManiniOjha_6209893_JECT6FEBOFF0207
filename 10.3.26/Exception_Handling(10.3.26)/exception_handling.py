'''
Exception: 
    -> Unauthorized event
    -> Flow of execution of the program will be stopped
    -> After it occurs, it won't execute the rest of the function code

    Types of Errors/Exceptions:

    *SyntaxError is the only exception that can't be handled(it is caused by things like typos or unclosed brackets, etc)

    Methods to Handle Exceptions:

        1.Specific Exception Handling
        2.Generic Exception Handling
        3.Default Exception Handling
    
    Important Keywords(blocks):

    =>try: Here we put the problem statement(aka a block of code due to which we might come across an error)
    =>except:(python doesn't have catch but has except) resolution of the error is written here.
    =>finally:executes regardless, Forcefully executing a block of code after getting an error/resolution
    =>else:changes control to the else block after encountering an error in try block(so error will get ignored). It is an alternative of try block.
    If we find out any error inside try block, interpreter will move forward towards else block.(if code is correct->output)(if code is incorrect->Error)

    purple/pink-exception
    red-Error
    purple-warning

    *we can use raise keyword to raise an error in a program(there are further three ways to raise an error)
'''




'''
1. Specific Exception Handling: 

    -->Handling a particular exception
    -->If we are aware of the error that might get thrown, we can go with specific exception handling

    Syntax:

    try:
        problem
        statement
    except ErrorName:
        resolution/solution code

'''
#ZeroDivisionError
n1,n2=21,0
try:
    result=n1/n2
    print(result)
except ZeroDivisionError:
    print("Please don't choose 0 as the second number")

# ValueError
try:
    a,b,c=1,2
except ValueError:
    print('For formorning MVC, no. of variables should be equal to no. of values!')

# print(a,b,c) #throws Name Error
try:
    print(a,b,c)
except NameError:
    print('Identifiers are not there in memoryy')



'''
2. Generic Exception Handling:
    -->don't need to know any child class names, only parent class name (Exception)
    -->reduces manual labour
'''
try:
    a,b,c=1,2
except Exception:
    print('For formorning MVC, no. of variables should be equal to no. of values!')
try:
    print(a,b,c)
except Exception:
    print('Identifiers are not there in memoryy')

#This won't work for KeyboardInterrupts or infinite loops

# try:
#     while True:
#         print('')
# except Exception:
#     print("You're enetering an infinite loop!!")


'''
3.Default Exception Handling
    -->we can simply use the except keyword, it's a kind of generic exception handling that handles all errors including keywordInterrupt but not syntax error
'''

try:
    while(True):
        print(' ')
except:
    print("Yeah my bad, went into an infinite loop lol")