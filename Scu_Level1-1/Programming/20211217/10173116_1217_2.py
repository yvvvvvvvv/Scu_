x=['Mary','Josh','Tracy']
print('目前宴會名單：',x)
print('1:新增客人','2:刪除客人')
a=input('請輸入功能：')
b=input('請輸入名字：')
if a=='1':
  x.append(b)
  print('新的宴會名單：',x)
elif a=='2' and b in x:
  x.remove(b)
  print('新的宴會名單：',x)
else:
  print('此人不在名單中')