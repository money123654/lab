from math import *
n=int(input("Enter the number of lines : "))
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        print((factorial(i)//(factorial(i-j)*factorial(j))),end=" ")
    print()