import tkinter as tk
from ViewPatientRecord import view_patient_record2
from DocViewAppointments import view_appointments_doc
def DoctorPageFunction():
    def view_patient_record():
        view_patient_record2()

    def view_appointments():
        view_appointments_doc()

    root = tk.Tk()
    root.title("Doctor Page")

    doctor_frame = tk.Frame(root)
    doctor_frame.pack(side=tk.TOP, padx=10, pady=10)

    view_patient_button = tk.Button(doctor_frame, text="View Patient Record", command=view_patient_record)
    view_patient_button.grid(row=0, column=0, padx=5)

    appointments_button = tk.Button(doctor_frame, text="View Appointments", command=view_appointments)
    appointments_button.grid(row=0, column=1, padx=5)

    root.mainloop()