n=int(input("Enter the no. of students : "))
di={}
for i in range(n):
    usn=input("Enter the usn : ")
    di.setdefault(usn,{})
    di1={}
    for i in range(3):
        a=input("Enter the  subject name: ")
        b=int(input("Enter the marks of subject : "))
        di1[a]=b
    di[usn]=di1
print(di)
for i in di:
    