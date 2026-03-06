#create a function which will return a list of prime numbers. Please make sure that user can pass n of inputs.For checking whether a number is prime or not, you can create one function.

def isPrime(num):
    if(num<=1):
        return False
    for i in range(2,(num-1)):
        if num%i==0:
            return False
        # else:
        #     return True; #won't work cause we want to run the whole loop
    return True

def find_prime_nums(*args):
    prime=[]
    for i in args:
        if(isPrime(i)):
            prime.append(i)
    return prime

print(find_prime_nums(*eval(input('enter a list of nums'))))