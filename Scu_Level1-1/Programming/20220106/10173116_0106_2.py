a=[]
b=[]
for x in range(1,100,2):
  a.append(x) 
##A=set(range(1,100,2))
for x1 in range(0,101,5):
  b.append(x1)
##B=set(range(0,101,5))
m=set(a)
n=set(b)
c=m&n
print('intersection=',c)
d=m|n
print('union=',d)
e=m-n
print('A-B difference=',e)
f=n-m
print('B-A difference=',f)