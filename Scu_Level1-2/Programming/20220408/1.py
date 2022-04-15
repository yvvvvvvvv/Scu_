x=input('請輸入數字 用逗號分隔:')
y=x.split(',')
y1=list(map(int,y))
print(y1)
a = lambda i : i*5
for i in y1:
    print(a(i))