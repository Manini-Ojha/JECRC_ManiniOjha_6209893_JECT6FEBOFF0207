file=open('temp.txt','w+')
# file.write('Mein ninja Hatori aa gaya hu')

file.writelines([
    'whatchu know about me\n',
    'whatchu\n',
    'whatchu know bout me\n'
])

file.seek(0)    #moves pointer to the start of the file(or at a specific index)
print(file.read())

file.close()

