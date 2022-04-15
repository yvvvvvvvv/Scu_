x=eval(input('半邊層次:'))
for i in range(x):
    for j in range(x-i-1):
        print(' ',end='')
    for k in range(2*(i+1)-1):
        print('*',end='')
    print('\n',end='')
for l in range(x-1):
    for f in range(l+1):
        print(' ',end='')
    for c in range(2*(x-(l+1))-1):
        print('*',end='')
    print('\n',end='')