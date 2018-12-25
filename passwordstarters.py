import tkinter as tk

#####################(Variables)###################
def onReturn(event):
	
	value = entry1.get();

	entry1.delete(0, 'end')

	if value == "XK8KSKAK":
		print("Hi, Steven")
	else:
		print("Sorry, You are not Permitted")
root = tk.Tk()
root.title("GUI Entry With Return")

#####################(Widget)#####################
entry1 = tk.Entry(root)
entry1.bind("<Return>", onReturn)
entry1.pack()

entry2 = tk.Entry(root)

root.mainloop()