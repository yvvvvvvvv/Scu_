x=input('請輸入五個城市並用,做區隔:')
x1=x.split(',')
print(x1)
x1.append('London')
print(x1)
x1.insert(3,'Xian')
print(x1)
y=input('請輸入欲刪除的城市:')
if y in x1:
    x1.remove(y)
    print(x1)
else:
    print('所輸入城市不在表中')