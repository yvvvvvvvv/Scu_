x=[1,3,5,2]
y=[]

a=True
while a:
    if x != []:
        max=0
        for i in x[:]:
            if i > max:
                max = i
        y.append(max)
        x.remove(max)
    else:
        break

print(y)
print(x)