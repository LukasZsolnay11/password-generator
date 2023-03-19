from tkinter import *

root = Tk()

def click():
    print("Hello kokot")

button = Button(root, text="Click me", command=click)
button.pack()


root.mainloop()