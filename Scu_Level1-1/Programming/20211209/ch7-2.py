n=int(input('請輸入整數:'))
num=list(range(n+1))
total=sum(num)
print('從1到%d的總和是'%n,total)

sum=int() #or sum=0
print(type(sum))
for x in range(0,n+1):
    sum+=x
print('從1到%d的總和是'%n,sum)

x=[n for n in range(6)]
print(x) #[0, 1, 2, 3, 4, 5]