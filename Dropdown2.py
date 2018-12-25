import tkinter as tk

root = tk.Tk()
root.title("Drop Down Menu 2")



var=tk.StringVar()

set1 = tk.OptionMenu(root, var, "CAD", "USD", "IDR")
var.set("Choose A Currency")

set1.config(font=("Arial", 13))
set1.grid(row=1, column=0)

root.mainloop()