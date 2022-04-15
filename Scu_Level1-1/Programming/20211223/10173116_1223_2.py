l=[['James',1030],['Curry',893],['Durant',2050],['Jordan',990],['David',2110]]
k = []
index = 0
while index < len(l):
    if l[index][1] >= 1000:
        k.append(l[index])
        l.remove(l[index])
        
    else:
        continue
    index = index+1
print("VIP買家資料:", k)
print("GOLD買家資料", l)