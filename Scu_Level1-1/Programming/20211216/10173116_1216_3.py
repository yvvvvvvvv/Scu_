x=[33,22,41,25,39,43,27,38,40]
print('目前有的分數:',x)
z=list()
for i in x:
    if i<30:
        continue
    z.append(i)
print('有%d場得分超過30分'%len(z))