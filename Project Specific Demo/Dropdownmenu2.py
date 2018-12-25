import tkinter as tk

root = tk.Tk()
root.title("Drop Down Menu 2")

tk.Label(root, text="Basic Dropdown List").grid(row=0)

var=tk.StringVar()

set1 = tk.OptionMenu(root, var, "1", "2", "3")


set1.config(font=("Arial", 25))
set1.grid(row=1, column=0)

root.mainloop()