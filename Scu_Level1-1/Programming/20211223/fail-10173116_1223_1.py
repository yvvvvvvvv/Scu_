x=True
while x:
    a=int(input('請輸入今年的大學學費，不得超過10萬:'))
    if a>=100000:
        continue
    else:
        x = False
        n=100000/(a*1.05) #懶得想算式了~~~~
        print('%d年後，學費會達到或超過十萬元'%n)