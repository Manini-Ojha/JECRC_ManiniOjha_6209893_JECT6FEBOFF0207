#acheive the following output
#input: RAhul@123Gh
#output:raHUL@123gH

#Restriction: can't use inbuilt functions

str=input("enter a string with numbers,alphabets and special characters")
ans=""
for i in str:
    if('a'<=i<='z' or 'A'<=i<='Z'):
        if('a'<=i<='z'):
            ans+=chr(ord(i)-32)
        elif('A' <= i<='Z'):
            ans+=chr(ord(i)+32)
    else:
        ans+=i
print(ans)
