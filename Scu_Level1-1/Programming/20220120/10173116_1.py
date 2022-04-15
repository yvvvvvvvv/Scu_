x=['Toyota','Nissan','Honda']
while True:
    y=input('請輸入車名(結束請按q):')
    z=y.strip()
    if z == 'q':
        print('結束工作')
        break
    elif z not in x:
        print('沒有所搜尋的%s車名'%y)
    else:
        c=x.index(z)+1
        print('所搜尋的車名%s 出現在cars的第%d個位置'%(y,c))