import tkinter as tk
import math


def change():
	print ("Change")
	print (v.get())



root = tk.Tk()
root.title("SaveMoney")


MODES = [
("Corporate Tax", "n*1.15"),
("Goods and Services Tax", "n*1.05"),
]

v = tk.StringVar()
v.set("15%")

for r in range(0,len(MODES),1):
	b = tk.Radiobutton(root, text=MODES[r][0], variable=v, value=MODES[r][1], command = change)
	b.pack(anchor=tk.W)

frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="QUIT", fg="red", command=quit)
button.config(width = 6, height = 1)
button.grid(row = 1, column = 0, sticky = "NESW")
button.pack(side=tk.LEFT)


root.mainloop()