#make all the immutable collections as keys, find the middle of all the immutable collections with odd length and put them as the values, otherwise put .

#input: ('Hello','Hi',20,40.2,9.6j,[1,2],'PYTHON','JECRC',(1,2,3))
#output:{'Hello':'l', 'Hi':'Hi','PYTHON':'PN','JECRC':'C',(1,2,3):2}
#take list,tuple,set

tup=eval(input('enter a collection'))
newdict={}
for i in tup:
    if type(i) in [str,tuple]:
        if(len(i)%2==0):
            newdict[i]=i[0]+i[-1]
        else:
            newdict[i]=i[len(i)//2]
print(newdict)
