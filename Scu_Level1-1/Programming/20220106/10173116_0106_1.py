x=[5,6,8,9,15,17,20]
y=[]
z=[]
for x1 in x[:]:
  y.append(x1)
#print(sum(y)) 80
a=round(sum(y)/len(x),2) #11.43
print('平均是:',a)

for x2 in x[:]:
  g=(x2-a)**2
  z.append(g)
#print(sum(z)) 205.71428571428572
b=round(sum(z)/(len(x)-1),2) #34.29
print('變異數:',b)

c=round(b**0.5,2) #5.86
print('標準差:',c)