N=int(input('請輸入欲排序的數字個數:'))
a=int(input('請輸入整數值域最小值:'))
b=int(input('請輸入整數值域最大值:'))
z=[]
j=[]
import random
for o in range(N):
  x=random.randint(a,b)
  z.append(x)
print('隨機產生之數列為:',z)
