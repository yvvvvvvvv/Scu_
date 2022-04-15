x=['cat','monkey','bird']
print('原本的字串',x)
for y in x[:]:
    if len(y)>4:
        x.insert(0,y)
        print('新增後的字串',x)
