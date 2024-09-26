class triangle:
    def __init__(self,x,y):
        self.l=x
        self.b=y
    def __gt__(self,t1):
        if 0.5*self.l*self.b>0.5*t1.l*t1.b:
            return "Area of t1 is greater than t2"
        else:
            return "Area of t2 is greater than t1"

a=int(input("Enter the l1:"))
b=int(input("Enter the b1:"))
t=triangle(a,b)
c=int(input("Enter the l2:"))
d=int(input("Enter the b2:"))
t1=triangle(c,d)
j=t>t1
print(j)