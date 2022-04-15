x=['洪錦魁','洪冰儒','東霞','大成']
y=[]
for z in x[:]:
    if z.startswith('洪'):
        x.remove(z)
        y.append(z)
print('新的串列',x)
print('lastname list',y)