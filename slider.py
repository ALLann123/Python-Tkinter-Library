#!/usr/bin/python3
from tkinter import*

root=Tk()
root.title("Slide Tutorial")
root.geometry("400x400")      #used to resize the root window

vertical=Scale(root, from_=0, to=200)
#pack it in its own line
vertical.pack()
def slide():
	my_label=Label(root, text=Horizontal.get()).pack()
	root.geometry(str(Horizontal.get())+"x"+str(vertical.get())) 
Horizontal=Scale(root, from_=0, to=200, orient=HORIZONTAL)
Horizontal.pack()


my_btn=Button(root, text="Click Me", command=slide).pack()

root.mainloop()