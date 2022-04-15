x=int(input('請輸入西元年:'))
if((x%400==0)or(x%4==0 and x%100!=0)):
    print('%d年是閏年'%x)
else:
    print('%d年不是閏年'%x)
