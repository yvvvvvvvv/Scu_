#byte=字串前加b
#unicode轉bytes用encode()
str='abc'
strbytes=str.encode('utf-8')
print(len(strbytes)) #str長度
print(type(strbytes)) #str型態
print(strbytes)
name='yvonne'
namebytes=name.encode('utf-8')
print(namebytes)
#NAME
name2="侯禹鳳"
name2bytes=name2.encode('utf-8')
print(len(name2bytes))
print(type(name2bytes))
print(name2bytes)
#bytes轉unicode用decode()
name2ucode=name2bytes.decode('utf-8')
print(len(name2ucode))
print(type(name2ucode))
print(name2ucode)
