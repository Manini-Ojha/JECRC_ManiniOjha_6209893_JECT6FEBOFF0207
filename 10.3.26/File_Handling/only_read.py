file=open('temp.txt','r')

'''
1. read() : display file content as is
2. readline() : read data line by line
3. readlines() : 

'''
print(file.readline())
file.seek(0)
print(file.read())
file.seek(0)
print(file.readlines())
