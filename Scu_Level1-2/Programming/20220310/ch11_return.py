def vip(id,name,tel=''):
    if tel:
        vip_dict={'VIP_ID':id,'NAME':name,'TEL':tel}
    else:
        vip_dict={'VIP_ID':id,'NAME':name}
    return vip_dict
member=vip('101','nal')
print(member)