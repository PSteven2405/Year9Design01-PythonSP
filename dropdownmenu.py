import tkinter as tk

root = tk.Tk()
Frame = tk.Frame()
root.title("Tk dropdown example")

mainframe = tk.Frame(root)
mainframe.grid(column=0, sticky="NWES" )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

tkvar =tk.StringVar(root)

choices = { 'Pizza', 'Lasagne', 'Fries', 'Fish', 'Potatoe'}
tkvar.set('Pizza')

popupMenu =tk.OptionMenu(mainframe, tkvar, *choices)
tk.Label(mainframe, text="Choose a Dish").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column = 1)

def change_dropdown(*args):
	print( tkvar.get())

tkvar.trace('w', change_dropdown)

root.mainloop()