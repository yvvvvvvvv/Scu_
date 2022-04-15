for i in range(8):
    for j in range(4):
        if i%2==0:
            j=' 2'
            print(j,end='')
        else:
            j='2 '
            print(j,end='')
    print()



for a in range(8):
    for b in range(8):
        if a%2==0:
            if b%2==0:
                print(' ',end='')
            else:
                print('Y',end='')
        else:
            if b%2==0:
                print('Y',end='') 
            else:
                print(' ',end='')
    print()