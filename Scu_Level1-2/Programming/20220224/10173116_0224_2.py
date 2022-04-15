fruits={'西瓜':15,'香蕉':20,'水蜜桃':25}
print('舊內容:',fruits)
while True:
    a=input('請輸入欲刪除之項目(q或Q結束):')
    if a=='q' or a=='Q':
        break
    elif a not in fruits:
        print('dose not exist!')
    else:
        fruits.pop(a)
        print('新內容:',fruits)
    