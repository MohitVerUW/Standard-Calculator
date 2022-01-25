# Import modules needed for GUI
import tkinter as tk
import math


# --------------------------FUNCTIONS------------------------------------------------------------#
def num_Input(num):
    """Function takes input from the number buttons pressed on GUI"""

    global result,equal_Flag, math_Flag, percentage_Flag

    # Enable buttons that were disabled from errors and reset parameters
    if btn_Percent["state"] == tk.DISABLED:
        bttn_Enable()
        reset_Param()

    # Reset app if the user hits equal button or percent button followed by pressing any number button
    if equal_Flag == True or percentage_Flag == True:
        reset_Param()

    # Allows user to input the 2nd value for the math_Op() function
    print(math_Flag)
    if math_Flag == True:
        entry.delete(0, "end")
        math_Flag = False

    entry.insert("end", str(num))  # display button pressed on entry widget

def clear():
    """Function clears everything in memory and restores default parameters"""

    # Enable all math operation buttons that had been disabled upon error
    if btn_Percent["state"] == tk.DISABLED:
        bttn_Enable()

    # Reset all program parameters
    reset_Param()

def delete():
    """Function deletes the last entry in the entry widget"""

    entry.delete(len(entry.get()) - 1)  # delete the last entry in the entry widget

def negation():
    """Converts number from +ve to -ve and vice versa"""

    temp1 = int(entry.get())

    if temp1 != 0.0:
        entry.delete(0, "end")
        entry.insert(0, -temp1)

def decimal():
    """Adds decimal point to a number being inputted by user"""
    global math_Flag
    # If decimal point missing, insert to end of display
    if "." not in entry.get():
        entry.insert(len(entry.get()), ".")

    # If user starts entry using a decimal point insert "0" to left of decimal
    if entry.get().index(".") == 0:
        entry.insert(0, "0")
        math_Flag = False

def percentage():
    """Calculates the percentage of two numbers"""

    global result, percentage_Flag

    temp2 = float(entry.get()) / 100.0
    percentage_Flag = True
    entry.delete(0, "end")
    entry.insert(0, temp2)

def squareRoot():
    """Calculates square root of a non-negative number"""

    global result, equal_Flag

    # Check and see if number inputted can be square rooted, if not catch error using exception block
    try:
        temp7 = math.sqrt(float(entry.get()))

        if result == 0 or equal_Flag == True:
            var.set(f'\u221A({float(entry.get())})')  # '\u221A' is unicode character for sqrt

        entry.delete(0, "end")
        entry.insert(0, temp7)

    except Exception as err1:
        err1 = "Invalid Input"
        var.set(f'\u221A({float(entry.get())})')
        entry.delete(0, "end")
        entry.insert(0, err1)

        # Disable all math buttons and entry widget
        bttn_Disable()
    pass

def squared():
    """Calculates the square of a number"""

    global result

    temp6 = math.pow(float(entry.get()), 2)

    if result == 0 or equal_Flag == True:
        var.set(
            f'({float(entry.get())})\u00b2')  # '\u00b2' is the unicode character for x^y; note - the last chacrter of '\u00b2' is the superscripted character!

    entry.delete(0, "end")
    entry.insert(0, temp6)

def math_Op(oper):
    """Defines the mathematical operation to be performed by user"""

    global result, symbol, math_Flag, equal_Flag

    symbol = oper  # create symbol as global to be used in the equal() function

    temp3 = float(entry.get())  # get and store the entry widget contents into temp3 var
    entry.delete(0, "end")  # delete everything in the entry widget

    # if-statement to continue showing same result if same operator pressed more han once
    if math_Flag == False:

        # Lets user input first number and continue using the result obtained from equal() to do further calculations
        if result == 0 or equal_Flag == True:
            var.set(f'{str(temp3)} {oper}')
            result = temp3
            equal_Flag = False

        else:
            scrn = display.cget("text")  # get text from the display widget
            lst = scrn.split()  # convert the string into a list [0] = number [1] = math operator
            intermediate_Result(lst, temp3)  # separate function created to update result with consecutive calculations
            entry.insert(0, str(result))  # display result in entry widget
            var.set(f'{str(result)} {oper}')  # show the operation to be performed the display widget

    else:
        entry.insert(0, str(result))

    math_Flag = True  # resest math_Op() flag to continue with calculations

def equal():
    """Calculate the final result between two numbers"""

    global symbol, result, equal_Flag, temp4

    # update list to be passed into intermediate_Result() function
    lst[0] = result
    lst[1] = symbol

    # Returns the result of two numbers being operated on
    if equal_Flag == False:
        temp4 = float(entry.get())
        var.set(f'{str(result)} {symbol} {str(temp4)}')
        intermediate_Result(lst, temp4)
        equal_Flag = True

    # When equal_Flag is True, then simply perform the same operation by holding the 2nd number constant and updating the result
    else:
        var.set(f'{str(lst[0])} {symbol} {temp4}')
        intermediate_Result(lst, temp4)

    entry.delete(0, "end")
    entry.insert(0, str(result))

