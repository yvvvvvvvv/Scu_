'''def H(n , A, B, C):
    if n==1:
        print("D 1",A,"->",B)
        return 
    H(n-1, A, C, B)
    print("D",n,A,"->",B)
    H(n-1, C, B, A)'''

def hanoi(n, A, B, C):
    if n == 1:
        print(f"{A}->{C}")
    else:
        hanoi(n-1, A, C, B) 
        hanoi(1, A, B, C) 
        hanoi(n-1, B, A, C)


while True:
    n=input('請輸入整數(輸入y 來結束）：')
    if n=='y':
        break
    else:
        n=int(n)     
        hanoi(n,'A','B','C')