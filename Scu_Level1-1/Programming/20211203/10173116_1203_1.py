x='鼠 牛 虎 兔 龍 蛇 馬 羊 猴 雞 狗 豬'
y=x.split(' ')
z=int(input('請輸入出生年:'))
i=z%12
if i==1:
    print(y[9])
elif i==2:
    print(y[10])
elif i==3:
    print(y[11])
elif i==4:
    print(y[12])
elif i==5:
    print(y[1])
elif i==6:
    print(y[2])
elif i==7:
    print(y[3])
elif i==8:
    print(y[4])
elif i==9:
    print(y[5])
elif i==10:
    print(y[6])
elif i==11:
    print(y[7])
else:
    print(y[8])
