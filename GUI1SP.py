#This imports the tkinter "tool box" this contains
#all the support material to make GUI elements
#by Including "as tk" we are giving a short name to use
import tkinter as tk

#Main Window
root = tk.Tk() #Creates the standard main window

#Three stages to build elements/objects
#1. CONSTRUCT the object: We Build and configure it.
#2. Configure the Object: We specify behaviours and settings (OPTIONAL)
#3. Pack the Object: Put it in the window


output = tk.Text(root,height = 10, width = 30) 
#ordered parameters: The order we send them matters. (COMMON)
#named parameters: Javascript and Python specific
output.config(state = "disable", background = "blue")
output.grid(row = 0, column = 0, rowspan = 5)

labInput1 = tk.Label(root, text ="input 1")
labInput1.grid(row = 5, column = 0)

labInput2 = tk.Label(root, text="input 2")
labInput2.grid(row = 6, column = 0)

labInput3 = tk.Label(root, text="input 3")
labInput3.grid(row = 7, column = 0)

var1 = tk.IntVar()
var2 = tk.IntVar()


cHC = tk.Checkbutton(root, text="Expand", variable=var1)
cHC.grid(row = 0, column = 1)

cLF = tk.Checkbutton(root, text="Expand", variable=var2)
cLF.grid(row=1, column=1)
#We are writing an EVENT DRIVE PROGRAM
#Build the GUI
#Start it running
#Wait for "EVENT"
root.mainloop()