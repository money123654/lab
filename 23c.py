class shop:
    def __init__(self):
        self.scart=[]
    def insert_item(self,x,y):
        self.scart.append([x,y])
        print("Tem added to cart")
    def remove_item(self,x):
        for i in self.scart:
            if x==i[0]:
                self.scart.remove(i)
                print("Item removed from cart")
            else:
                print("Item doesn't exist in cart")
    def get_price(self):
        p=0
        for i in self.scart:
            p+=int(i[1])
        return p

s=shop()
g=0
while True:
    ch=input("Enter your choice add remove price : ")
    if ch=="add":
        s.insert_item(input("Enter product name : "),input("Enter product price : "))
    elif ch=="remove":
        s.remove_item(input("Enter product name : "))
    elif ch=="price":
        g=s.get_price()
        print("price : ",g)
    else:
        break     

