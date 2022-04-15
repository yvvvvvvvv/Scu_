a='X'
b=20
print('%s你成績是%d'%(a,b))
print('{}你成績是{}'.format(a,b))
#format前面記得加.
print('{1}你成績是{0}'.format(b,a))
#後面()中的順序編號是(0,1,2,3,......)
#format的留空間是:m.nf(for example)
print('{1:3s}你成績是{0:7.2f}'.format(b,a))
#:取代%
#如果是開頭的碼 會靠左留空
#靠左< 靠右> 置中^
