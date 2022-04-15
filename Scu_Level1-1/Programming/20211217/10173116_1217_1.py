#6-1
a='1234567890'
print(a[0]+a[-1]+a[0]+a[-4]+'-'+a[2]+a[0]+a[0]+a[5])

#6-2
x='welCOme,everyONE'
#print(x.title()) #Welcome,Everyone
y=x.split(',')
print(y[0].title()+','+y[1].lower()) #Welcome,everyone

#6-3
a=[[1,2,3,4,5],[6,7,8,9,10]]
print(a[1][4])
print(a[-1][-3])