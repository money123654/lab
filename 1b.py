n=int(input("Enter the no. of lines to print : "))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ",sep=" ")
    print()
