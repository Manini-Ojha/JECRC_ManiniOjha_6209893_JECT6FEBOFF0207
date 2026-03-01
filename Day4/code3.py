#WAP to check whether aa year is leap year or not
year=int(input("enter a year"))
if(year%4==0 and year%100!=0):
    print("leap!")
elif(year%400==0):
    print("leap!")
else:
    print("Nope, not whimsy enough") 
