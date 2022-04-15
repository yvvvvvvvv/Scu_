##1
x={'飯糰':39,'飲料':15,'零食':25}
y=dict(飯糰=39,飲料=20,零食=25)
##2
z=dict(筆=12)
x.update(z)
##3
a=0
for key,value in x.items():
  if value<20 or value>30:
    print(key)
    a+=1
print('總數=',a)