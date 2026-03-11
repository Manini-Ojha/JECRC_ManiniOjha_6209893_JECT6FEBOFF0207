'''
lambda(Anonymous Function):
    1.Lambda is a keyword which is used to create anonymous functions
    2.For calling a lambda funtion, we can store the address of lambda inside a variabl. by invoking the var_name, we can call the functions
    3. This function only returns a value, doesn't print it
'''

'''
var-name=lambda args: <exp>
var_name(args) ##Calling the lambda function
'''

#lambda args: <exp>

#WAP to add two numbers
result=lambda a,b: a+b #Returns value
print(result) #prints location of lambda
print(result(1,2))
(lambda a,b: print(a+b))(int(input('First Num: ')), int(input('Sec Num: ')))


#lamda args:<exp-1> if<cond> else <exp_2>

#WAP to find the square of a number if its given

# num=int(input('enter a number: '))
# if num%2==0:
#     print(num**2)

res=lambda num: print(num**2) if num%2 ==0 else None
res(10)
(lambda num: print(num**2) if num%2 ==0 else None)(int(input()))

#WAP to find square for even numbers and cubes for odd numbers

res= lambda numb: print(numb**2) if numb%2==0 else print(numb**3)
res(11)


#check whether a num is positive, negative or zero

# n=int(input())
# if n>0:
#     print('pos')
# elif n<0:
#     print('neg')
# else:
#     print('0')

#lambda has no concept of elif so we implement the above in the followig way:-

# if n>0:
#     print('pos')
# else:
#     if n<0:
#         print('neg')
#     else:
#         print('0')

r=lambda n:print('pos') if n>0 else print('neg') if n<0 else print('0')
r(int(input()))