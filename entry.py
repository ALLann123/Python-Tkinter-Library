#!/usr/bin/python3
from tkinter import*

root=Tk()

e = Entry(root, width=50 )
e.pack()
e.insert(0, "Enter name")

def my_click():
	hello="Hello " + e.get()
	label=Label(root, text=hello, fg="red")
	label.pack()
	return

button=Button(root, text="Continue", command=my_click, fg="blue")
button.pack()



root.mainloop()