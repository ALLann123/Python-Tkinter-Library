#!/usr/bin/python3
from tkinter import*

root=Tk()
def my_click():
	label=Label(root, text="Welcome Mr.Robot", fg="red")
	label.pack()
	return

button=Button(root, text="CLick Me", padx=50, pady=50, command=my_click, fg="blue")

button.pack()
root.mainloop()