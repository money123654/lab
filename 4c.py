from datetime import date
x=date.today()
print(x)
a=int(input("Read your birth year : "))
y=x.year
age=y-a
if age>=10 and age<=14:
    print("Kid")
elif age>=15 and age<=18:
    print("teenage")
elif age>=19 and age<=30:
    print("young")
elif age>=31 and age<=60:
    print("middle young")
elif age>=61 and age<=75:
    print("middle old") 
elif age>=76 and age<=90:
    print("old") 
else:
    print("Old and Old") 