#result=eval(expression) expression is string
numberStr=input('請輸入數學公式:')
number=eval(numberStr)
print('計算結果{}'.format(number))
n1,n2,n3=eval(input('input three numbers:'))
average=(n1+n2+n3)/3
print(average)
