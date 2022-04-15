def a(i):
  if i >= 0 :
    i = i 
  else:
    i = -i
  print('絕對值:%i'%i)

def mymax(n1, n2):
  if n1 > n2:
    print(n1,'較大')
  elif n1 < n2:
    print(n2,'較大')
  else:
    print('SAME')

def reverse():
  s=input("請輸入需要反轉的內容：")
  return s[::-1]


while True:
  e=input('請選擇功能:1.abs 2.較大值 3.reverse 4.結束:')
  if e == '1':
    i = int(input('請輸入數字:'))
    a(i)
  elif e == '2':
    x = int(input('請輸入欲比較之數字一:'))
    y = int(input('請輸入欲比較之數字二:'))
    mymax(x,y)
  elif e == '3':
    a=reverse()
    print(a)
  elif e == '4':
    break
  else:
    print('error')