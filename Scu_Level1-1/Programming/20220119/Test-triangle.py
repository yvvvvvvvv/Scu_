x=eval(input('高度:'))
for i in range(x):
    for j in range(x-i-1):
        print(' ',end='')
    for h in range(i+1,0,-1):
        print(h,end='')
    for k in range(2,i+2):
        print(k,end='')
    print( '\n',end='')