#!/usr/bin/python3
from tkinter import*
from tkinter import messagebox

top=Tk()      #create a tkinter object for the whole window
top.geometry("400x400")    #edit the size of the whole window
def  hello_call_back():  #create a function
	msg=messagebox.showinfo("Greetings", "Hello Mr.Robot")         #create a message box to be displayed when the button is executed

b=Button(top, text="Note", command=hello_call_back, bg="Green")       #create a button object with the function being executed when pressed
b.place(x=200, y=200)             #this is the shape of the button on the screen
top.mainloop()    #execute the window to be displayed on the screen