from tkinter import *

def red():
    w.config(bg='red')
    label = Label(text='Red', bg='white', fg='red', font='Mingliu 20 bold', width=8)
    label.place(x=50, y=50)

def yellow():
    w.config(bg='yellow')
    label2 = Label(text='Yellow', bg='white', fg='yellow', font='Mingliu 20 bold', width=8)
    label2.place(x=50, y=50)

def blue():
    w.config(bg='blue')
    label3 = Label(text='Blue', bg='white', fg='blue', font='Mingliu 20 bold', width=8)
    label3.place(x=50, y=50)

def clear():
    for widget in w.winfo_children():
        if type(widget) == type(exitbtn):
            pass
        else:
            widget.destroy()
        w.config(bg=orig_color)

w = Tk()
w.title('3')
w.geometry("300x200")
orig_color = w.cget('background')

exitbtn = Button(w, text='Exit', command=w.destroy)
redbtn = Button(w, text='Red', command=red)
bluebtn = Button(w, text='Blue', command=blue)
yellowbtn = Button(w, text='Yellow', command=yellow)
clearbtn = Button(w, text='Clear', command=clear)

exitbtn.pack(anchor=S, side=RIGHT, padx=5, pady=5)
clearbtn.pack(anchor=S, side=RIGHT, padx=5, pady=5)
yellowbtn.pack(anchor=S, side=RIGHT, padx=5, pady=5)
bluebtn.pack(anchor=S, side=RIGHT, padx=5, pady=5)
redbtn.pack(anchor=S, side=RIGHT, padx=5, pady=5)

w.mainloop()