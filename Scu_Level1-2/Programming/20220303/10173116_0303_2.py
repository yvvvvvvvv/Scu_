s=dict()
while True:
    a=input('請輸入姓名　:')
    b=input('夢幻旅遊景點:')
    c=input('是否有人要參加市場調查?(y/n)')
    if c=='n':
        d={a:b}
        s.update(d)
        q=list(s.keys())
        z=list(s.values())
        for w in range(len(s)):
            print(q[w],'夢幻旅遊景點:',z[w])
        break
    elif c=='y':
        d={a:b}
        s.update(d)
    else:
        print('again')