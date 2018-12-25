import tkinter as tk


root=tk.Tk

def main():
	total = 0.0
	print("this is the accumulator test run")
	while True:
		number= input("enter a number:")
		if number == 0:
			break
		total += number

	print("the total is", total)

root.mainloop()