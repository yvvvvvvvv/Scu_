#dict.items()同時取key value
#for a,b in dict.items()
#sorted()
##for a in sorted(dict.key())排開頭字母
#for a in dict.values() 如果有重複 也會出現
##for a in set(dict.values()) 轉成set重複項會自動影藏
#sorted(dict.item()) 排序預設key 如果想用value sorted(dict.values())不存在 要用sorted(dict.items(),key=lambda x:x[1])
#lambda 匿名函數
#x:[0] key x:x[1] value