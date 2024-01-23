import tkinter as tk
from tkinter import messagebox
import csv

from AdminPage import AdminPageFunction
from DoctorPage import DoctorPageFunction
from PatientDataEntry import PatientDataEntryFunction
from PatientPage import PatientPageFunction

def admin_login():
    admin_window = tk.Toplevel(root)
    admin_window.title("Admin Login")

    def login():
        username = entry_username.get()
        password = entry_password.get()

        if username == "" or password == "":
            messagebox.showinfo('Error', 'Please input a username and password')
        else:
            x = 0
            with open('Admin Logins.csv') as csv_file:
                csv_file = csv.reader(csv_file)
                for row in csv_file:
                    if x == 0:
                        for field in row:
                            if field == username and row[1] == password and x == 0:
                                messagebox.showinfo('Login', 'Logged in Successfully')
                                x = 1
                                AdminPageFunction()
                                break

    text1 = tk.Label(admin_window, text="Username:")
    text1.grid(row=0, column=0, padx=10, pady=10)
    entry_username = tk.Entry(admin_window)
    entry_username.grid(row=0, column=1, padx=10, pady=10)

    text2 = tk.Label(admin_window, text="Password:")
    text2.grid(row=1, column=0, padx=10, pady=10)
    entry_password = tk.Entry(admin_window, show="*")
    entry_password.grid(row=1, column=1, padx=10, pady=10)

    submit_button = tk.Button(admin_window, text="Submit", command=login)
    submit_button.grid(row=2, column=0, columnspan=2, pady=10)

def doctor_login():
    doctor_window = tk.Toplevel(root)
    doctor_window.title("Doctor Login")

    def login():
        username = entry_username.get()
        password = entry_password.get()

        if username == "" or password == "":
            messagebox.showinfo('Error', 'Please input a username and password')
        else:
            x = 0
            with open('Doctor Logins.csv') as csv_file:
                csv_file = csv.reader(csv_file)
                for row in csv_file:
                    if x == 0:
                        for field in row:
                            if field == username and row[1] == password and x == 0:
                                messagebox.showinfo('Login', 'Logged in Successfully')
                                x = 1
                                DoctorPageFunction()
                                break

    text1 = tk.Label(doctor_window, text="Username:")
    text1.grid(row=0, column=0, padx=10, pady=10)
    entry_username = tk.Entry(doctor_window)
    entry_username.grid(row=0, column=1, padx=10, pady=10)

    text2 = tk.Label(doctor_window, text="Password:")
    text2.grid(row=1, column=0, padx=10, pady=10)
    entry_password = tk.Entry(doctor_window, show="*")
    entry_password.grid(row=1, column=1, padx=10, pady=10)

    submit_button = tk.Button(doctor_window, text="Submit", command=login)
    submit_button.grid(row=2, column=0, columnspan=2, pady=10)

def patient_login():
    patient_window = tk.Toplevel(root)
    patient_window.title("Patient Login")

    def register():
        PatientDataEntryFunction()

    def login():
        username = entry_username.get()
        password = entry_password.get()

        if username == "" or password == "":
            messagebox.showinfo('Error', 'Please input a username and password')
        else:
            x = 0
            with open('Patient Logins.csv') as csv_file:
                csv_file = csv.reader(csv_file)
                for row in csv_file:
                    if x == 0:
                        for field in row:
                            if field == username and row[1] == password and x == 0:
                                messagebox.showinfo('Login', 'Logged in Successfully')
                                x = 1
                                PatientPageFunction()
                                break

    text1 = tk.Label(patient_window, text="Username:")
    text1.grid(row=0, column=0, padx=10, pady=10)
    entry_username = tk.Entry(patient_window)
    entry_username.grid(row=0, column=1, padx=10, pady=10)

    text2 = tk.Label(patient_window, text="Password:")
    text2.grid(row=1, column=0, padx=10, pady=10)
    entry_password = tk.Entry(patient_window, show="*")
    entry_password.grid(row=1, column=1, padx=10, pady=10)

    login_button = tk.Button(patient_window, text="Login", command=login)
    login_button.grid(row=2, column=0, columnspan=2, pady=10)

    register_button = tk.Button(patient_window, text="Register", command=register)
    register_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create the main window
root = tk.Tk()
root.title("Medical Centre Management System")

# Create and configure the buttons
admin_button = tk.Button(root, text="Admin", command=admin_login, width=20, height=2)
admin_button.pack(pady=10)

doctor_button = tk.Button(root, text="Doctor", command=doctor_login, width=20, height=2)
doctor_button.pack(pady=10)

patient_button = tk.Button(root, text="Patient", command=patient_login, width=20, height=2)
patient_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()