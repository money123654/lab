def check_habit(n):
    for i in range(n):
        m=(3*(2**i))-1
        if m==n:
            return True
    else:
        return False
n=int(input("Enter the number : "))
print(check_habit(n))