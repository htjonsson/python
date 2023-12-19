from tkinter import *
from tkinter import ttk

global childWindow

def calculate(*args):

    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

    if childWindow != None :
        childWindow.deiconify()
    # childWindow.grab_set()

def whatever():
    # Replace this with your own event for example:
    print("oi don't press that button")
    childWindow.withdraw()

mainWindow = Tk()
mainWindow.title("Feet to Meters")

# Make the window resizable false
mainWindow.resizable(False,False)

mainFrame = ttk.Frame(mainWindow, padding="3 3 12 12")
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))

mainWindow.columnconfigure(0, weight=1)
mainWindow.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainFrame, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainFrame, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainFrame, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainFrame, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainFrame, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainFrame, text="meters").grid(column=3, row=2, sticky=W)

for child in mainFrame.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
mainWindow.bind("<Return>", calculate)

#Create a child window using Toplevel method
childWindow = Toplevel(mainWindow)
childWindow.geometry("750x250")
childWindow.title("New Child Window")
childWindow.withdraw()
childWindow.protocol("WM_DELETE_WINDOW", whatever)

#Create Label in Childwindow
label_child = Label(childWindow , text= "Hi, this is Child Window", font=('Helvetica 15'))
label_child.pack()

mainWindow.mainloop()