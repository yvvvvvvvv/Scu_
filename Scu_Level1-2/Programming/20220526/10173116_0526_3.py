from tkinter import *
def printInfo():
    selection=''
    for i in checkboxes:
        if checkboxes[i].get()==True:
            selection=selection+sports[i]+"\t"
    print('姓名:'+n1.get())
    print('電話:'+n2.get())
    print('喜歡的運動:'+selection)
def clear():
    n1.set("")
    n2.set("")
    checkboxes.clear()
window=Tk()
window.title('ch18_28_1')
lab1=Label(window,text="姓名").grid(row=0,sticky=W)
lab2=Label(window,text="電話").grid(row=1,sticky=W)
lab3=Label(window,text="請選擇喜歡的運動").grid(row=2,sticky=W)
n1=StringVar()
n2=StringVar()
e1=Entry(window,textvariable=n1)
e2=Entry(window,textvariable=n2)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

sports={0:'美式足球',1:'棒球',2:'籃球',3:'網球'}
checkboxes={}
for i in range(len(sports)):
    checkboxes[i]=BooleanVar()
    Checkbutton(window,text=sports[i],variable=checkboxes[i]).grid(row=i+3,sticky=W)
Button(window,text='確定',width=10,command=printInfo).grid(row=i+4,column=i+3)
Button(window,text='取消',width=10,command=clear).grid(row=i+4,column=i+4)
window.mainloop()