x=[[16,77],[25,85],[12,8],[36,52]]
a=0
big=-1
for ilist in x:
  for i in ilist:
    big+=1
    if i>a:
      a=i
  x[big]=a
print[x]