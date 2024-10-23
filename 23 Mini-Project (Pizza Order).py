#pizza order project
print("welcomw to pizza shop")

pizzas={'1.chicken peri peri':250.00,'2.BBQ chicken':350.00,'3.chicken sausage':300.00,'4.chicken cheese':350.00,'5.tandoori chicken':400.00}

pizzaprices={1:250.00,2:350.00,3:300.00,4:350.00,5:400}

pizzaname={1:"chicken peri peri",2:"BBQ chicken",3:"chicken sausage",4:"chicken cheese",5:"tandoori chicken"}

print(pizzas)

def calprice(pn,q):
    price=pizzaprices[pn]*q
    return price

print("---------ordering screen----------")

totalbill=0
while True:
    pno=int(input("enter pizza number"))
    qn=int(input("enter quantity"))
    pr=calprice(pno,qn)
    print('price of'+str(qn)+''+pizzaname[pno]+'pizza is'+str(pr)) #concating
    print('---------------')
    print("amount is",pr)

    totalbill=totalbill+pr
    print("----------------")
    print("your payable amt",totalbill)
    print("---thankyou---")
    ans=input("do you want to order anymore")
    if(ans.lower()!='y'):
        break