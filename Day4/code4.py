#ASCII of a=97
#ASCII of A=65
#ASCII a-A=32
#so, a->A = -32
#A->a = +32
#function ord() checks the ASCII value of any character
#funtion chr() checks the character of an ASCII value

#WAP to take a character and covert lowercase to uppercase and vice versa.

ch=input("enter a character: ")
# if(ch not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
#     print(ch)
# else:
ascii=ord(ch)
if(ascii>=97 and ascii<=122):
    ch=ascii-32
    print(chr(ch))
elif(ascii>=65 and ascii<=90):      #we could write an else block here too
    ch=ascii+32
    print(chr(ch))
else:
    print(ch)


#human readable + optimization
#using 'a' instead of 97 and 'z' instead of 122


#ch=input('enter a char')[0]
#if('a'<= ch <= 'z)
#result=chr(ascii-32)
#print(ch)
