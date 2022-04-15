import math
#math.radians(x)轉成弧度 .acos .sin .cos ()放弧度
a=input("請輸入地點一:")
b=input('請輸入地點二:')
(x1,y1),(x2,y2)=eval(input('請輸入兩個地點(x1,y1),(x2,y2):'))
x1=math.radians(x1)
y1=math.radians(y1)
x2=math.radians(x2)
y2=math.radians(y2)
distance=6371*math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))
print("%s到%s的距離"%(a,b),"是%f公里"%distance)
