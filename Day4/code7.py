#input [10,2.2,5,'Hello',[100,200],99.9]
#output 99.9

#WAP to find out the maximum number 

l1=[10,2.2,5,'Hello',[100,200],99.9]
max=l1[0]
for i in l1:
    if(type(i)==type(1) or type(i)==type(1.0)): #type(i) in [int,float]
        if(i>max):
            max=i
print(max)
        
