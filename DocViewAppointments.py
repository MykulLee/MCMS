import tkinter as tk
from tkinter import ttk
import csv

def view_appointments_doc():
    def view_appointments():
        view_window = tk.Tk()
        view_window.title("View Appointments")

        tree = ttk.Treeview(view_window)
        tree["columns"] = ("Patient Name", "Reason", "Doctor")
        tree.heading("#0", text="Appointment ID")
        tree.column("#0", anchor="center", width=50)

        for col in tree["columns"]:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=100)

        with open('Appointments.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            for row_id, row in enumerate(reader, start=1):
                try:
                    # Use the actual column names from your CSV file
                    tree.insert("", "end", iid=row_id, text=row_id, values=(
                        row["Patient Name"],
                        row["Reason"],
                        row["Doctor"]
                    ))
                except KeyError as e:
                    print(f"KeyError: {e} not found in the row.")

        tree.pack(padx=10, pady=10)
        view_window.mainloop()

    # Run the view_appointments function when the script is executed
    view_appointments()
