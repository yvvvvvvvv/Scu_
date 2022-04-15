string='python'
print(string[0]) #p
#[1] y [2] t.....
print(string[-1]) #n
#[-2] o [-3] h.....
#多重
s1,s2,s3,s4='abcd'
print(s1) #a
#...
#可以切片喔 string[0:3]...
#len() max() min()
str='Deep Learning'
slen=len(str)
print(slen) #13
maxs=max(str)
print('字串最大的unicode碼值和字元',ord(maxs),maxs) #114 r
mins=min(str)
print('字串最小的unicode碼值和字元',ord(mins),mins) #32 (space)

#字串不能改內容 a[0]='tmu' 不行 要先換成串列