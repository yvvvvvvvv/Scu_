soldier0={'tag':'red','score':3}
print(soldier0['tag'],'小兵為',soldier0['score'])
x=eval(input('小兵的x座標:'))
y=eval(input('小兵的y座標:'))
print('小兵的x,y舊座標=',x,',',y)
while True:
    speed={'slow':x+1,'medium':x+3,'fast':x+5}
    a=eval(input('請選擇小兵增加的速度(1.slow/2.medium/3.fast/4.結束此程式:'))
    if a==4:
        break
    elif a==1:
        print('小兵的速度是slow')
        x=speed['slow']
        print('小兵的新速度=',x,",",y)
    elif a==2:
        print('小兵的速度是medium')
        x=speed['medium'] 
        print('小兵的新速度=',x,",",y)
    elif a==3:
        print('小兵的速度是fast')
        x=speed['fast'] 
        print('小兵的新速度=',x,",",y)
    else:
        break