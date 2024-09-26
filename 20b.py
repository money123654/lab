def dict_str(m):
    k=''
    for i in m:
        k+=i+'-'+str(m[i])+" "
    return k.rstrip()
def str_dict(n):
    l=n.split(' ')
    d={}
    for i in l:
        l1=i.split('-')
        d[l1[0]]=int(l1[1])
    return d
m=eval(input("Enter a dict:"))
print(dict_str(m))
n=(input("enter a string:"))
print(str_dict(n))
