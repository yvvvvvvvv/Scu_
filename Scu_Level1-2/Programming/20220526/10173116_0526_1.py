from tkinter import *
from tkinter import messagebox

def printInfo():
    if(e1.get() == '' or e2.get() == ''):
        messagebox.showinfo('提醒視窗','二個欄位都不能為空')
    else:
        print('Account :%s\nPassword:%s'%(e1.get(),e2.get()))
        e1.delete(0,END)
        e2.delete(0,END)

w = Tk()
w.title('')

lab1 = Label(w, text='Account ').grid(row = 0)
lab2 = Label(w, text='Password').grid(row = 1)

e1 = Entry(w)
e2 = Entry(w, show='*')

e1.insert(1,'Kevin')
e2.insert(1,'pwd')

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

q = PhotoImage(file='p.png')

btn1 = Button(w, image=q, text='Print', command=printInfo, compound=TOP)
btn1.grid(row=2, column=0, sticky=W, pady=10) #sticky=W 對齊上面的label

btn2 = Button(w, image=q,text='Quit', command=w.destroy, compound=TOP)
btn2.grid(row=2, column=1, sticky=W, pady=10)

w.mainloop()