x1=float(input("Enter the value of x1 : "))
y1=float(input("Enter the value of y1 : "))
x2=float(input("Enter the value of x2 : "))
y2=float(input("Enter the value of y2 : "))
x3=float(input("Enter the value of x3 : "))
y3=float(input("Enter the value of y3 : "))
area=(1/2)*((x1*(y2-y3))+(x2*(y3-y1))+(x3*(y1-y2)))
if area==0:
    print("Points are collinear")
else:
    print("Points are not collinear")