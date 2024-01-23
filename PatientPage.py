import tkinter as tk
from tkinter import messagebox
from BookingApp import BookingAppFunction
from DocViewAppointments import view_appointments_doc
def PatientPageFunction():
    patientPage_window = tk.Toplevel()
    patientPage_window.title("Patient Page")

    book_button = tk.Button(patientPage_window, text="Book new appointment", command=on_book_clicked)
    book_button.pack(pady=5)

    view_button = tk.Button(patientPage_window, text="View existing appointments", command=on_view_clicked)
    view_button.pack(pady=5)

def on_book_clicked():
    BookingAppFunction()
def on_view_clicked():
    view_appointments_doc()

