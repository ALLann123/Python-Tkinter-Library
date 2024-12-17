#!/usr/bin/python3
from tkinter import*
from tkinter import messagebox

root=Tk()
root.title("Message Box Tutorial")

#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
	response=messagebox.showinfo("This Is My Popup!", "Hello World")
	label=Label(root, text=response).pack()
	#if response == "yes":
		#Label(root, text="You Clicked Yes!!").pack()
	#else:
		#Label(root, text="You Clicked No!!").pack()


Button(root, text="Popup", command=popup).pack()

root.mainloop()