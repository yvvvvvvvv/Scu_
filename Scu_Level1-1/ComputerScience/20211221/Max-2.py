x=[16,77,25,85,12,8,36,52]
##第一行可改成
##for z in x:
##if len(x)%2==1:break
for i in range(len(x)-1):
  for a in range(0,len(x)-1,2):
    if x[a]>=x[a+1]:
      x.append(x[a])
    else:
      x.append(x[a+1])
print(x[-1])