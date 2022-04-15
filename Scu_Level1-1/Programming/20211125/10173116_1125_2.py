x=input('請輸入欲搜尋的車名:')
x1=x.strip()
cars=['toyota','nissan','honda']

if x1 in cars:
    i=cars.index(x1)
    print('所搜尋元素{} 第一次出現位置索引是{}'.format(x,i))
else:
    print('沒有此車名')