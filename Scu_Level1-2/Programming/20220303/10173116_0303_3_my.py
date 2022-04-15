import this
import re
a=input('原始文章:')
a1=a.lower()
out = re.sub(r'[^\w\s]','',a1)
b=out.split()
print(b)
c=set(b)
print(c)
d=list(c)
print(d)
e=[]
f=dict()
for x in range(len(d)):
    e.append(b.count(d[x]))
print(e)
for y in range(len(d)):
    #s=(d[y],e[y])
    r={d[y]:e[y]}
    f.update(r)
print(f)
#my name is my name is yvonne
#g=sorted(f.items(),key=lambda x:x[1],reverse=True)
#print(g)
#for p in range(len(f)):
    