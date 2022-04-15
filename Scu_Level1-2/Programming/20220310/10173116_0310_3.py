def make(type,topping):
    print(type,'冰淇淋加的配料')
    for t in topping:
        print('---',t)
while True:
    a=eval(input('點餐選1,結束選2:'))
    if a == 1:
        b=input('請輸入口味:')
        e=[]
        while True:
            c=eval(input('加料選1,不加了選2:'))
            if c==1:
                d=input('配料:')
                e.append(d)
            elif c==2:
                break
        make(b,e)
    else:
        break