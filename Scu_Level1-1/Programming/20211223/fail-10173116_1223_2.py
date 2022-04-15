buyers=[['James',1030],['Curry',893],['Durant',2050],['Jordan',990],['David',2110]]
a=[]
b=[]
x=0,1,2,3,4
s=int(buyers[x][1])
while True:
    if s>=1000:
        a.append(buyers[x])
        break
    else:
        b.append(buyers[x])
        continue