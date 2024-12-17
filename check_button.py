#!/usr/bin/python3
from tkinter import*

top=Tk()
top.geometry("200x200")

var1=IntVar()
var2=IntVar()

c1=Checkbutton(top, text="C++", variable=var1, onvalue=1, offvalue=0, height=5, width=20)
c2=Checkbutton(top, text="Python", variable=var2, onvalue=1, offvalue=0, height=5, width=20)

c1.pack()
c2.pack()
top.mainloop()