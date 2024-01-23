import tkinter as tk
from tkinter import ttk
import csv

def view_doctors2():
    view_window = tk.Tk()
    view_window.title("View Doctors")

    tree = ttk.Treeview(view_window)
    tree["columns"] = ("First Name", "Last Name", "Title", "Age", "Address", "Phone Number", "Speciality")
    tree.heading("#0", text="Doctor ID")
    tree.column("#0", anchor="center", width=50)

    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=100)

    with open('Doctors.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row_id, row in enumerate(reader, start=1):
            tree.insert("", "end", iid=row_id, text=row_id, values=(
                row["First Name"], row["Last Name"], row["Title"],
                row["Age"], row["Address"], row["Phone Number"], row["Speciality"]
            ))

    tree.pack(padx=10, pady=10)

    view_window.mainloop()
