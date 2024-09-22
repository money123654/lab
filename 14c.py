s="14,625,498.002"
st=""
for i in s:
    if i.isdigit():
        st=st+i
    elif i==',':
        st=st+'.'
    elif i=='.':
        st=st+','
print(st)