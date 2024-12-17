#!/usr/bin/python3
from tkinter import*

top=Tk()
label=Label(top,text="Favorite Programming Language")
label.pack()

lb=Listbox(top)
lb.insert(1,"Python")
lb.insert(2,"C++")
lb.insert(3,"Java")
lb.insert(4,"Ruby")
lb.insert(5,"C")
lb.pack()

top.mainloop()