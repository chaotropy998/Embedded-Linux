from tkinter import *

box = Tk()
box.title('Test Code')

def start():
    print("Start is triggered")

b1 = Button(box, text = "Start", command=start)
b2 = Button(box, text = "Left")
b3 = Button(box, text = "Right")
b4 = Button(box, text = "Stop", command = box.destroy)

b1.grid(row = 0, column= 1)
b2.grid(row = 1, column= 0)
b3.grid(row = 1, column= 2)
b4.grid(row = 2, column = 1)

box.resizable(False, False)
box.mainloop()
