import csv
from datetime import date

file=open('expense.csv','a+',newline='')
# w=csv.writer(file)
# w.writerow(['DATE','CATEGORY','AMOUNT'])
# w.writerows(
#     [
#         [date.today(),'Travel',2000],
#         [date.today(),'Food',550],
#         [date.today(),'Entertainment',1700],
#     ]
# )

r=csv.reader(file)
file.seek(0)
print(list(r))
file.close()