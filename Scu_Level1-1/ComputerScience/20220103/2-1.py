n=eval(input("請輸入三角形的高度:")) 
for i in range(n):
    for a in range(n-i-1):
        print(" ",end="")
    for b in range(2*i+1): 
        #if b<n:
         #   print(range(0,2*i+1,-1),end='')
        #else:
         #   print(range(1,2*i+1),end='')
        print("b=",b,",n=",n)
        for w in range(1,n,-1): 
           print (w,end='')
        #for s in range(n):
         #  print(s, end='') 
        #print('1',end='')
    print("\n", end="")
        

#for o in range(2*(n-1)+1):