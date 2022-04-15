#開啟一個檔案oprn()，供讀取或寫入
#file_Obj=open(file,mode='rt')
#r w a x action
#b t 二進位 文字
x1=open('out1.txt',mode='w')#取代先前資料
print('testing for output',file=x1)
x1.close()
x2=open('out2.txt',mode='a')#附加資料後面
print('testing for out put',file=x2)
x2.close()
