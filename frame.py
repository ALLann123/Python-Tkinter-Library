#!/usr/bin/python3
from tkinter import*
from PIL import ImageTk, Image

root = Tk()
root.title("Frame Tutorial")

frame=LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10, pady=10)

b=Button(frame, text="Don't Click Here")
b.grid(row=0, column=0)

b2=Button(frame, text="Or Here!!")
b2.grid(row=2, column=0)



root.mainloop()