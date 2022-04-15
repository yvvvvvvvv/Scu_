def vip(id,name,tel):
    vip_dict={id:{'NAME':name,'TEL':'沒有號碼'}}
    if tel:
        vip_dict[id]['TEL']=tel
    return vip_dict 

v={}
while True:
    print('建立VIP資訊系統')
    id=input('請輸入ID:')
    name=input('請輸入姓名:')
    tel=input('請輸入電話號碼:')
    member=vip(id,name,tel)
    v.update(member)
    print(v)
    re=input('是否繼續?輸入非y字元結束:')
    if re !="y":
        break