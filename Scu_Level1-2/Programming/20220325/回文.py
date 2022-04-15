def s(a):
  b = a[::-1] 
  if a == b:
    print ("是")
  else:
    print ("否")

while True:
  a = input("請輸入字串(q結束):")
  if a == 'q':
    break
  else:
    s(a)