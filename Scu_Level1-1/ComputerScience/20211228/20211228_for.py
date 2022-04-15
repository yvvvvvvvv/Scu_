x=[1,3,5,2]
y=[]
xl = len(x)
for g in x[:]:
    max=0
    for i in x[:]:
        if i > max:
            max = i
    y.append(max)
    x.remove(max)


print(y)
print(x)