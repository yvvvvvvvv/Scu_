import re
while True:
    d={}
    a=input('文章(單獨輸入*表示結束):')
    if a == '*':
        break
    a1=a.lower()
    out = re.sub(r'[^\w\s]','',a1)
    b=out.split()
    for q in b:
        if q in d:
            d[q]+=1
        else:
            d[q]=1
    print(d)