def intermediate_Result(dis_Exp, current):
    """Calculates the result of two numbers during consecutive math operations"""

    global result

    first_Num = float(dis_Exp[0])
    math = dis_Exp[1]

    try:
        # Division
        if math == "/":
            result = first_Num / current

        # Multiplication
        elif math == "*":
            result = first_Num * current
        # Subtraction
        elif math == "-":
            result = first_Num - current

        # Addition
        elif math == "+":
            result = first_Num + current

    except ZeroDivisionError:
        var.set("Cannot Divide by Zero")
        entry.insert(0, "Cannot Divide by Zero")

        # Disable all math buttons and entry widget
        bttn_Disable()

    except Exception as err2:
        var.set(err2)
        entry.insert(0, err2)

        # Disable all math buttons and entry widget
        bttn_Disable()

def reset_Param():
    """Reset program parameters"""

    global result, equal_Flag, percentage_Flag, math_Flag

    entry.delete(0, "end")  # clear the entry widget
    result = 0  # reset result back to 0
    equal_Flag = False  # boolean flag for equal button
    math_Flag = False  # boolean flag for math_Op()
    percentage_Flag = False  # boolean flag for percent button
    var.set(0)  # display 0 as in the result display screen

def bttn_Disable():
    """Disbale entry widget and math buttons"""

    # Disable entry widget
    entry.config(state="disabled")

    # Disable all math operation buttons
    btn_Percent["state"] = tk.DISABLED
    btn_Sqrt["state"] = tk.DISABLED
    btn_Exp["state"] = tk.DISABLED
    btn_Divide["state"] = tk.DISABLED
    btn_Multiply["state"] = tk.DISABLED
    btn_Minus["state"] = tk.DISABLED
    btn_Plus["state"] = tk.DISABLED
    btn_Equal["state"] = tk.DISABLED
    btn_Sign["state"] = tk.DISABLED
    btn_Decimal["state"] = tk.DISABLED

def bttn_Enable():
    """Enable all the disabled buttons"""

    entry.config(state="normal")  # Enable entry widget

    btn_Percent["state"] = tk.NORMAL
    btn_Sqrt["state"] = tk.NORMAL
    btn_Exp["state"] = tk.NORMAL
    btn_Divide["state"] = tk.NORMAL
    btn_Multiply["state"] = tk.NORMAL
    btn_Minus["state"] = tk.NORMAL
    btn_Plus["state"] = tk.NORMAL
    btn_Equal["state"] = tk.NORMAL
    btn_Sign["state"] = tk.NORMAL
    btn_Decimal["state"] = tk.NORMAL

# --------------------------MAIN CODE------------------------------------------------------------#

# Define variables that will be used as global variables
result = 0  # store the overall value
temp4 = 0  # used for equal()
equal_Flag = False  # boolean flag for equal button
math_Flag = False  # boolean flag for math_Op()
percentage_Flag = False  # boolean flag for percentage button

# Define list var to be used for equal() when equal button pressed
lst = [None, None]

# Widget text styling and spacing between
text_Style = "Segoe"
text_Height = 15
hor_Pad = 5
vert_Pad = 5

# Call on tkinter to create main window
main = tk.Tk()
main.geometry('500x700')  # define default size for window

# Define frames to contain widgets for GUI and configuration
display_Frame = tk.Frame(main)
bttn_Frame = tk.Frame(main)

# Widget arrangement using .grid() method
display_Frame.grid(row=0, column=0, sticky="nsew")
bttn_Frame.grid(row=1, column=0, sticky="nsew")

# Main window row and column configuration
main.columnconfigure(index=0, weight=1)
main.rowconfigure(index=0, weight=2)
main.rowconfigure(index=1, weight=3)

# ===================Calculator display========================

# Result widget to display result of calculation
var = tk.StringVar()  # define textvar for label widget
var.set(0)  # default display of label set to show 0

display = tk.Label(display_Frame, textvariable=var, font=("TKDefaultFont", 30), anchor="e")  # Display result only
entry = tk.Entry(display_Frame, font=("TKDefaultFont", 60), justify="right")  # Display and take user input

# Widget arrangement using .grid() method
display.grid(row=0, column=0, padx=hor_Pad, pady=vert_Pad, sticky="nsew")
entry.grid(row=1, column=0, padx=hor_Pad, pady=vert_Pad, sticky="nsew")

