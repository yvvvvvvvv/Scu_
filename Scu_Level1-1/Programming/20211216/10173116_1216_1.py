x=['Curry','Jordan','James','Durant','Obama','Kevin','Lin']
print('目前有的球員',x)
y=int(input('請輸入要顯示的人數:'))
if y>len(x):y=len(x)
w=1
for z in x:
    if w<=y:
        print(z,end=' ')
        w+=1
    else:
        break