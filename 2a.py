a=int(input("Enter the 1st integer number : "))
b=int(input("Enter the 2nd integer number : "))
x=input("Enter your choice A or B\n")
if x=='A':
    y=input("Enter your choice + to Add,- to Sub,* to Mul,/ to Div\n")
    if y=='+':
        print("Result : ",a+b)
    elif y=='-':
        print("Result : ",a-b)
    elif y=='*':
        print("Result : ",a*b)
    elif y=='/':
        print("Result : ",a/b)
elif x=='B':
    y=input("Enter your choice & to AND | to OR ^ to EXOR\n")
    if y=='&':
        print("Result : ",a&b)
    elif y=='|':
        print("Result : ",a|b)
    elif y=='^':
        print("Result : ",a^b)