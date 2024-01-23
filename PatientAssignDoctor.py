import tkinter as tk
from tkinter import ttk
import csv
def view_patients():
    def assign_patient():
        selected_item = tree.focus()
        if selected_item:
            patient_info = tree.item(selected_item, 'values')
            appointment_info = [patient_info[0], patient_info[6], patient_info[7]]  # [Patient Name, Doctor, Reason]

            with open('Appointments.csv', 'a', newline='') as appointments_file:
                appointments_writer = csv.writer(appointments_file)
                appointments_writer.writerow(appointment_info)

    def update_doctor(event):
        # Update the doctor column in the treeview when the dropdown selection changes
        selected_item = tree.focus()
        if selected_item:
            tree.item(selected_item, values=(tree.item(selected_item, 'values')[:-1] + (doctor_var.get(),)))


    view_window = tk.Tk()
    view_window.title("View Patients")

    tree = ttk.Treeview(view_window)
    tree["columns"] = ("First Name", "Last Name", "Title", "Age", "Address", "Phone Number", "Reason", "Doctor")
    tree.heading("#0", text="Patient ID")
    tree.column("#0", anchor="center", width=50)

    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=100)

    # Read doctors from Doctors.csv
    doctors = []
    with open('Doctors.csv', 'r') as doctor_file:
        doctor_reader = csv.DictReader(doctor_file)
        for doctor_row in doctor_reader:
            doctors.append(doctor_row['First Name'])

    # Create a dropdown menu for doctors
    doctor_var = tk.StringVar(view_window)
    doctor_var.set(doctors[0])  # Set the default value

    doctor_menu = ttk.Combobox(view_window, textvariable=doctor_var, values=doctors)
    doctor_menu.pack(pady=10)

    # Bind the dropdown menu change event to update_doctor function
    doctor_menu.bind("<<ComboboxSelected>>", update_doctor)

    with open('patient_bookings.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row_id, row in enumerate(reader, start=1):
            tree.insert("", "end", iid=row_id, text=row_id, values=(
                row["First Name"], row["Last Name"], row["Title"],
                row["Age"], row["Address"], row["Phone Number"], row["Reason"],
                doctor_var.get()
            ))

    tree.pack(padx=10, pady=10)

    # Add Assign Patient button
    assign_button = tk.Button(view_window, text="Assign Patient", command=assign_patient)
    assign_button.pack(side=tk.BOTTOM, pady=10, padx=10)

    view_window.mainloop()
