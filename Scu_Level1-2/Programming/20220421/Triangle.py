def triangle(n):
    x=[]
    for i in range(n):
        if i==0:
            x.append([1])
        elif i==1:
            x.append([1,1])
        else:
            y=[]
            for j in range(i+1):
                if j==0 or j==i:
                    y.append(1)
                else:
                    y.append(x[i-1][j]+x[i-1][j-1])
            x.append(y)
    return x

n=int(input('請輸入數字:'))
s=triangle(n)
for i in range(len(s)):
    a=str(s[i])
    print(a.center(n*10))