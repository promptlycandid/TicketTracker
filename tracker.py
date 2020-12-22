import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import pandas as pd 

# Build the widget
class App(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()

master = App()

# Window configurations
master.master.title("Ticket Tracker")
master.master.geometry("1000x500")
#master.configure(bg="#F9EBEA")


############# FUNCTIONS #####################################################

### New Ticket Function ###
def newTicket():
	nTicket = App()

	# Submit button function
	def submitTicket():
		path = "TicketTracker.ods"

		# Read the Ticket Tracker sheet into a dataframe
		df1 = pd.read_excel(path, index_col=None, header=0)

		# assign each column from the dataframe a different variable
		SeriesA = df1['Location']
		SeriesB = df1['Priority']
		SeriesC = df1['Open Date']
		SeriesD = df1['Issue']
		SeriesE = df1['Tech']
		SeriesF = df1['Fix']
		SeriesG = df1['Fix Date']
		SeriesH = df1['Closed']

		# Get the text from the form fields and assign them to a variable
		A = pd.Series(entry1.get())
		B = pd.Series(entry2.get())
		C = pd.Series(entry3.get())
		D = pd.Series(entry4.get())
		E = pd.Series(entry5.get())
		F = pd.Series(entry6.get())
		G = pd.Series(entry7.get())
		H = pd.Series(entry8.get())

		# Assign the form field entries to the worksheet dataframes
		SeriesA = SeriesA.append(A)
		SeriesB = SeriesB.append(B)
		SeriesC = SeriesC.append(C)
		SeriesD = SeriesD.append(D)
		SeriesE = SeriesE.append(E)
		SeriesF = SeriesF.append(F)
		SeriesG = SeriesG.append(G)
		SeriesH = SeriesH.append(H)

		# Create a new dataframe so as to not overwrite the old data in the sheet
		df2 = pd.DataFrame({"Location":SeriesA, "Priority":SeriesB, "Open Date":SeriesC, "Issue":SeriesD, "Tech":SeriesE, "Fix":SeriesF, "Fix Date":SeriesG, "Closed":SeriesH})

		# Write the new dataframe to the worksheet
		df2.to_excel(path, index=False)

		# Clear form fields for new data
		entry1.delete(0, tk.END)
		entry2.delete(0, tk.END)
		entry3.delete(0, tk.END)
		entry4.delete(0, tk.END)
		entry5.delete(0, tk.END)
		entry6.delete(0, tk.END)
		entry7.delete(0, tk.END)
		entry8.delete(0, tk.END)

	# Create widget labels
	ttk.Label(nTicket, text="Location", ).grid(row=0, pady=4)
	ttk.Label(nTicket, text="Priority").grid(row=1, pady=4)
	ttk.Label(nTicket, text="Open Date").grid(row=2, pady=4)
	ttk.Label(nTicket, text="Issue").grid(row=3, pady=4)
	ttk.Label(nTicket, text="Tech").grid(row=4, pady=4)
	ttk.Label(nTicket, text="Fix").grid(row=5, pady=4)
	ttk.Label(nTicket, text="Fix Date").grid(row=6, pady=4)
	ttk.Label(nTicket, text="Closed").grid(row=7, pady=4)

	# Create widget data entry fields
	entry1 = ttk.Entry(nTicket)
	entry2 = ttk.Entry(nTicket)
	entry3 = ttk.Entry(nTicket)
	entry4 = ttk.Entry(nTicket)
	entry5 = ttk.Entry(nTicket)
	entry6 = ttk.Entry(nTicket)
	entry7 = ttk.Entry(nTicket)
	entry8 = ttk.Entry(nTicket)

	# Place data entry fields in widget
	entry1.grid(row=0, column=1)
	entry2.grid(row=1, column=1)
	entry3.grid(row=2, column=1)
	entry4.grid(row=3, column=1)
	entry5.grid(row=4, column=1)
	entry6.grid(row=5, column=1)
	entry7.grid(row=6, column=1)
	entry8.grid(row=7, column=1)

	# Create button to submit data to worksheet
	tk.Button(nTicket, text='Submit', command=submitTicket, height=2, width=50, bg="#AED6F1").grid(row=9, column=1, pady=4)


### TODO: View Tickets Function ###
def viewTickets():
	oTicket = tk.Tk()
	oTicket.geometry("1500x1000")
	oTicket.pack_propagate(False)
	oTicket.resizable(0, 0)

	def clear_data():
		tv1.delete(*tv1.get_children())

	oTicket.title("All Tickets")


	# Frame for Treeview
	frame1 = tk.LabelFrame(oTicket, text="Ticket Data")
	frame1.place(height=1000, width=1500)

	# Treeview Widget
	tv1 = ttk.Treeview(frame1)
	tv1.place(relheight=1, relwidth=1)

	treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview)
	treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview)
	tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
	treescrollx.pack(side="bottom", fill="x")
	treescrolly.pack(side="right", fill="y")

	file_path = "TicketTracker.ods"
	excel_filename = r"{}".format(file_path)
	df = pd.read_excel(excel_filename)

	clear_data()
	tv1["column"] = list(df.columns)
	tv1["show"] = "headings"
	for column in tv1["columns"]:
		tv1.heading(column, text=column)

	df_rows = df.to_numpy().tolist()
	for row in df_rows:
		tv1.insert("", "end", values=row)
	return None

### Open Tickets Function ###
def openTickets():
	oTicket = tk.Tk()
	oTicket.geometry("1500x1000")
	oTicket.pack_propagate(False)
	oTicket.resizable(0, 0)

	def clear_data():
		tv1.delete(*tv1.get_children())

	oTicket.title("Open Tickets")


	# Frame for Treeview
	frame1 = tk.LabelFrame(oTicket, text="Ticket Data")
	frame1.place(height=1000, width=1500)

	# Treeview Widget
	tv1 = ttk.Treeview(frame1)
	tv1.place(relheight=1, relwidth=1)

	treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview)
	treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview)
	tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
	treescrollx.pack(side="bottom", fill="x")
	treescrolly.pack(side="right", fill="y")

	# Read file with Pandas
	file_path = "TicketTracker.ods"
	excel_filename = r"{}".format(file_path)
	df = pd.read_excel(excel_filename)
	open_tickets = df.loc[df['Closed'] != 'X']
	

	clear_data()
	tv1["column"] = list(open_tickets.columns)
	tv1["show"] = "headings"
	for column in tv1["columns"]:
		tv1.heading(column, text=column)

	df_rows = open_tickets.to_numpy().tolist()
	for row in df_rows:
		tv1.insert("", "end", values=row)
	return None


### TODO: Close Ticket Function

### TODO: Edit Ticket Function







########### MENU BUTTONS ###########################



# Ticket Tracker main menu buttons
tk.Button(master, text='New Ticket', command=newTicket).grid(row=6, column=0, pady=4)
tk.Button(master, text='View Tickets', command=viewTickets).grid(row=6, column=1, pady=4)
tk.Button(master, text='Open Tickets', command=openTickets).grid(row=6, column=2, pady=4)
# TODO: tk.Button(master, text='Edit Ticket', command=editTicket).grid(row=6, column=3, pady=4)
# TODO: tk.Button(master, text='Close Ticket', command=closeTicket).grid(row=6, column=4, pady=4)
tk.Button(master, text='Quit', command=master.quit).grid(row=6, column=5, pady=4)



master.mainloop()