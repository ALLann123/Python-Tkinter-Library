#!/usr/bin/python3
from tkinter import*


root=Tk()
root.title("Different Windows")
label=Label(root, text="First Window").pack()

def open():
	top=Toplevel()
	lbl=Label(top, text="Second Window").pack()
	button=Button(top, text="Close", command=top.destroy).pack()

	return

btn=Button(root, text="Open Second Window", command=open).pack()



root.mainloop()