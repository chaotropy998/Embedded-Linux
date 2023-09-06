from tkinter import *

box = Tk()
box.geometry("300x150+800+400")
box.title("Word Reverser!")

def Reverser():
    text = textbox.get()
    reversed_text = "".join(reversed(text))
    result.config(text=reversed_text) 

Label(box, text="Enter your text:").grid(row=0, column= 0)
Button(box, text="Stop", command=box.destroy).grid(row=3, column=1)

textbox = Entry(box)
button = Button(box, text="Reverse", command=Reverser)
result = Label(box, text="")

textbox.grid(row= 0, column= 1)
button.grid(row= 2, column= 1)
result.grid(row=1, column=1)
 
box.mainloop()