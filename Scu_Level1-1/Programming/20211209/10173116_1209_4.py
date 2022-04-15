x=int(input('請輸入本金:'))
y=int(input('請輸入欲貸款的年份:'))
for z in range(1,y+1):
    x*=(1+0.015)
    print('第%d年本金為:'%z,int(x))