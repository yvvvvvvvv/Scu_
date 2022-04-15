x=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
y=int(input('請輸入天數:'))
i=y%7
if i==0:
    z=x[6]
elif i==1:
    z=x[0]
elif i==2:
    z=x[1]
elif i==3:
    z=x[2]
elif i==4:
    z=x[3]
elif i==5:
    z=x[4]
else:
    z=x[5]
print('%d天後是%s'%(y,z))
