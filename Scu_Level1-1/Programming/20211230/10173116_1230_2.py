x=input('請輸入一串文字:')
y=list(x)
a=0
b=0
c=0
d=0
for i in y[:]:
    if i>'A' and i<'z':
        a+=1
    elif i==' ':
        b+=1
    elif i>'0' and i<'9':
        c+=1
    else:
        d+=1
print('英文字母有%d個，空白有%d個，數字有%d個，其他字元有%d個'%(a,b,c,d))
