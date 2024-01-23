import tkinter as tk

from RegisterDoctor2 import RegisterDoctorFunction
from ViewDoctors2 import view_doctors2
from DeleteDoctor import delete_doc
from PatientAssignDoctor import view_patients
from ViewPatientRecord import view_patient_record2
from UpdateDoctors import update_doc
from DeletePatient import delete_patient
from ManagementReport import ManagementReportFunction
def AdminPageFunction():
    def register_doctor():
        RegisterDoctorFunction()

    def view_doctors():
        view_doctors2()

    def update_doctor():
        update_doc()

    def delete_doctor():
        delete_doc()

    def view_patient_record():
        view_patient_record2()

    def assign_patient_to_doctor():
        view_patients()

    def discharge_patient():
        delete_patient()

    def management_report():
        ManagementReportFunction()

    root = tk.Tk()
    root.title("Admin Page")

    #Makes a Doctor frame inside the root
    doctor_frame = tk.Frame(root)
    doctor_frame.pack(side=tk.TOP, padx=10, pady=10)

    #Creates doctor buttons
    register_button = tk.Button(doctor_frame, text="Register a Doctor", command=register_doctor)
    register_button.grid(row=0, column=0, padx=5)

    view_button = tk.Button(doctor_frame, text="View Doctors", command=view_doctors)
    view_button.grid(row=0, column=1, padx=5)

    update_button = tk.Button(doctor_frame, text="Update Doctor", command=update_doctor)
    update_button.grid(row=0, column=2, padx=5)

    delete_button = tk.Button(doctor_frame, text="Delete Doctor", command=delete_doctor)
    delete_button.grid(row=0, column=3, padx=5)

    #Makes patient frame inside the root
    patient_frame = tk.Frame(root)
    patient_frame.pack(side=tk.TOP, padx=10, pady=10)

    #Creates patient buttons
    view_patient_button = tk.Button(patient_frame, text="View Patient Record", command=view_patient_record)
    view_patient_button.grid(row=0, column=0, padx=5)

    assign_patient_button = tk.Button(patient_frame, text="Assign Patient to a Doctor", command=assign_patient_to_doctor)
    assign_patient_button.grid(row=0, column=1, padx=5)

    discharge_patient_button = tk.Button(patient_frame, text="Discharge Patient", command=discharge_patient)
    discharge_patient_button.grid(row=0, column=2, padx=5)

    managementReport_button = tk.Button(patient_frame, text="Get management report", command=management_report)
    managementReport_button.grid(row=0, column=3, padx=5)

    root.mainloop()
