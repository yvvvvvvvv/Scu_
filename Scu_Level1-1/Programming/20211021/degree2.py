a=int(input('請輸入攝氏溫度:'))
華氏溫度=int(a*(9/5)+32)
print('攝氏 {} 等於華氏 {}'.format(a,華氏溫度))
x1=open('degree2.txt',mode='w')
print('攝氏 {} 等於華氏 {}'.format(a,華氏溫度),file=x1)
