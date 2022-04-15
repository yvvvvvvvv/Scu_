x=list(eval(input("請輸入數字串:")))
act=int(input('請輸入1表小到大排列2表大到小(則一):'))
y=[]
z=[]
a=True

def swap1(x):
    while a:
        if x != []:
            max=0
            for i in x[:]:
                if i > max:
                    max = i
            y.append(max)
            x.remove(max)
        else:
            break

def swap2(x):
    b=0
    for i in x[:]:
        if i > b:
            b = i
    while a:
        if x != []:
            min=b+1
            for i in x[:]:
                if i < min:
                    min = i
            z.append(min)
            x.remove(min)
        else:
            break

if act==1:
    swap2(x)
    print(z)
else:
    swap1(x)
    print(y)