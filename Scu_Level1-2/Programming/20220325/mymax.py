def mymax(n1, n2):
  if n1 > n2:
    print(n1,'較大')
  elif n1 < n2:
    print(n2,'較大')
  else:
    print('SAME')

x = int(input('請輸入欲比較之數字一:'))
y = int(input('請輸入欲比較之數字二:'))
mymax(x,y)