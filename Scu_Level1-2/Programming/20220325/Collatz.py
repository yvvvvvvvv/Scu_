def c(e):
  while True:
    if e == 1:
      break
    elif e % 2 == 0:
      e /= 2
      print(int(e))
    else:
      e = e * 3 + 1
      print(int(e))
while True:
  e = int(input('number(0 quit):'))
  if e == 0:
    break
  else:
    c(e)