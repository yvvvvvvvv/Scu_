print('巨資購物中心')
x = int(input('請選擇功能:1.購物 2.顯示買家資料:'))
y = [['電視', 5000], ['冰箱', 4000], ['洗衣機', 7000], ['電扇', 1000], ['冷氣機', 6000]]
c = [['James', 1030], ['Curry', 893], ['Durant', 2050], ['Jordan', 990],
     ['David', 2110], ['Kevin', 15000], ['Mary', 10050], ['Tom', 8800]]
x1 = []
x2 = []
x3 = []
z = []
if x == 1:
    while True:
        w = input('請輸入購買的商品(q=結束):')
        if w == 'q' or w == 'Q':
            break
        else:
            for i in y[:]:
                if w == i[0]:
                    z.append(i)
                else:
                    continue
    print('購物結束')
    print('今天購買的商品與價格', z)
    a = 0
    for k in z[:]:
        if k == z[0]:
            a = k[1]
        else:
            a += k[1]
    print('所購商品總價',a)
elif x == 2:
  for o in c[:]:
      if o[1] >= 10000:
          x1.append(o)
      elif o[1] >= 1000:
          x2.append(o)
      else:
          x3.append(o)
  print('Infinite買家資料:', x1)
  print('VIP買家資料:', x2)
  print('Gold買家資料:', x3)
