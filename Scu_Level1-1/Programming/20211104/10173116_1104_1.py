x=[1,2,3,4,5,6,7,8,9,10]
x1=sum(x[:3])
x2=sum(x[1:4])
x3=sum(x[0:10:2])
x4=sum(x[-3:])
x5=sum(x[4:])
#sum可以直接,sum() 不用分開弄
print('james第1-3場個別得分',x[:3],'總分={}'.format(x1))
print('james第2-4場個別得分',x[1:4],'總分={}'.format(x2))
print('james第1,3,5,7,9場個別得分',x[0:10:2],'總分={}'.format(x3))
print('james後3場個別得分',x[-3:],'總分={}'.format(x4))
print('james第5場開始到最後的得分',x[4:],'總分={}'.format(x5))
print('james最高分=',max(x[0:10]),'最低分=',min(x[0:10]))
