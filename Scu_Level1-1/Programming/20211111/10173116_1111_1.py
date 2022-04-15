x1,x2,x3,x4,x5=eval(input('請輸入5個考試成績:'))
x=[x1,x2,x3,x4,x5]
print('分數串列為   :',x)
y=sorted(x,reverse=True)
print('高分往低分排列:',y)
z=sorted(x)
print('低分往高分排列:',z)
print('最高分       :',max(x))
print("總分         :",sum(x))
##y,z可以直接放進print 逗號後面