#len() 抓個數
x=[1,2,3,4,5,6,7,8,9,10]
x1=len(x[1:6])
print('經過%d場比賽 總分='%x1,sum(x[1:6]))
#% format 後面依舊可以直接加,sum()之類的函數 老師說它很聰明

a,*b,c=1,2,3,4,5
print(a)
print(b)
print(c)
#醬