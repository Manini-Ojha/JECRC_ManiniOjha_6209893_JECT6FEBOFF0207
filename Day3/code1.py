#Write a program to check whether username and password is correct or not, if correct, print login successful else do nothing.
user={
    'username' : 'user123',
    'password' : '*****'
}

un=input('enter username: ')
pd=input('enter password: ')
if(un == user['username'] and pd==user['password']):        #if condition
    print('login sunccessful')                              #statement block/true statement block

#elif can't be used without if condition.

# else:
#     print("incorrect username or pasword")

print("you've reached the end of this program")
