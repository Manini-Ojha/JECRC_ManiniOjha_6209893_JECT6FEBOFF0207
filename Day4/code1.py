'''
calculate electricity bill based on units consumed
0-100 -> 5rs/unit
101-300 -> 7rs/unit
above 300 -> 10rs/unit
if bill> 5000 then give 5% discount

'''

#take unit from user(int num)
#apply all the conditions and calculate the total bill amount
#check other condition for applying discount

units=int(input("Enter units:"))
amount=0
if units>0:
    if units<=100:
        amount=units*5
    elif units<=300:
        amount=100*5 + (units-100)*7
    else:
        amount=100*5 + 300*7 + (units-400)*10
else:
    print("Invalid units")

if amount>5000:
    amount-=amount*0.05

print(amount)
