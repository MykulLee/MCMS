import csv
import tkinter as tk

def ManagementReportFunction():
    def count_doctors(filename):
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)  # Skip the header row
            return sum(1 for row in reader)

    def count_patients_by_reason(filename):
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            reason_count = {}
            for row in reader:
                reason = row['Reason']
                reason_count[reason] = reason_count.get(reason, 0) + 1
            return reason_count

    def display_counts():
        doctor_count = count_doctors('doctors.csv')
        patient_counts = count_patients_by_reason('Appointments.csv')

        display_text = f"Total Number of Doctors: {doctor_count}\n\n"
        display_text += "Total Number of Patients by Reason:\n"
        for reason, count in patient_counts.items():
            display_text += f"{reason}: {count}\n"
        label.config(text=display_text)

    # Create the main window
    root = tk.Tk()
    root.title("Management Report")

    # Create a label to display the counts
    label = tk.Label(root, justify=tk.LEFT)
    label.pack(pady=20)

    # Automatically update the label with the counts
    display_counts()

    # Start the GUI event loop
    root.mainloop()

