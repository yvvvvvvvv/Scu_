print('觸犯道路交通管理處罰條例人員名單')
A = {'name':'甲','age':40,'罪責':{'第62條':'汽車駕駛人駕駛汽車肇事','第12條':'汽車使用吊銷、註銷之牌照'},'罰鍰':{'第62條':2000,'第12條':5000}}
B = {'name':'乙','age':52,'罪責':{'第16條':'裝置高音量喇叭或其他產生噪音器物','第56條':'在禁止臨時停車處所停車','第82條':'未經許可在道路擺設攤位','第17條':'汽車不依限期參加定期檢驗或臨時檢驗'},'罰鍰':{'第16條':1200,'第56條':800,'第82條':1500,'第17條':900}}
C = {'name':'丙','age':63,'罪責':{'第21條':'未領有駕駛執照駕駛小型車或機車'},'罰鍰':{'第21條':8000}}

def guilt(name): 
    a = len(name['罪責'])
    n = []
    for b in name['罪責']:
        gu = (b,name['罪責'][b])
        n.append(gu)
    return a, n

def money(name):
    m = 0
    n = []
    for c in name['罰鍰']:
        mo = (c,name['罰鍰'][c])
        n.append(mo)
        m += name['罰鍰'][c]
    return m, n

'''犯罪次數排名'''
gua, ga = guilt(A)
gub, gb = guilt(B)
guc, gc = guilt(C)
x = [gua,gub,guc]
x1 = enumerate(x, start = 1)
x2 = (sorted(x1, key = lambda s: s[1]))
#print(x2) #[(原始位置,value)]

'''罰錢金額排名'''
moa, ma = money(A)
mob, mb = money(B)
moc, mc = money(C)
y = [moa,mob,moc]
y1 = enumerate(y, start = 1)
y2 = (sorted(y1, key = lambda s: s[1]))

while True:
    options = input('請輸入: 1.查看A 2.查看B 3.查看C 4.犯罪數排名 5.累積罰金&罰鍰數排名 6.結束程式:')
    if options == '1':
        print('Name:',A['name'],'\nAge:',A['age'])
        print('共觸犯(條):',gua)
        print('條例內容:',ga)
        print('罰鍰總額(元):',moa)
        print('詳細內容:',ma)
    elif options == '2':
        print('Name:',B['name'],'\nAge:',B['age'])
        print('共觸犯(條):',gub)
        print('條例內容:',gb)
        print('罰鍰總額(元):',mob)
        print('詳細內容:',mb)
    elif options == '3':
        print('Name:',C['name'],'\nAge:',C['age'])
        print('共觸犯(條):',guc)
        print('條例內容:',gc)
        print('罰鍰總額(元):',moc)
        print('詳細內容:',mc)
    elif options == '4':
        print('甲為1，乙為2，丙為3')
        print('(人,犯罪次數)(少->多）')
        print(x2)
    elif options == '5':
        print('甲為1，乙為2，丙為3')
        print('(人,金額)(少->多）')
        print(y2)
    elif options == '6':
        print('Bye bye~~~')
        break
    else:
        print('輸入錯誤，請重新輸入')
        continue


# 道路交通管理處罰條例62條	汽車駕駛人駕駛汽車肇事 新臺幣一千元以上三千元以下罰鍰
# 道路交通管理處罰條例12條 汽車使用吊銷、註銷之牌照 新臺幣三千六百元以上一萬零八百元以下罰鍰
# 道路交通管理處罰條例16條 裝置高音量喇叭或其他產生噪音器物 新臺幣九百元以上一千八百元以下罰鍰
# 道路交通管理處罰條例56條 在禁止臨時停車處所停車 新臺幣六百元以上一千二百元以下罰鍰
# 道路交通管理處罰條例82條 未經許可在道路擺設攤位 新臺幣一千二百元以上二千四百元以下罰鍰
# 道路交通管理處罰條例17條 汽車不依限期參加定期檢驗或臨時檢驗 新臺幣九百元以上一千八百元以下罰鍰
# 道路交通管理處罰條例21條 未領有駕駛執照駕駛小型車或機車 新臺幣六千元以上一萬二千元以下罰鍰
