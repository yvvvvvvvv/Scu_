from tkinter import *
def count():
    l = n4.get()
    if l == '+':
        n3.set(n1.get()+n2.get())
    elif l == '-':
        n3.set(n1.get()-n2.get())
    elif l == '*':
        n3.set(n1.get()*n2.get())
    elif l == '/':
        n3.set(n1.get()/n2.get())


def add():
    n4.set('+')
def sub():
    n4.set('-')
def mul():
    n4.set('*')
def div():
    n4.set('/')

def clear():
    n1.set(0)
    n2.set(0)
    n3.set(0)
    n4.set('*')

w = Tk()
n1 = IntVar()
n2 = IntVar()
n3 = IntVar()
n4 = StringVar()
n4.set('*')

e1 = Entry(w, width=8, textvariable=n1)
label = Label(w, width=3, textvariable=n4)
e2 = Entry(w, width=8, textvariable=n2)
btn1 = Button(w, width=5, text='+', command=add)
btn2 = Button(w, width=5, text='-', command=sub)
btn3 = Button(w, width=5, text='*', command=mul)
btn4 = Button(w, width=5, text='/', command=div)
btn5 = Button(w, width=5, text='=', command=count)
e3 = Entry(w, width=8, textvariable=n3)
clearbtn = Button(w, width=5, text='C', command=clear)

e1.grid(row=0, column=0)
label.grid(row=0, column=1, padx=5)
e2.grid(row=0, column=2)
btn1.grid(row=1, column=1)
btn2.grid(row=2, column=1)
btn3.grid(row=3, column=1)
btn4.grid(row=4, column=1)
clearbtn.grid(row=5, column=0, pady=5)
btn5.grid(row=5, column=1, pady=5)
e3.grid(row=6, column=1, pady=5)

w.mainloop()