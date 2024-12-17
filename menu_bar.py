#!/usr/bin/python3
from tkinter import*

def donothing():
	filewin=Toplevel(root)
	button=Button(filewin, text="Do nothing button")
	button.pack()

root=Tk()    #creating a window using the tkinter class Tk()
menu_bar=Menu(root)

file_menu=Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=donothing)
file_menu.add_command(label="Open", command=donothing)
file_menu.add_command(label="Save As", command=donothing)
file_menu.add_command(label="Save", command=donothing)
file_menu.add_command(label="Close", command=donothing)

file_menu.add_separator()

file_menu.add_command(label="Exit", command=root.quit())

menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu=Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo", command=donothing)
edit_menu.add_command(label="Cut", command=donothing)
edit_menu.add_command(label="Paste",command=donothing)
edit_menu.add_command(label="Delete", command=donothing)
edit_menu.add_command(label="Select All", command=donothing)

menu_bar.add_cascade(label="Edit", menu=edit_menu)

help_menu=Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Help Index", command=donothing)
help_menu.add_command(label="About", command=donothing)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)
root.mainloop()

