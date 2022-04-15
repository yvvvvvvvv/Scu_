##.split() 分割字串 括弧內表示分割物
x='auyhu rdtfmgy rdfimly'
y='crducjn\cdbnckjk\mlerbdfnj'
x1=x.split()
y1=y.split('\\') #\在python 裡是溢出字元 所以要用\表示 -> \\ 前者表示 後者執行
print(x) #auyhu rdtfmgy rdfimly
print(x1) #['auyhu', 'rdtfmgy', 'rdfimly']
print(y) #crducjn\cdbnckjk\mlerbdfnj
print(y1) #['crducjn', 'cdbnckjk', 'mlerbdfnj']
