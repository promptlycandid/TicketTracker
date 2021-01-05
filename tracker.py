import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.commondialog import Dialog
from tkcalendar import Calendar, DateEntry

import pandas as pd

import ViewTickets

HEIGHT = 500
WIDTH = 1000

# Build the widget
root = tk.Tk()
root.title("Ticket Tracker")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame1 = tk.Frame(root, height=HEIGHT, width=WIDTH)
frame1.place(rely=0.05, relx=0, relwidth=1, relheight=1)

menu_frame = tk.Frame(root)
menu_frame.place(rely=0, relx=0, relwidth=1, relheight=0.05)

background_image = tk.PhotoImage(file='ProfilePic.png')
background_label = tk.Label(frame1, image=background_image, bg='#E15F5F')
background_label.place(relwidth=1, relheight=1)

# ===================================================================
# 							MENU
# ===================================================================

class Message(Dialog):
    "A message box"

    command  = "tk_messageBox"

def _show(title=None, message=None, _icon=None, _type=None, **options):
    if _icon and "icon" not in options:    options["icon"] = _icon
    if _type and "type" not in options:    options["type"] = _type
    if title:   options["title"] = title
    if message: options["message"] = message
    res = Message(**options).show()
    if isinstance(res, bool):
        if res:
            return YES
        return NO
    return str(res)

def aboutTracker(title="About Ticket Tracker", message="Ticket Tracker \n Version 1.0 \n Copyright 2020"):
	"Shows info about ticket tracker"
	return _show(title, message)

menubar = tk.Menu(menu_frame)

# File Menu
fileMenu = tk.Menu(menubar, tearoff=0)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=fileMenu)

# Edit Menu

# Help Menu
helpMenu = tk.Menu(menubar, tearoff=0)
helpMenu.add_command(label="About", command=aboutTracker)

menubar.add_cascade(label="Help", menu=helpMenu)

root.config(menu=menubar)

# ===================================================================
# ===================================================================
# 							FUNCTIONS
# ===================================================================
# ===================================================================

### New Ticket Function ###
def newTicket():
	nTicket = tk.Tk()
	nTicket.title("New Ticket")

	nCanvas = tk.Canvas(nTicket, height=600, width=800)
	nCanvas.pack()

	nFrame1 = tk.LabelFrame(nTicket, text=None)
	nFrame1.place(relwidth=1, relheight=1)

	# # Submit button function
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
		closed_var.deselect()

	# Create widget labels
	label1 = ttk.Label(nTicket, text="Location")
	label1.place(rely=0.1, relx=0.25, anchor='center')
	label1.config(font=("Helvetica", 16))

	label2 = ttk.Label(nTicket, text="Priority")
	label2.place(rely=0.2, relx=0.25, anchor='center')
	label2.config(font=("Helvetica", 16))

	label3 = ttk.Label(nTicket, text="Open Date")
	label3.place(rely=0.3, relx=0.25, anchor='center')
	label3.config(font=("Helvetica", 16))

	label4 = ttk.Label(nTicket, text="Issue")
	label4.place(rely=0.4, relx=0.25, anchor='center')
	label4.config(font=("Helvetica", 16))

	label5 = ttk.Label(nTicket, text="Tech")
	label5.place(rely=0.5, relx=0.25, anchor='center')
	label5.config(font=("Helvetica", 16))

	label6 = ttk.Label(nTicket, text="Fix")
	label6.place(rely=0.6, relx=0.25, anchor='center')
	label6.config(font=("Helvetica", 16))

	label7 = ttk.Label(nTicket, text="Fix Date")
	label7.place(rely=0.7, relx=0.25, anchor='center')
	label7.config(font=("Helvetica", 16))

	label8 = ttk.Label(nTicket, text="Closed")
	label8.place(rely=0.8, relx=0.25, anchor='center')
	label8.config(font=("Helvetica", 16))

	# Create widget data entry fields
	entry1 = ttk.Entry(nTicket)
	entry1.place(rely=0.1, relx=0.75, anchor='center', width=350, height=50)
	entry1.config(font=("Helvetica", 14,))

	entry2 = ttk.Entry(nTicket)
	entry2.place(rely=0.2, relx=0.75, anchor='center', width=350, height=50)
	entry2.config(font=("Helvetica", 14,))

	entry3 = DateEntry(nTicket)
	entry3.place(rely=0.3, relx=0.75, anchor='center', width=350, height=50)
	entry3.config(font=("Helvetica", 14,))

	entry4 = ttk.Entry(nTicket)
	entry4.place(rely=0.4, relx=0.75, anchor='center', width=350, height=50)
	entry4.config(font=("Helvetica", 14,))

	entry5 = ttk.Entry(nTicket)
	entry5.place(rely=0.5, relx=0.75, anchor='center', width=350, height=50)
	entry5.config(font=("Helvetica", 14,))

	entry6 = ttk.Entry(nTicket)
	entry6.place(rely=0.6, relx=0.75, anchor='center', width=350, height=50)
	entry6.config(font=("Helvetica", 14,))

	entry7 = DateEntry(nTicket)
	entry7.place(rely=0.7, relx=0.75, anchor='center', width=350, height=50)
	entry7.config(font=("Helvetica", 14,))
	entry7.delete(0, tk.END)

	# Ticket Closed Checkbox
	entry8 = tk.IntVar()
	closed_var = tk.Checkbutton(nTicket, variable=entry8, onvalue = True, offvalue = False)
	closed_var.place(rely=0.8, relx=0.75, relheight=0.1, relwidth=0.1, anchor='c')

	# Create button to submit data to worksheet
	cButton = tk.Button(nTicket, text='Submit', command=submitTicket, height=2, width=50, bg="#AED6F1")
	cButton.config(font=("Helvetica", 16))
	cButton.place(rely=0.9, relx=0.5, anchor='center', width=700, height=50)

# ===================================================================
# 			OPEN TICKETS
# ===================================================================
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
	open_tickets = df.loc[df['Closed'] == 0]
	

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

# ===================================================================
# 			MENU BUTTONS
# ===================================================================

button1 = tk.Button(frame1, text='New Ticket', command=newTicket, bd=5)
button1.place(rely=0.01, relx=0, relwidth=0.30, relheight=0.30)
button1.config(font=("Helvetica", 18))


button2 = tk.Button(frame1, text='View Tickets', command=ViewTickets.viewTickets, bd=5)
button2.place(rely=0.01, relx=0.35, relwidth=0.30, relheight=0.30)
button2.config(font=("Helvetica", 18))

button3 = tk.Button(frame1, text='Open Tickets', command=openTickets, bd=5)
button3.place(rely=0.01, relx=0.70, relwidth=0.30, relheight=0.30)
button3.config(font=("Helvetica", 18))

button4 = tk.Button(frame1, text='Edit Ticket', command=root.quit, bd=5)
button4.place(rely=0.94, relx=0,  relwidth=0.30, relheight=0.30, anchor='sw')
button4.config(font=("Helvetica", 18))

button5 = tk.Button(frame1, text='Close Ticket', command=root.quit, bd=5)
button5.place(rely=0.94, relx=0.35,  relwidth=0.30, relheight=0.30, anchor='sw')
button5.config(font=("Helvetica", 18))

button6 = tk.Button(frame1, text='Quit', command=root.quit, bd=5)
button6.place(rely=0.94, relx=0.70,  relwidth=0.30, relheight=0.30, anchor='sw')
button6.config(font=("Helvetica", 18))

# ===================================================================
# END PROGRAM LOOP
# ===================================================================
root.mainloop()