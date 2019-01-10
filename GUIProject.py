import tkinter as tk
from tkinter import ttk

class Display:

	def __init__(self):

		
		def changevart1(*args):
			self.varT1.get()

		def changevart2(*args):
			self.varT2.get()
			

		def change_dropdown(*args):
			print( tkvar.get())
		def SubmitItem(*args):
			
			Item = self.NoIEntryT1.get()
			Date = self.DBEntryT1.get()
			Price = self.PoIEntryT1.get()

			if self.check1Var.get() == 1:

				if self.varT1.get() == "CAD":
					Price = float(Price)*(1.05)
				elif self.varT1.get() == "USD":
					Price = float(Price)*(1.075)
				elif self.varT1.get() == "SAR":
					Price = float(Price)*(1.05)
				elif self.varT1.get() == "IDR":
					Price = float(Price)*(1.1)

			DateItemPrice = "\n"+"("+Item+")"+","+" "+"["+"$"+str(Price)+"]"+","+" "+"{"+"Date Purchased:"+Date+"}"
			TotalPrice = "Total:"+"$"+str(Price)
			
			self.OutputT1.config(state="normal")
			self.OutputT1.insert(tk.INSERT, DateItemPrice)
			self.OutputT1.configure(state="disabled")
			

			self.OutputTotalT1.config(state="normal")
			self.OutputTotalT1.delete(1.0, tk.END)
			self.OutputTotalT1.insert(tk.INSERT, TotalPrice)
			self.OutputTotalT1.config(state="disabled")

			
			self.NoIEntryT1.delete(0, tk.END)
			self.DBEntryT1.delete(0, tk.END)
			self.PoIEntryT1.delete(0, tk.END)


			
			


		def SaveList():
			print("List Saved")
		def ClearList():
			
			self.OutputT1.config(state="normal")
			self.OutputT1.delete(1.0,tk.END)
			self.OutputT1.config(state="disabled")

			self.OutputTotalT1.config(state="normal")
			self.OutputTotalT1.delete(1.0,tk.END)
			self.OutputTotalT1.config(state="disabled")
		def SubmitIncome():
			self.OutputT2.delete(1.0, tk.END)

			Income = float(self.IPMEntryT2.get())

			IncomeOutput = "\n"+"Your Income:"+" "+"$"+str(Income)
			
			IncomeError = "Please Choose an Income Tax !!"
			if self.check2Var.get() == 1:

				if self.varT2.get() == "Income of $46,605 or Below":
					Income = float(Income)*(1.15)
				elif self.varT2.get() == "Income of $46,606 - $93,208":
					Income = float(Income)*(1.205)
				elif self.varT2.get() == "Income of $93,209 - $144,489":
					Income = float(Income)*(1.26)
				elif self.varT2.get() == "Income of $144,490 - $205,842":
					Income = float(Income)*(1.29)
				elif self.varT2.get() == "Over $205,842":
					Income = float(Income)*(1.33)
			if self.varT2.get() == "Choose Your Income Tax":

				self.OutputT2.config(state="normal")
				self.OutputT2.insert(tk.INSERT, IncomeError)
				self.OutputT2.config(state="disabled")	
			
			self.OutputT2.config(state="normal")
			self.OutputT2.insert(tk.INSERT, IncomeOutput)
			self.IPMEntryT2.delete(0, tk.END)
			self.OutputT2.config(state="disabled")
			
			

		def SubmitBill():
			print("Bill Submitted")

		def change1(*args):
			print(self.check1Var.get())

		def change2(*args):
			print(self.check2Var.get())

		self.root = tk.Tk()
		self.root.title("SaveMoney")


		OPTIONST1 = [

			"CAD",
			"USD",
			"IDR",
			"SAR"
		]

		OPTIONST2 = [

			"Choose Your Income Tax",
			"Income of $46,605 or Below",
			"Income of $46,606 - $93,208",
			"Income of $93,209 - $144,489",
			"Income of $144,490 - $205,842",
			"Over $205,842"
		]
		##################################################[Base Frame Codes]##################################
		self.frame = tk.Frame(self.root)
		
		self.varT1 = tk.StringVar()
		self.varT1.set("CAD")
		self.varT1.trace("w",changevart1)

		self.varT2 = tk.StringVar()
		self.varT2.trace("w", changevart2)
		self.tabControl = ttk.Notebook(self.root)


		self.tab1 = ttk.Frame(self.tabControl)
		self.tabControl.add(self.tab1, text="Spending Calculator")
		
		self.tab2 = ttk.Frame(self.tabControl)
		self.tabControl.add(self.tab2, text="Income Calculator")
		
		self.tabControl.pack(expand=1, fill="both")
		
		#[[[[[[[[[[[[[[[[[[[[[[[[Spending Calculator Variables]]]]]]]]]]]]]]]]]]]]]]]]
		#########################[Tax Checkboxes]################################
		self.check1Var = tk.IntVar()
		self.check1Var.trace("w",change1)
		self.GaSTaxT1 = tk.Checkbutton(self.tab1, text="Goods and Services Tax",var = self.check1Var )
		self.GaSTaxT1.grid(row = 1, column = 3, sticky="W")

		self.check2Var = tk.IntVar()
		self.check2Var.trace("w",change2)
		self.CoTaxT1 = tk.Checkbutton(self.tab1, text="Corporate Tax", var = self.check2Var )
		self.CoTaxT1.grid(row = 2, column = 3, sticky="W")
		#########################[Currency Dropdown Menu 1 and 2]########################
		self.DDCT1 = tk.OptionMenu(self.tab1,self.varT1, OPTIONST1[0], OPTIONST1[1], OPTIONST1[2], OPTIONST1[3])
		self.varT1.set("CAD")

		self.DDCT1.config(font=("Arial", 13))
		self.DDCT1.grid(row=3, column=3, sticky="W")

		self.DDCT2 = tk.OptionMenu(self.tab2,self.varT2, OPTIONST2[0], OPTIONST2[1], OPTIONST2[2], OPTIONST2[3], OPTIONST2[4], OPTIONST2[5])
		self.varT2.set(" Choose Your Income Tax ")

		self.DDCT2.config(font=("Arial", 13))
		self.DDCT2.grid(row=0, column=4, sticky="W")
		##############################[Labels]###################################
		self.NoILabT1 = tk.Label(self.tab1, text="Name of Item:")
		self.NoILabT1.grid(column=3, row=4,sticky="W")

		self.DBLabT1 = tk.Label(self.tab1, text="Date Bought:")
		self.DBLabT1.grid(row=6, column=3,sticky="W")

		self.PoILabT1 = tk.Label(self.tab1, text="Price of Item:")
		self.PoILabT1.grid(row=8, column=3, sticky="W")

		self.IPMLabT2 = tk.Label(self.tab2, text="Income Per Month:")
		self.IPMLabT2.grid(row=1, column=3, sticky="W")

		self.MBSLabT2 = tk.Label(self.tab2, text="Monthly Bills Section")
		self.MBSLabT2.grid(column=3, columnspan=2, row=3, sticky="N")

		self.NoBLabT2 = tk.Label(self.tab2, text="Name of Bill:")
		self.NoBLabT2.grid(column=3, row=4, sticky="W")

		self.BDDLabT2 = tk.Label(self.tab2, text="Bill Due Date:")
		self.BDDLabT2.grid(column=3, row=6, sticky="W")

		self.PoBLabT2 = tk.Label(self.tab2, text="Price of Bill:")
		self.PoBLabT2.grid(column=3, row=8, sticky="W")
		#################################[Buttons]###############################
		self.SLIBttnT1 = tk.Button(self.tab1, text="      Submit Logged Item      ", command=SubmitItem)
		self.SLIBttnT1.grid(column=3, row=10, columnspan=2, sticky="W")

		self.SLBttnT1 = tk.Button(self.tab1, text="   Save List   ", command=SaveList)
		self.SLBttnT1.grid(column=3, row=11, sticky="W")

		self.CLBttnT1 = tk.Button(self.tab1, text="    Clear List  ", command=ClearList)
		self.CLBttnT1.grid(column=3, row=11, sticky="E")

		self.QBttnT1 = tk.Button(self.tab1, text="                  QUIT                  ", command=quit)
		self.QBttnT1.grid(column=3, row=12, sticky="W", columnspan=2)

		self.SIBttnT2 = tk.Button(self.tab2, text="           Submit Income           ", command=SubmitIncome)
		self.SIBttnT2.grid(column=4, row=2, sticky="W")

		self.SBBttnT2 = tk.Button(self.tab2, text="              Submit Bill              ", command=SubmitBill)
		self.SBBttnT2.grid(column=3, row=10, sticky="W")
		#################################[Entry Tabs]############################
		self.NoIEntryT1 = tk.Entry(self.tab1)
		self.NoIEntryT1.grid(column=3, row=5, columnspan=2, sticky="W")

		self.DBEntryT1 = tk.Entry(self.tab1)
		self.DBEntryT1.grid(column=3, row=7, columnspan=2, sticky="W")

		self.PoIEntryT1 = tk.Entry(self.tab1)
		self.PoIEntryT1.grid(column=3, row=9, columnspan=2, sticky="W")

		self.IPMEntryT2 = tk.Entry(self.tab2)
		self.IPMEntryT2.grid(column=4, row=1, sticky="W")

		self.NoBEntryT2 = tk.Entry(self.tab2)
		self.NoBEntryT2.grid(column=3, columnspan=2, row=5, sticky="W")

		self.BDDEntryT2 = tk.Entry(self.tab2)
		self.BDDEntryT2.grid(column=3, columnspan=2, row=7, sticky="W")

		self.PoBEntryT2 = tk.Entry(self.tab2)
		self.PoBEntryT2.grid(column=3, columnspan=2, row=9, sticky="W")
		#################################[Output Tab (1 and 2)]############################
		self.OutputT1 = tk.Text(self.tab1, width=60, height=30, relief=tk.GROOVE)
		self.OutputT1.config(state="disabled")
		self.OutputT1.grid(row=1, column=0, rowspan=11, columnspan=3)

		self.OutputTotalT1 = tk.Text(self.tab1, width=60, height=1, relief=tk.GROOVE) 
		self.OutputTotalT1.config(state="disabled")
		self.OutputTotalT1.grid(row=12, column=0, columnspan=3)

		self.OutputT2 = tk.Text(self.tab2, width=60, height=30, borderwidth=3, relief=tk.GROOVE)
		self.OutputT2.config(state="disabled")
		self.OutputT2.grid(row=0, column=0, rowspan=11, columnspan=3,)		

		self.root.mainloop()



display = Display()