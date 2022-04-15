x='content'
w=0
for i in x:
    w+=1
    if i=='t':
        break
    else:
        print(i)
print('for break迴圈結束\n迴圈執行了%d次'%w)

w=0
for i in x:
    if i=='t':
        w+=1
        continue
    print(i)
print('for break迴圈結束\n迴圈執行了%d次'%w)

w=0
for i in x:
    if i=='t':
        w+=1
        pass
    print(i)
print('for break迴圈結束\n迴圈執行了%d次'%w)
