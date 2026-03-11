'''
raise->keyword that helps throw an error in between a program

Exception Creation

1.Custom Exception(raise)
2.User-defined Exception(raise)
3.Assertion Exception(assert)

'''



'''
1.Custom Exception:
    We use prebuilt Exception classes according to our requirement.

    raise ValueError('message')
    ValueError:message
'''
num=17
if num>=18:
    print('eligible')
else:
    # raise ValueError('Age should be greater than or equal to 18')
    raise NameError("You're clearly not 18")

'''
2. User Defined Exception
    1. It is a type of exception in which we can create our own exception classes based upon our own requirement. We can also provide names to those classes according to the user

'''
class MyException(Exception):
    pass

raise MyException('This is my exception class!!')


n1,n2=10,0
if n2==0:
    raise MyException('Second number cannot be zero')
else:
    print(n1/n2)


'''
Assertion exception

-->can be created using keyword assert
assert<condition>,print(ERROR)
print(output)

'''

s=input('Enter a string: ')
assert s==s[::-1],print('It is not a palindromic string')
print('It is a palindromic string')