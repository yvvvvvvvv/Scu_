import base64
import hashlib

def s(x):
  be = base64.b64encode(x.encode())
  bes = be.decode()
  print('已加密字串,結果為:%s'%bes)
def m(x):
  h = hashlib.md5(x.encode())
  h.update(x.encode("utf8"))
  val = h.digest()
  print('已加密字串,結果為:', h.hexdigest())

x = input('欲加密字串:')
y = input('1:加密方法一 2:加密方法二 :')
if y == '1':
  s(x)
elif y == '2':
  m(x)
else:
  error