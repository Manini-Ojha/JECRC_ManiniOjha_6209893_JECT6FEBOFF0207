'''
File-> a container that stores data

How do you identify what's present inside a file? File extensions.

Handling->managing the file

Before handling a file, we should have the permisiion to access it.
the following functions will give you access:-

    open():

        var_name=open('FileName.ext'/'absolute_path','mode')

    close():

        var_name.close()
'''



'''
Types of Modes:

1. Read(r):reading a file, can't perform any changes
    a) only read(r)
    b) read+write(r+)
    c) read binary(rb)
    d) read+write binary(rb+)

2. Write(w):overwrites a file,  creates a new file if file doesn't exist
    a) only write(w)
    b) write+read(w+)
    c) write binary(wb)
    d) write+read binary(wb+)

3. Append(a):appends to the text in file
    a) only append(a)
    b) append+read(a+)
    c) append binary(ab)
    d) append+read binary(ab+)

'''


'''
For write operation:
    1. write(str_data)->single line of data
    2. writelines([line1,line2,....])->multiple line of data

'''
