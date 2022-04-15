x=['94','82','60','91','88','79','61','93','99','77']
p=sorted(x,reverse=True)
y=int(input('請輸入要顯示最高分錢幾個的成績:'))
for i in range(len(x)):
    if i == y:
        break
    else:
        print(p[i],end=' ')
        