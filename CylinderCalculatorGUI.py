import tkinter as tk
import math


def submit():

	print("Submit pressed")
	r = float(entr.get())
	h = float(enth.get())

	v = math.pi*r*r*h
	v = round(v,3)

	output.config(state="normal")

	OutputValue = "Given\nradius:"+str(r)+" units\nheight:"+str(h)+" units\nThe Volume Is:"+str(v)+" units cubed\n\n"

	output.delete(1.0,tk.END)
	output.insert(tk.INSERT, OutputValue)
	output.config(state="disabled")







root = tk.Tk() #add a Root Window
root.title("Volume of a cylinder")


labr = tk.Label(root, text="radius")
labr.pack()

entr = tk.Entry(root)
entr.pack()

labh = tk.Label(root, text="height")
labh.pack()

enth = tk.Entry(root)
enth.pack()

btn = tk.Button(root, text="Submit", command=submit)
btn.pack()

output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()









root.mainloop() #Displays Window, and sets up an "event"