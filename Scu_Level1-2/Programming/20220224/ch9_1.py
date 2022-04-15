#dict 
#key:value
fruits={'西瓜':15,'香蕉':20,'水蜜桃':25}
noodles={'牛肉麵':100,'肉絲麵':80,'陽春麵':60}
print(fruits)
print(noodles)
print(type(fruits))
print(fruits['水蜜桃']) #25
#增加字典內容
fruits['橘子']=18
print(fruits) #{'西瓜': 15, '香蕉': 20, '水蜜桃': 25, '橘子': 18}
#改內容 改成香蕉12
fruits['香蕉']=12
print(fruits) #{'西瓜': 15, '香蕉': 12, '水蜜桃': 25, '橘子': 18}
##刪除用dict.pop(key)
##del dict[key]