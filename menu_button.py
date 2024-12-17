#!/usr/bin/python3
from tkinter import*

top=Tk()

mb=Menubutton(top, text="Karis", relief=RAISED)
mb.grid()

mb.menu=Menu(mb, tearoff=0)
mb["menu"]=mb.menu

allan=IntVar()
mbugua=IntVar()

mb.menu.add_checkbutton(label="allan", variable=allan)
mb.menu.add_checkbutton(label="mbugua", variable=mbugua)
mb.pack()

top.mainloop()