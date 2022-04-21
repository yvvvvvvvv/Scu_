def H(n , A, B, C):
    if n==1:
        print("Disk 1 from",A,"to",B)
        return 
    H(n-1, A, C, B)
    print("Disk",n,"from",A,"to",B)
    H(n-1, C, B, A)


while True:
    n=input('請輸入整數(輸入y 來結束）：')
    if n=='y':
        break
    else:
        n=int(n)     
        H(n,'A','B','C')