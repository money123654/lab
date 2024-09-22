a=(1,1,1,0)
s=0
for i in range(len(a)-1,-1,-1):
    s+=a[i]*2**i
print(s)