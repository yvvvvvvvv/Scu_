#x1=(x2+1)*2
#x=int(input('桃子:'))
y=1
a=10
while True:
    if a!=1:
        y=(y+1)*2
        a-=1
        print('第%d天，桃子數%d'%(a,y))
    else:
        break