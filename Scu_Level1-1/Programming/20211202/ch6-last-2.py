#串列賦值 一個串列的更改會影響到另一個串列
a=['sa','aaxax','scfsexfe']
b=a
print(b) #['sa', 'aaxax', 'scfsexfe']
a.append('uftk')
print(b) #['sa', 'aaxax', 'scfsexfe', 'uftk']
b.append('tgm,k')
print(a) #['sa', 'aaxax', 'scfsexfe', 'uftk', 'tgm,k']

#切片拷貝(copy) friendsport=mysport[:] 兩者記憶體位置不同
a=['vm.','rfkgk','yrtfkgmiy']
b=a[:]
a.append('tfmkg,') 
b.append('glu.,')
print(a) #['vm.', 'rfkgk', 'yrtfkgmiy', 'tfmkg,']
print(b) #['vm.', 'rfkgk', 'yrtfkgmiy', 'glu.,']

#copy 只能在第一層起作用 二為串列就已經不行了  只更改串列本身的記憶體位置 但裡面的子物件並不分開(串列位置 物件位置 不同)
a=[1,2,3,[4,5,6]]
b=a.copy()
a.append(7)
print(a) #[1, 2, 3, [4, 5, 6], 7]
print(b) #[1, 2, 3, [4, 5, 6]]
a[3].append(7)
print(b) #[1, 2, 3, [4, 5, 6, 7]]

#deepcopy 需要import copy 完全獨立  
import copy #import 是模組 要導入模組才能用模組裡的東西
a=[1,2,3,[4,5,6]]
b=copy.deepcopy(a)
a[3].append(7)
print(b) #[1, 2, 3, [4, 5, 6]]
