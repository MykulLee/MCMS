import tkinter as tk
from tkinter import ttk
import csv

def view_patient_record2():
    view_window = tk.Tk()
    view_window.title("View Patient Record")

    tree = ttk.Treeview(view_window)
    tree["columns"] = ("First Name", "Last Name", "Title", "Age", "Address", "Phone Number", "Reason")
    tree.heading("#0", text="Patient ID")
    tree.column("#0", anchor="center", width=50)

    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=100)

    with open('patient_bookings.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row_id, row in enumerate(reader, start=1):
            tree.insert("", "end", iid=row_id, text=row_id, values=(
                row["First Name"], row["Last Name"], row["Title"],
                row["Age"], row["Address"], row["Phone Number"], row["Reason"]
            ))

    tree.pack(padx=10, pady=10)

    view_window.mainloop()
