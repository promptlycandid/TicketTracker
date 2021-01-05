import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.commondialog import Dialog
from tkcalendar import Calendar, DateEntry

import pandas as pd

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
