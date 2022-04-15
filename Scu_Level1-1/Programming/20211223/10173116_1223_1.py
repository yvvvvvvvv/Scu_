x=int(input('請輸入今年的大學學費，不得超過10萬:'))
y=0
total=0
while total<100000:
    if x>=100000:
        x=int(input('請請重新輸入今年的大學學費，不得超過10萬:'))
    y+=1
    total=x*1.05**y
print('%d年後，學費會達到或超過十萬'%y)