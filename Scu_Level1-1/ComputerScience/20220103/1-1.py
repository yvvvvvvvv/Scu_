N=int(input('請輸入欲排序的數字個數:'))
a=int(input('請4輸入整數值域最小值:'))
b=int(input('請輸入整數值域最大值:'))
z=[]
j=[]
import random
for o in range(N):
  x=random.randint(a,b)
  z.append(x)
print('隨機產生之數列為:',z)

s=0
for h in z[:]:
  if h>s:
    s=h
while True:
  if z!=[]:
    min=s+1
    print(min)
    for l in z[:]:
      if l<min:
        min=l
    j.append(min)
    z.remove(min)
  else:
    break
print('排序後之數列為:',j)