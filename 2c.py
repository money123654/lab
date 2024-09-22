n=int(input("Enter the number to print fibonacci sequence : "))
fib1=0
fib2=1
for i in range(n+1):
    if i==0:
        print(i,end="->")
    elif i==1:
        print(i,end="->")
    else:
        fib3=fib1+fib2
        if i==n:
            print(fib3)
        else:
            print(fib3,end="->")
        fib1=fib2
        fib2=fib3