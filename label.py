from tkinter import *
from PIL import Image, ImageTk  # Import Pillow libraries

top = Tk()
top.geometry("300x300")

var = StringVar()
label = Label(top, textvariable=var, relief=RAISED)
var.set("Profile Below")
label.pack()

# Load the .jpg image using PIL
image = Image.open("J:/code/python code/tkinter/eliot.jpg")  # Provide correct path to your image
photo = ImageTk.PhotoImage(image)

# Display the image in the label
label2 = Label(top, image=photo, height=500, width=500)  # Adjust height and width as needed
label2.pack()

top.mainloop()
