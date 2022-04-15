##change the element
CARS=['TO','DFYGI','GBCNFMUES']
print(CARS) #=['TO', 'DFYGI', 'GBCNFMUES']
CARS[1]='tgrufc,h;i'
print(CARS) #=['TO', 'tgrufc,h;i', 'GBCNFMUES']

##append()新增list裡的資料(最後面)
x=[] #一定要記得先宣告x->[]
x.append('hgmlknc')
print(x) #['hgmlknc']
x.append('jgyouigu/l.')
print(x) #['hgmlknc', 'jgyouigu/l.'] 

##insert()可以指定位置新增
y=['dgrvxdg','ytmui','gfnml,.i']
print(y) #['dgrvxdg', 'ytmui', 'gfnml,.i']
y.insert(1,'gmb,lkh')
print(y) #['dgrvxdg', 'gmb,lkh', 'ytmui', 'gfnml,.i']

##.pop()刪除後可以print(list.pop())顯示刪除的資料 pop()括弧內為指定位置
z=['uybtm,;.i','fgohp','wsrdifgko','egdukuyiuh']
print(z)
popped=z.pop(2)
print(z) #['uybtm,;.i', 'fgohp', 'egdukuyiuh']
print(popped) #wsrdifgko
