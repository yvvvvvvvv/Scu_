a=[80,100,90,95]
b=[100,93,75,80]
c=[65,87,70,77]
x={'A':a,'B':b,'C':c}
##1
for key,val in x.items():
  x1=sum(val)/4
  print(x1)
##2
for i in (a,b,c):
    print(sum(i)/4)