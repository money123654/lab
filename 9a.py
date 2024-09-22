from math import *
x=int(input("Enter the x coordinate : "))
y=int(input("Enter the y coordinate : "))
x1=int(input("Enter the x1 coordinate : "))
y1=int(input("Enter the y1 coordinate : "))
r=int(input("Enter the radius of circle : "))
res=sqrt(((x1-x)**2)+((y1-y)**2))
if res==r:
    print("Point lies on circumference of circle")
elif res>r:
    print("Point lies outside the circle")
else:
    print("Point lies inside the circle")