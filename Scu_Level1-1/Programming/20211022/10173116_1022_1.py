a=int(input('請輸入要兌換的金額:'))
b=divmod(a,100)
(x,y)=b
c=divmod(y,50)
(z,u)=c
d=divmod(u,10)
(i,j)=d
print('共兌換的百元鈔{}張，50元硬幣{}個，10元硬幣{}個'.format(x,z,i))
