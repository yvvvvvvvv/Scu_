#if(int(x)<0):x=abs(x)
#if()成立:(執行內容) 在只有一列的情況下
x=100
x1=0.2*x
x2=0.5*x
x3=0.8*x
a=int(input("請輸入歲數:"))
if(0<=a and a<=2):
    print("不收費")
elif((3<=a and a<=6) or a>=80):
    print('收費是打2折，%d元'%x1)
elif((7<=a and a<=12) or (60<=a and a<=79)):
    print("收費是打5折，%d元"%x2)
elif((13<=a and 18>=a) or (50<=a and 59>=a)):
    print('收費是打8折，%d元'%x3)
else:
    print('收費是原價，%d元'%x)