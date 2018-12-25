import tkinter as tk


 
root = tk.Tk()
frame = tk.Frame(root)
var = tk.StringVar()
root.title("Save Money")
def change_dropdown(*args):
	print( tkvar.get())
def SubmitItem():
	print("Item Submitted")
def SaveList():
	print("List Saved")
def ClearList():
	print("List Cleared")


#########################[Tax Checkboxes]################################
GaSTax = tk.Checkbutton(root, text="Goods and Services Tax")
GaSTax.grid(row = 1, column = 3, sticky="W")

CoTax = tk.Checkbutton(root, text="Corporate Tax")
CoTax.grid(row = 2, column = 3, sticky="W")
#########################[Currency Dropdown]#############################
DDC = tk.OptionMenu(root, var, "CAD", "USD", "IDR")
var.set("Choose A Currency")

DDC.config(font=("Arial", 13))
DDC.grid(row=3, column=3, sticky="W")
##############################[Labels]###################################
NoILab = tk.Label(text="Name of Item")
NoILab.grid(column=3, row=4,sticky="W")

DBLab = tk.Label(text="Date Bought")
DBLab.grid(row=6, column=3,sticky="W")

PoILab = tk.Label(text="Price of Item")
PoILab.grid(row=8, column=3, sticky="W")
##############################[Buttons]##################################
SLIBttn = tk.Button(root, text="      Submit Logged Item      ", command=SubmitItem)
SLIBttn.grid(column=3, row=10, columnspan=2, sticky="W")

SLBttn = tk.Button(root, text="   Save List   ", command=SaveList)
SLBttn.grid(column=3, row=11, sticky="W")

CLBttn = tk.Button(root, text="    Clear List  ", command=ClearList)
CLBttn.grid(column=3, row=11, sticky="E")

QBttn = tk.Button(root, text="                  QUIT                  ", command=quit)
QBttn.grid(column=3, row=12, sticky="W", columnspan=2)
###############################[Entry Boxes]#############################
NoIEntry = tk.Entry(root)
NoIEntry.grid(column=3, row=5, columnspan=2, sticky="W")

DBEntry = tk.Entry(root)
DBEntry.grid(column=3, row=7, columnspan=2, sticky="W")

PoIEntry = tk.Entry(root)
PoIEntry.grid(column=3, row=9, columnspan=2, sticky="W")

Output = tk.Text(root, width=30, height=20, borderwidth=3, relief=tk.GROOVE)
Output.config(state="disabled")
Output.grid(row=1, column=0, rowspan=11, columnspan=3)

root.mainloop()
