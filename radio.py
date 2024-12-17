#!/usr/bin/python3
from tkinter import*
from PIL import ImageTk, Image

root=Tk()
root.title("Radio Tutorial")

#r =IntVar()
#r.set("2")

MODES=[
	("Pepperoni","Pepperoni"),
	("Cheese","Cheese"),
	("Mushroom","Mushroom"),
	("Onion", "Onion"),
]

pizza=StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
	Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)
def clicked(value):
	mylabel = Label(root, text=value)
	mylabel.pack()


#Radiobutton(root, text="Option1", variable=r, value=1, command=lambda:clicked(r.get())).pack()
#Radiobutton(root, text="Option2", variable=r, value=2, command=lambda:clicked(r.get())).pack()

#mylabel = Label(root, text=pizza.get())
#mylabel.pack()

myButton=Button(root, text="Click Me", command=lambda:clicked(pizza.get()))
myButton.pack()
mainloop()