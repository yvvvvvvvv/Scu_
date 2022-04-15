#list 串列 中括號[]
#sc=[[a],[b]] sc[0]=[a] sc[1]=[b]
james=[23,19,22,31,18]
print('列印james串列',james)
James=['james',23,19,22,31,18]
print('列印James串列',James)
fruits=['apple','banana','orange']
print('列印fruits串列',fruits)
print(type(fruits))
print('fruits的type',type(fruits))
#print('james第一場成績',james[0]) 以此類推
#另一種 
game1,game2,game3,game4,game5=james
print('james各場次得分',game1,game2,game3,game4,game5)
#list 裡面可以放list 
m=[[23,10],19,22,31,18]
print('james第一場失分',m[0][1])
#m[0][1] list m 的0的位置裡的1的位置的元素
