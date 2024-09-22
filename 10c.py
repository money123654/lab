s=input("Enter the number in words : ")
a=s.split(' ')
st=""
for i in a:
    if i=='one':
        st=st+'1'
    elif i=='two':
        st=st+'2'
    elif i=='three':
        st=st+'3'
    elif i=='four':
        st=st+'4'
    elif i=='five':
        st=st+'5'
    elif i=='six':
        st=st+'6'
    elif i=='seven':
        st=st+'7'
    elif i=='eight':
        st=st+'8'
    elif i=='nine':
        st=st+'9'
    elif i=='zero':
        st=st+'0'
print("Number in digits : ",st)