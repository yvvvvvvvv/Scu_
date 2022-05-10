#max,min
a = [1,2,35,9,26,10]
b = [2,26,38,44,2,8]
print(max(a))
print(max(b))
print(min(a))
print(min(b))

#sum
c = [5,10,15,20]
print(sum(c))
print(sum(c,5))

#len
x = 'Hello 理律！' #空格也算喔
y = ['理','律','夏','令','營'] #可以換成數字
z = {1:'理',2:'律',3:'夏',4:'令',5:'營'}

print(len(x))
print(len(y))
print(len(z))

#enumarate
seasons = ['Spring', 'Summer', 'Fall', 'Winter']

a = list(enumerate(seasons))
print(a)
#[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

b = list(enumerate(seasons,start=1)) #下標從1開始
print(b) 
#[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

#sorted
a = [5,7,6,3,4,1,2]
b = sorted(a)  # 保留原列表

print(a) 
#[5, 7, 6, 3, 4, 1, 2]
print(b)
#[1, 2, 3, 4, 5, 6, 7]
 
c = sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
print(c)
#[1, 2, 3, 4, 5]

d = sorted("This is a test string from Andrew".split())
print(d)

e = sorted("This is a test string from Andrew".split(), key=str.lower)
print(e)

#if...else
fine = input('請輸入罰金金額：')

if fine != int and fine != float:
    print('請輸入數字！')
elif fine >= 90 and fine <= 100:
    print('成績：A+')
elif fine >= 80 and fine < 90:
    print('成績：B+')
elif fine >= 70 and fine < 80:
    print('成績：B')
else:
    print('成績：C')

a = [1,2,3,4,5]
b = input('請輸入數字：')
if b not in a:
  print('Not in list!')
else:
  print(b)
  
#forLoop
a = [1,2,3,4,5]
for i in a:
  print(i)

print('   ')

for i in range(5): #從0開始的五個數字
  print(i)

print('   ')

for i in range(2,7): #從2開始到6結束
  print(i)

print('   ')

for i in range(2,11,2): #從2開始，一次加2，到11結束
  print(i)

print('   ')

for i in range(20):
  if i >= 10:
    break
  print(i)

print('   ')

index = 0
for i in range(20):
  if i >= 10: #為什麼沒有10
    continue
  index += 1
print(index)

print('   ')

name = 'LawTech'
for i in name:
  print(i,end='')
print('   ')
for i in name:
  print(i)

print('   ')

#巢狀for-loop
for i in range(1, 10):
    for j in range(1, 10):
        if j == 9:
            print("\t", i*j) # j == 9時，換行
        else:
            print("\t", i*j, end = '') # j < 9時，不換行

print('   ')

#練習題
for i in range(8):
    for j in range(4):
        if i % 2 == 0:
            j = ' Y'
            print(j,end='')
        else:
            j = 'Y '
            print(j,end = '')
    print()
    
#lambda
L=[('b',2),('a',1),('c',3),('d',4)]
sorted(L, cmp=lambda x,y:cmp(x[1],y[1]))   # 利用cmp函数
#[('a', 1), ('b', 2), ('c', 3), ('d', 4)]
sorted(L, key=lambda x:x[1])               # 利用key
#[('a', 1), ('b', 2), ('c', 3), ('d', 4)]

 
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
sorted(students, key=lambda s: s[2])            # 按年龄排序
#[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
 
sorted(students, key=lambda s: s[2], reverse=True)       # 按降序
#[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]


