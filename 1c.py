s=input("Enter the string : ")
if s.isalpha():
    if s.islower():
        print("Lower case\n")
    elif s.isupper():
        print("Upper case\n")
elif s.isdigit():
    summ=0
    for i in s:
        summ=summ+int(i)
    print("sum of digits : ",summ)
else:
    ss=0
    for i in s:
        if i.isalnum():
            pass
        else:
            ss=ss+1
    print("No. of symbols : ",ss)