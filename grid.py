#!/usr/bin/python3
from tkinter import*

root=Tk()

#create object onthe screen
label1=Label(root, text="Hello, Mr.Robot!!")
label2=Label(root, text="Elliot right?")

#put widget onto the window
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

root.mainloop()