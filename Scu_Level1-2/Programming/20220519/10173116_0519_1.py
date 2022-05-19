from tkinter import *

window = Tk()
window.title('tk1')
a = Label(window, text='AaaA', relief=RAISED, width=10, bg='#ADADAD', font='ITCBLKAD 14 italic')
b = Label(window, text='BbbB', relief=SUNKEN, width=10, bg='#FF5151', font='BRUSHSCI 14 italic')
c = Label(window, text='CccC', relief=GROOVE, width=10, bg='#F0F0F0', font='ITCEDSCR 14 italic')

a.pack()
b.pack(pady=7)
c.pack()

window.mainloop()