
y=[]
while True:
    x = input('請選擇功能:1.建立國家或城市 2.刪除國家或城市(若要結束本功能請按q):')
    if x == 'q' or x == 'Q':
        print('結束所有工作!')
        break
    elif int(x) == 1:
        while True:
            w=input('請輸入欲增加城市(q=結束):')
            if w == 'q' or w == 'Q':
                print('結束新增工作!')
                break
            elif w in y:
                print('已在串列中')
                print(y)
            else:
                y.append(w)
                print(y)
    elif int(x) == 2:
        while True:
            w1 = input('請輸入欲刪除城市(q=結束):')
            if w1 == 'q' or w1 == 'Q':
                print('結束刪除工作!')
                break
            elif w1 not in y:
                print('沒有%s這個城市國家'%w1)
                print(y)
            else:
                y.remove(w1)
                print(y)
    else:
        print('無此選項')
        continue