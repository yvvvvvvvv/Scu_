x=int(input('請輸入今年的大學學費，不得超過10萬:'))
y=0
while True:
    if x<100000:
        x=int(x*1.05)
        y+=1
    elif x>=100000 and y>0:
        print('%d年後，學費會達到或超過十萬'%y)
        break
    else:
        x=int(input('請請重新輸入今年的大學學費，不得超過10萬:'))
        continue