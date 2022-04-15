import random
x=random.randint(1,100)
print(x)
a=0
while True:
  y=int(input('猜1~100之間的數字='))
  if y<1 or y>100:
    y=int(input('請重新輸入1~100之間的數字='))
    a+=1
    if y>x:
      print('請猜小一點')
    elif y<x:
      print('請猜大一點')
    else:
      print('猜對了')
      break
  else:
    a+=1
    if y>x:
      print('請猜小一點')
    elif y<x:
      print('請猜大一點')
    else:
      print('猜對了')
      break
print('共猜了{}次'.format(a))