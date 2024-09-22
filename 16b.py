s=input("Enter the string : ")
n=int(input("Enter the size : "))
n=n%len(s)
a=s[n::]+s[:n:]
b=s[len(s)-n::]+s[:len(s)-n:]
print("Clockwise rotation : ",a)
print("Anti clockwise rotation : ",b)