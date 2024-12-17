#!/usr/bin/python3
from tkinter import*

root=Tk()
root.title("Checkbox Tutorial")
root.geometry("400x400")

var=StringVar()

def show():
	my_label= Label(root,text=var.get()).pack()

c=Checkbutton(root, text="Checkbox this box I dare you", variable=var, onvalue="Attack", offvalue="Reccon")
c.deselect()
c.pack()



myButton=Button(root, text="show selection", command=show).pack()


root.mainloop()