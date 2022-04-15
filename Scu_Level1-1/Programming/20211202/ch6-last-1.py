#list.count()傳回特定元素內容出現的次數 可為0 
x1='aasiovnsai'
x2=x1.count('a')
print(x2) #3
y1=[1,2,3,4,3,5,2]
print(y1.count(3)) #2
#[1][1]list位置1的list的位置1
list=[['hf','wefe'],'ewrcwxr']
print(list[0][1]) #wefe
#join結合
x=['etc','exw','wcr']
y='\\'
print(y.join(x)) #etc\exw\wcr
#a.extend(b)將串列b分解為元素加入串列a
#startswith() 列出字串的起始文字是否是訂字串
#endswith() 結尾文字
#replace(a,b) 將a字串由b字串取代