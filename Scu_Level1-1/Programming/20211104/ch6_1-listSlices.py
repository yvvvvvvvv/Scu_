#name_list[start:end] 讀取從索引start到(end-1)索引的串列元素
#[:n]只要前n 
#[:-n]從前面取不要後n 
#[n:]從n開始取 
#[-n:]只要後n 
x=['0','1','2','3','4','5','6','7','8','9']
print(x[:3])
print(x[:-3])
print(x[3:])
print(x[-3:])
print(x[0:3])
#[0:3] 取0 1 2 
print(x[0:9])
#[a:b] 取a到b-1
print(x[0:6:2])
print(x[0:6:3])
#[a:b:c] c是隔幾個 a+c,a+2c,...
#比如c=2 0 2 4....
#c=3 0 3 6....