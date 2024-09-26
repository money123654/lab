pr=0
shop={'chair':[10,10000],'sofa-set':[5,60000]}
prod=input("Enter the product name")
q=int(input("enter the quantity"))
for i in shop:
    if i==prod:
        if shop[i][0]>=q:
            print('price:',shop[i][1])
            print('quantity',shop[i][0])
            diff=shop[i][0]-q
            shop[i][0]=diff
            pr=q*shop[i][1]
        else:
            print('not avaliable')
    else:
        print('product not available')
print('profit=',pr)
print(shop)

