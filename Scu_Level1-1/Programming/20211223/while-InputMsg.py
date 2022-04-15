##ctrl+c 可以跳出迴圈
x=True
while x:
    inputMsg=input('msg:')
    if inputMsg!='q':
        print(inputMsg)
    else:
        x=False