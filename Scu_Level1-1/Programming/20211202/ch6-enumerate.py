#可以印出索引值 也可設定起始的索引值 記得轉成list再print
d=['uhreth','zrc','fexw']
e=enumerate(d)
print(list(e)) #[(0, 'uhreth'), (1, 'zrc'), (2, 'fexw')]
f=enumerate(d,start=10)
print(list(f)) #[(10, 'uhreth'), (11, 'zrc'), (12, 'fexw')]