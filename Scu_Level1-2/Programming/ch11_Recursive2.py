#Palindrome
def P(s):
    if len(s)<=1: ##終止
        return True
    elif s[0] != s[len(s)-1]: ##判定非回文
        return False
    else:
        return P(s[1:len(s)-1]) ##遞迴呼叫

while True:
    s=input('請輸入單詞:')
    if P(s):
        print('%s是回文字串'%s)
    else:
        print('%s不是回文字串'%s)
    re=input('是否繼續輸入字串? y(是)輸入其他內容結束:')
    if re!='y':
        break

#2
a=input('Enter a string:')
b=a[::-1]

if a==b:
    print('Yes')
else:
    print('No')