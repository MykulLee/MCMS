import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv

def delete_patient():
    def delete_patient(patient_id, view_window):
        with open('patient_data.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)

        with open('patient_data.csv', 'w', newline='') as csvfile:
            fieldnames = ["First Name", "Last Name", "Title", "Age", "Address", "Phone Number"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for row_id, row in enumerate(rows, start=1):
                if row_id != patient_id:
                    writer.writerow(row)

        messagebox.showinfo("Patient Deleted", "Patient successfully deleted.")
        view_window.destroy()
        view_patients()

    def confirm_delete(patient_id, view_window):
        confirm_window = tk.Tk()
        confirm_window.title("Confirm Deletion")

        label = tk.Label(confirm_window, text="Are you sure you want to delete this patient?")
        label.pack(padx=10, pady=10)

        yes_button = tk.Button(confirm_window, text="Yes", command=lambda: [confirm_window.destroy(), delete_patient(patient_id, view_window)])
        yes_button.pack(side="left", padx=5)

        no_button = tk.Button(confirm_window, text="No", command=confirm_window.destroy)
        no_button.pack(side="right", padx=5)

    def view_patients():
        view_window = tk.Tk()
        view_window.title("View Patients")

        tree = ttk.Treeview(view_window)
        tree["columns"] = ("First Name", "Last Name", "Title", "Age", "Address", "Phone Number")
        tree.heading("#0", text="Patient ID")
        tree.column("#0", anchor="center", width=50)

        for col in tree["columns"]:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=100)

        with open('patient_data.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row_id, row in enumerate(reader, start=1):
                tree.insert("", "end", iid=row_id, text=row_id, values=(
                    row["First Name"], row["Last Name"], row["Title"],
                    row["Age"], row["Address"], row["Phone Number"]
                ))

        def on_delete():
            selected_item = tree.selection()
            if selected_item:
                patient_id = int(tree.item(selected_item, "text"))
                confirm_delete(patient_id, view_window)
            else:
                messagebox.showwarning("No Patient Selected", "Please select a patient to delete.")

        delete_button = tk.Button(view_window, text="Discharge", command=on_delete)
        delete_button.pack(pady=10)

        tree.pack(padx=10, pady=10)

        view_window.mainloop()

    view_patients()

# You can call delete_patient() to start the application.
