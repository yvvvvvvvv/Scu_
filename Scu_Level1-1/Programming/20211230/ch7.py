print(chr(655))
x='I love python3!'
y=list(x)
a=0
b=0    
c=0
d=0
if y[13]>'A' and y[13]<'z':
    a+=1
elif y[13]==' ':
    b+=1
elif y[13]>'0' and y[13]<'9':
    c+=1
else:
    d+=1
print(a,b,c,d)