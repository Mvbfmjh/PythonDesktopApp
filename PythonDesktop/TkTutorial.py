##-------------------------------------------------------------
## TUTORIAL SCRIPT
## Link: https://tkdocs.com/tutorial/firstexample.html
## This is a tutorial script for learning how to use tkinter
##-------------------------------------------------------------


from tkinter import *
from tkinter import ttk

### This function is placed up here because it is called by other widgets 
### and needs to be implemented before the widgets refer to it
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int (0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
### This function takes the value of "feet" and sets the value of "meters" through the calculation

# Setting up the main window of the tutorial
root = Tk()
root.title("Feet to Meters")

# Main frame of the window

## This will hold the contents of the user interface
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
### The reason why this frame is made is because the root window is from older themes, 
### and there will be a contrast between the newer themed widges and the old themed window

# Entry widget

## This is where the user would input some data
feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

### EXPLANATION OF WHAT'S GOING ON
###
### When creating a widget, 2 things need to be done: 1) Create the widget itself; 2) Place the widget onscreen
### 1) When creating a widget, a parent must be specified -> The widget will be placed into the parent
###    ttk.Entry() is the function to create a widget: 
###        First parameter is always the parent. Additional parameters are to set other configuration options
###        width=7 means the text entry allows upto 7 characters
###
### 2) To place the widget onto the screen, [widget_name].grid() is used
###    [widget_name].grid()
###        Widgets are placed in the columns/rows specified in the parameters
###        sticky is used to anchor the object to the sides of the cell it is in 
###        N = Top, W = Left, E = right, S = bottom
###
### textvariable=[variable_name]
###    This links the text within the entry to a global variable, and Tk will update it automatically
###    In Python, this variable must be an instance of StringVar()

# Other widgets

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# Add Padding
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
# When the app starts, it will start on the entry widget
feet_entry.focus()
# When the user presses the "Return" key, it will also run the function calculate
root.bind("<Return>", calculate)

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int (0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
### This function takes the value of "feet" and sets the value of "meters" through the calculation

root.mainloop()


### Additional Note from the tutorial:
### Typically, we want to encapsulate the data rather than placing it in the global variable space
### For additional information on this tutorial script, refer back to the link at the top