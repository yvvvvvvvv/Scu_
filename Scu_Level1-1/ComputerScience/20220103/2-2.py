n=eval(input("請輸入三角形的高度:")) 
for i in range(n):
    for a in range(n-i-1):
        print(" ",end="")
    for b in range(i+1,0,-1): 
        print(b,end='')
    for c in range(2,i+2):
        print(c,end='')
    print("\n", end="")
        