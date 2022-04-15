#meow meow meow~~~~~
#la la la~~~~
#ya ya ya~~~~
#i want to g home~~
#carrie~~~
#6-5-2sort
#reverse sort index
x=['a','s','d','f','g']
print('目前串列內容=',x)
#直接列印x[::-1]顛倒排序 不改list內容
#list.reverse() 
#lust.sort() sort預設是由小排到大
#用reverse=ture 反過來
num=[1,3,2,4,5,6]
num.reverse()
print(num) 
num.sort()
print(num)
num.sort(reverse=True) #Ture False 用大寫!!!
print(num)
num.sort(reverse=False)
print(num)

num2=sorted(num)#sorted 更改後的list可以另存新檔(新的變數)
print(num)
#num3=sorted(num,reverse=Ture)

#print(num.sort())仄個不行

a=eval(input())
b=list(a)
print(b)
