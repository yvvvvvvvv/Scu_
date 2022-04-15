x=100
print('x=/%6d/'%x)
#/%nd/是給的空間(位數)
y=10.5
print('y=/%6.2f/'%y)
#/%m.nf/是從m個空間中保留兩個小數點位數*小數點算一個位子
s='deep'
print('s=/%6s/'%s)
#注意/%/的d or f or s
print('以下是保留空間不足的例子')
print('x=/%2d/'%x)
print('y=/%3.2f/'%y)
print('s=/%2s/'%s)
#這些例子都沒有刪減
#靠左靠右
print('x=/%-6d/'%x)
print('x=/%+6d/'%x)
#加-靠左 加+依舊靠右但加了+在前面*+占一格
print('y=/%+6.2f/'%y)
print('y=/%-6.2f/'%y)
print('s=/%+6s/'%s)
print('s=/%-6s/'%s)
#%s的加+沒影響
#%m.ns表示共m個空間 只要n個
i='abcdefg'
print('y=/%8s/'%i)
print('y=/%8.3s/'%i)
