ans=30
guess=0
while guess!=ans:
    guess=int(input('請輸入0~100之間的數字:'))
    if guess>ans:
        print('請輸入小一點')
    elif guess<ans:
        print('請輸入大一點')
    else:
        print('恭喜你答對了')