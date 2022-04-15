import random
#chr(65-90)
x1=[]
for a in range(65,91):
  x1.append(chr(a))
#print(x1)
x=set(x1)
y=set(random.sample(x,10))
z=set(random.sample(x,10))

b=x-y ##difference
c=x-z
d=b&c ##intersection
print('沒被選到=',d)

e=b^c ##symmetric difference
print('只選到一次=',e)

f=y&z
print('選到兩次=',f)