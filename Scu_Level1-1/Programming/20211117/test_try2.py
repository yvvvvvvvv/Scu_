from os import read


x=open('testTry.txt',mode='w')
print('testTry1',file=x)
print('testTry2',file=x)
#w 第二次執行將覆蓋前一次結果
y=open('testTry2.txt',mode='a')
print('testTry1',file=y)
print('testTry2',file=y)
#a 第二次執行結果顯示在第一次結果下方
s=open('testTry2.txt',mode='r',encoding='UTF-8')
z=s.read()
print(z)
x.close()
y.close()