# Widget row and column configuration in associated frame
display_Frame.columnconfigure(index=0, weight=1)
display_Frame.rowconfigure(index=0, weight=1)
display_Frame.rowconfigure(index=1, weight=1)

# =============Calculator clear and delete buttons=================
#
# Define clear and delete buttons
btn_Clear = tk.Button(bttn_Frame, text="CLEAR", font=30, command=clear)
btn_Delete = tk.Button(bttn_Frame, text="\u232b", font=50, command=delete)

# Widget arrangement using .grid() method
btn_Clear.grid(row=0, column=0, columnspan = 2, padx=hor_Pad, pady=vert_Pad, sticky="nsew")
btn_Delete.grid(row=0, column=2, columnspan = 2, padx=hor_Pad, pady=vert_Pad, sticky="nsew")

# =============Calculator number and math buttons=================

# Buttons for math operations and "0" button
btn_Percent = tk.Button(bttn_Frame, text="%", justify="center", font=(text_Style, text_Height), command=percentage)
btn_Sqrt = tk.Button(bttn_Frame, text="\u221A(x)", justify="center", font=(text_Style, text_Height), command=squareRoot)
btn_Exp = tk.Button(bttn_Frame, text="x\u00b2", justify="center", font=(text_Style, text_Height), command=squared)

btn_Divide = tk.Button(bttn_Frame, text="/", justify="center", font=(text_Style, text_Height), command=lambda: math_Op("/"))
btn_Multiply = tk.Button(bttn_Frame, text="X", justify="center", font=(text_Style, text_Height), command=lambda: math_Op("*"))
btn_Minus = tk.Button(bttn_Frame, text="-", justify="center", font=(text_Style, text_Height), command=lambda: math_Op("-"))
btn_Plus = tk.Button(bttn_Frame, text="+", justify="center", font=(text_Style, text_Height), command=lambda: math_Op("+"))
btn_Equal = tk.Button(bttn_Frame, text="=", justify="center", font=(text_Style, text_Height), command=equal)

btn_Sign = tk.Button(bttn_Frame, text="\u00B1", font=(text_Style, text_Height), command=negation)
btn_Decimal = tk.Button(bttn_Frame, text=".", font=(text_Style, text_Height), command=decimal)

btn_0 = tk.Button(bttn_Frame, text="0", font=(text_Style, text_Height), command=lambda: num_Input(0))

# Widget arrangement using .grid() method
#row = 1
btn_Percent.grid(row=1, column=0, padx=hor_Pad, pady=vert_Pad, sticky="nsew")
btn_Sqrt.grid(row=1, column=1, padx=hor_Pad, pady=vert_Pad, sticky="nsew")
btn_Exp.grid(row=1, column=2, padx=hor_Pad, pady=vert_Pad, sticky="nsew")
btn_Divide.grid(row=1, column=3, padx=hor_Pad, pady=vert_Pad, sticky="nsew")

# row = 2
btn_Multiply.grid(row=2, column=3, padx=hor_Pad, pady=vert_Pad, sticky="nsew")

# row = 3
btn_Minus.grid(row=3, column=3, padx=hor_Pad, pady=vert_Pad, sticky="nsew")

# row = 4
btn_Plus.grid(row=4, column=3, padx=hor_Pad, pady=vert_Pad, sticky="nsew")

# row = 5
btn_Sign.grid(row=5, column=0, padx=hor_Pad, pady=vert_Pad, sticky="nsew")
btn_0.grid(row=5, column=1, padx=hor_Pad, pady=vert_Pad, sticky="nsew")
btn_Decimal.grid(row=5, column=2, padx=hor_Pad, pady=vert_Pad, sticky="nsew")
btn_Equal.grid(row=5, column=3, padx=hor_Pad, pady=vert_Pad, sticky="nsew")

# Buttons for numbers from 1 - 9 created using for-loop
num_List = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]

for ii in range(len(num_List)):
    for jj in range(len(num_List[1])):
        bttn = tk.Button(bttn_Frame, text=num_List[ii][jj], font=(text_Style, text_Height))
        bttn.grid(row=ii + 2, column=jj, padx=hor_Pad, pady=vert_Pad, sticky="nsew")
        bttn["command"] = lambda bttn=num_List[ii][jj]: num_Input(
            bttn)  # lambda used to pass button info to associated command
        bttn_Frame.rowconfigure(index=ii, weight=1)
        bttn_Frame.columnconfigure(index=jj, weight=1)

# Configure row and columns of all buttons in bttn_Frame widget
for kk in range(6):
    bttn_Frame.rowconfigure(kk, weight=1)

for mm in range(4):
    bttn_Frame.columnconfigure(mm, weight=1)

main.mainloop()
