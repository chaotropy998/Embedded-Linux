# /------------------------------------------------------------------------------/
# This code is made to run 2 calculators: A basic one where it calculates the sum
# and subtraction of a number, and the other to calculate the number's factorial
# /--------------------------------------------------------------------------/

from tkinter import *
from tkinter.messagebox import showinfo, showerror
from math import factorial

def basic_calculator_window():
    def basic_calculator():
        try:
            m = float(e1.get())
            n = float(e2.get())
            
            if var.get() == 1:
                result = m + n
            elif var.get() == 2:
                result = m - n
            else:
                showerror(title="Error", message="Please select an operation.")
                
            result_label.config(text=f"The result is: {result}")
            
        except ValueError:
            showerror(title="ValueError", message="Invalid input. Please enter numbers.")
 
    # Basic Calculator Toplevel window settings
    box = Toplevel(root)
    box.title("Basic Calculator")
    
    box.geometry("300x175+800+400")
    box.title("Simple Calculator")
    box.resizable(False, False)


    var = IntVar()

    Label(box, text="Enter the value of M: ").place(x=20, y=20)
    Label(box, text="Enter the value of N: ").place(x=20, y=45)

    result_label = Label(box, text="")


    e1 = Entry(box, width=15)
    e2 = Entry(box, width=15)

    sumButton = Radiobutton(box, text='Sum', variable=var, value =1)
    subButton = Radiobutton(box, text="Subtract", variable=var, value=2)

    calculate_button = Button(box, text="Calculate",command=basic_calculator)

    e1.place(x=160, y=20)
    e2.place(x=160, y=45)
    sumButton.place(x=20, y=80)
    subButton.place(x=20,y=105)
    calculate_button.place(x=160, y=100)
    result_label.place(x=160, y=75)

def factorial_calculator_window():
    def calculate_factorial():
        try:
            n = int(factorial_entry.get())
            result = factorial(n)
            factorial_result.config(text=f"The factorial of {n} is {result}")
        except ValueError:
            showerror("Error", "Please enter a valid integer.")
 
    # Factorial Toplevel window settings
 
    factorial_window = Toplevel(root)
    factorial_window.geometry("300x100+900+400")
    factorial_window.title("Factorial Calculator")
    factorial_window.resizable(True,False)

    factorial_label = Label(factorial_window, text="Enter an integer:")
    calculate_button = Button(factorial_window, text="Calculate", command=calculate_factorial)
    factorial_result = Label(factorial_window, text="")
    factorial_entry = Entry(factorial_window)

    factorial_label.pack()
    factorial_entry.pack()
    factorial_result.pack()
    calculate_button.pack()

# Root window from which the user can choose basic or factorial calculator

root = Tk()
root.geometry("300x100+800+400")
root.title("Calculator")
root.resizable(False,False)

# Create RadioButtons to choose between calculators
calculator_choice = IntVar()

basic_radio = Radiobutton(root, text="Basic Calculator", variable=calculator_choice, value=1, command=basic_calculator_window)
factorial_radio = Radiobutton(root, text="Factorial Calculator", variable=calculator_choice, value=2, command=factorial_calculator_window)

label = Label(root, text="Choose a Calculator:")

label.pack()
basic_radio.pack()
factorial_radio.pack()

root.mainloop()