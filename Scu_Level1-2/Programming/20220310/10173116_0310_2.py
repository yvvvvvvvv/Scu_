uns=[]
s=[]
def kit(uns,s):
    print('廚房處理中...')
    while uns:
        meal=uns.pop()
        print('菜單:',meal)
        s.append(meal)
def unsm(uns):
    print('===尚未服務===')
    if not uns:
        print('***沒有餐點***','\n')
    for x in uns:
        print(x)
def sm(s):
    print('===已服務餐點===')
    if not s:
        print('***沒有餐點***','\n')
    for y in s:
        print(y) 

while True:
    d=eval(input('請輸入要進行的服務:1.餐點服務/2.處理餐點/3.結束點餐:'))
    if d==1:
        a=input('請輸入餐點:(以空格為分隔)')
        uns=a.split(' ')
        print(uns)
    elif d==2:
        unsm(uns)
        sm(s)
        kit(uns,s)
        print('\n','===廚房處理結束===','\n')
        unsm(uns)
        sm(s)
    elif d==3:
        break