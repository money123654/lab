n=int(input("Enter the number : "))
prod=n
while(True):
    y=int(input("Enter the number : "))
    if y!=-1:
        prod=prod*y
    else:
        break
print(prod)