x=384400/250
y=divmod(x,60)
a,b=y
z=divmod(a,24)
s,n=z 
h=int(b)
t=int(n)
f=int(s)
print('總共需要%d天和%d小時%d分鐘'%(f,t,h))
