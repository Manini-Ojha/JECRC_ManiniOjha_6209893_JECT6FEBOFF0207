#WAP in python to take a character from the user and check whether it is vowel, consonant, digit or special character.


#1. take a character as input
#2. Apply the consitions one by one

char=input("enter a character: ")#input in the form of a string
# vowels=['a','A','e','E','i','I','o','O','u','U']
# if char in vowels:
if char in'aAeEiIoOuU':
    print('character is a vowel')
elif char in '0123456789':
    print('character is a digit.')
elif (char>='A' and char<='Z') or(char>='a' and char<='z'):
    print('character is a consonant')
else:
    print('character is a special character')
