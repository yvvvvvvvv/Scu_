x=int(input('請輸入整數:'))
z=[]
#y=list(range(1,x+1))
if x>10:
    x=10
for y in range(1,x+1):
    z.append(y*y)
print(z)