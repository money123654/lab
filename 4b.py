n=int(input("Enter the number : "))
m=n
while n%2==0:
    n=n/2
while n%3==0:
    n=n/3
while n%5==0:
    f=n/5
if n==1:
    print(m," is an ugly number")
else:
    print(m," is not an ugly number")