import tkinter as tk
from tkinter import ttk, filedialog
from tkcalendar import Calendar, DateEntry
from collections import defaultdict

import pandas as pd

HEIGHT = 1000
WIDTH = 1200

class Application(tk.Frame):
	def __init__(self, root):
		self.root = root
		self.initialize_user_interface()

	def initialize_user_interface(self):
		# Configure the root object for the Application
		self.root.title("Ticket Tracker")

		self.canvas = tk.Canvas(self.root, height=HEIGHT, width=WIDTH)
		self.canvas.pack()

		# FRAMES

		self.frame1 = tk.Frame(self.root, bd=5) # bg='#96e4ff'
		self.frame1.place(rely=0, relx=0, relheight=0.4, relwidth=1)

		self.frame2 = tk.Frame(self.root, bd=5) # bg='#96e4ff'
		self.frame2.place(rely=0.4, relx=0, relheight=0.6, relwidth=1)

		# LABELS

		self.location_label = ttk.Label(self.frame1, text="Location", anchor='c')
		self.location_label.place(rely=0.05, relx=0.2, relheight=0.08, relwidth=0.1)
		self.priority_label = ttk.Label(self.frame1, text="Priority", anchor='c')
		self.priority_label.place(rely=0.15, relx=0.2, relheight=0.08, relwidth=0.1)
		self.openDate_label = ttk.Label(self.frame1, text="Open Date", anchor='c')
		self.openDate_label.place(rely=0.25, relx=0.2, relheight=0.08, relwidth=0.1)
		self.issue_label = ttk.Label(self.frame1, text="Issue", anchor='c')
		self.issue_label.place(rely=0.35, relx=0.2, relheight=0.08, relwidth=0.1)
		self.tech_label = ttk.Label(self.frame1, text="Assigned Tech", anchor='c')
		self.tech_label.place(rely=0.45, relx=0.2, relheight=0.08, relwidth=0.1)
		self.fix_label = ttk.Label(self.frame1, text="Fix", anchor='c')
		self.fix_label.place(rely=0.55, relx=0.2, relheight=0.08, relwidth=0.1)
		self.fixDate_label = ttk.Label(self.frame1, text="Fix Date", anchor='c')
		self.fixDate_label.place(rely=0.65, relx=0.2, relheight=0.08, relwidth=0.1)
		self.closed_label = ttk.Label(self.frame1, text="Closed", anchor='c')
		self.closed_label.place(rely=0.75, relx=0.2, relheight=0.08, relwidth=0.1)

		# ENTRY FIELDS

		self.location_entry = ttk.Entry(self.frame1)
		self.location_entry.place(rely=0.05, relx=0.3, relheight=0.08, relwidth=0.35)
		self.priority_entry = ttk.Entry(self.frame1)
		self.priority_entry.place(rely=0.15, relx=0.3, relheight=0.08, relwidth=0.35)
		self.openDate_entry = DateEntry(self.frame1)
		self.openDate_entry.place(rely=0.25, relx=0.3, relheight=0.08, relwidth=0.35)
		self.issue_entry = ttk.Entry(self.frame1)
		self.issue_entry.place(rely=0.35, relx=0.3, relheight=0.08, relwidth=0.35)
		self.tech_entry = ttk.Entry(self.frame1)
		self.tech_entry.place(rely=0.45, relx=0.3, relheight=0.08, relwidth=0.35)
		self.fix_entry = ttk.Entry(self.frame1)
		self.fix_entry.place(rely=0.55, relx=0.3, relheight=0.08, relwidth=0.35)
		self.fixDate_entry = DateEntry(self.frame1)
		self.fixDate_entry.place(rely=0.65, relx=0.3, relheight=0.08, relwidth=0.35)
		self.fixDate_entry.delete(0, tk.END)
		self.closedEntry = tk.IntVar() 
		self.closed_entry = tk.Checkbutton(self.frame1, variable=self.closedEntry, onvalue=1, offvalue=0, relief=tk.SOLID)
		self.closed_entry.place(rely=0.75, relx=0.3, relheight=0.08, relwidth=0.35)

		# BUTTONS

		self.submit_button = tk.Button(self.frame1, text="Submit", command=self.Submit_Ticket)
		self.submit_button.place(rely=1, relx=0.70, relheight=0.1, relwidth=0.1, anchor='se')
		self.save_button = tk.Button(self.frame1, text="Save")
		self.save_button.place(rely=1, relx=0.85, relheight=0.1, relwidth=0.1, anchor='se')
		self.delete_button = tk.Button(self.frame1, text="Delete", command=self.Delete_Ticket)
		self.delete_button.place(rely=1, relx=0, relheight=0.1, relwidth=0.1, anchor='sw')		
		self.exit_button = tk.Button(self.frame1, text="Exit", command=self.root.quit)
		self.exit_button.place(rely=1, relx=1, relheight=0.1, relwidth=0.1, anchor='se')

		# ===========================================
		# TREEVIEW
		# ===========================================

		self.tree = ttk.Treeview(self.frame2, columns=('Location', 'Priority', 'Opened Date', 'Issue', 'Assigned Tech', 'Fix', 'Fix Date', 'Closed'))
		self.tree.heading('#0', text='Ticket #')
		self.tree.heading('#1', text='Location')
		self.tree.heading('#2', text='Priority')
		self.tree.heading('#3', text='Opened Date')
		self.tree.heading('#4', text='Issue')
		self.tree.heading('#5', text='Assigned Tech')
		self.tree.heading('#6', text='Fix')
		self.tree.heading('#7', text='Fix Date')
		self.tree.heading('#8', text='Closed')

		for i in range(9):
			x = ("#" + str(i))
			self.tree.column(x, stretch=tk.YES)

		self.tree.place(rely=0, relx=0, relwidth=1, relheight=1)	
		self.treeview = self.tree

		self.treescrolly = tk.Scrollbar(self.frame2, orient="vertical", command=self.tree.yview)
		self.treescrollx = tk.Scrollbar(self.frame2, orient="horizontal", command=self.tree.xview)
		self.tree.configure(xscrollcommand=self.treescrollx.set, yscrollcommand=self.treescrolly.set)
		self.treescrollx.pack(side="bottom", fill="x")
		self.treescrolly.pack(side="right", fill="y")

		self.id = 1
		self.iid = 1

	# ======================================================================
	# BUTTON FUNCTIONS
	# ======================================================================

	def Submit_Ticket(self):
		# IF Statement to turn closed entry to Yes or No in table
		self.closed_yn = self.closedEntry.get()
		if self.closed_yn == 1:
			self.closedYN = "Yes"
		elif self.closed_yn == 0:
			self.closedYN = "No"

		# Insert entry fields into table
		self.treeview.insert('', 'end', iid=self.iid, text=self.id, values=(self.location_entry.get(), self.priority_entry.get(), self.openDate_entry.get(), self.issue_entry.get(), self.tech_entry.get(), self.fix_entry.get(), self.fixDate_entry.get(), self.closedYN))

		# Add one to the ticket number
		self.iid = self.iid +1
		self.id = self.id +1

		# Delete fields
		self.location_entry.delete(0, tk.END)
		self.priority_entry.delete(0, tk.END)
		self.issue_entry.delete(0, tk.END)
		self.tech_entry.delete(0, tk.END)
		self.fix_entry.delete(0, tk.END)
		self.fixDate_entry.delete(0, tk.END)
		self.closed_entry.deselect()

	def Delete_Ticket(self):
		ticket_num = int(self.tree.focus())
		self.treeview.delete(ticket_num)

	def Update(self):
		for idx, node in enumerate(self.treeview.get_children()):
			self.tree.item(node)

	


app = Application(tk.Tk())
app.root.mainloop()