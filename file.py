#!/usr/bin/python3
from tkinter import*
from tkinter import filedialog
from PIL import ImageTk, Image

root=Tk()
root.title("Opening Files")


def open():
	global my_Image
	root.filename=filedialog.askopenfilename(initialdir="image", title="Select a File", filetypes=(("jpg files", "*.jpg"),("all files","*.*")))
	label=Label(root, text=root.filename).pack()
	my_Image = ImageTk.PhotoImage(Image.open(root.filename))
	lbl=Label(root, image=my_Image).pack()


my_btn=Button(root, text="Select File", command=open).pack()

mainloop()