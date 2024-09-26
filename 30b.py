class shape:
    def area(self):
        pass
    def para(self):
        pass

class circle(shape):
    def __init__(self,x):
        self.r=x
    def area(self):
        return 3.142*self.r*self.r
    def para(self):
        return 2*3.142*self.r
class triangle(shape):
    def __init__(self,x,y,z):
        self.l=x
        self.b=y
        self.h=z
    def area(self):
        return 0.5*self.l*self.b
    def para(self):
        return self.l+self.b+self.h
class square(shape):
    def __init__(self,x):
        self.l=x
    def area(self):
        return self.l*self.l
    def para(self):
        return 4*self.l


s=shape()
r=int(input("Enter the radius : "))
c=circle(r)
print("Area of circle : ",c.area())
print("Parameter of circle",c.para())