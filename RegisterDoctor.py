def RegisterDoctorFunction():
    import tkinter as tk
    from tkinter import ttk #Themed Tkinter
    from tkinter import messagebox
    import csv

    def submit_form():
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        #Checking if firstname and last name are entered and not left blank
        if firstname and lastname:
            title = title_combobox.get()
            address = address_entry.get()
            phone = phoneNum_entry.get()
            speciality = speciality_combobox.get()


            #Save user information to a CSV file

            #Opens a CSV file named 'patient_data.csv' in append mode or creates it if it doesn't exist and defines the field names
            with open('patient_data.csv', 'a', newline='') as csvfile:
                fieldnames = ['First Name', 'Last Name', 'Title', 'Address', 'Phone Number', 'Symptoms']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                #Checks if the file is empty and write headers if needed
                if csvfile.tell() == 0:
                    writer.writeheader()

                #Write user data to the CSV file
                writer.writerow({'First Name': firstname, 'Last Name': lastname, 'Title': title, 'Address': address, 'Phone Number': phone,})

            tk.messagebox.showinfo(title="Form Submitted", message="User information saved successfully.")
        else:
            tk.messagebox.showwarning(title="Invalid entry", message="First name and last name are required")

    window = tk.Tk()
    window.title("Patient Data Entry")

    #Parent is window where the frame resides in
    frame = tk.Frame(window)
    frame.pack()

    #Saving User Info
    doctor_info_frame = tk.LabelFrame(frame, text="Doctor's Information")
    doctor_info_frame.grid(row=0, column=0, padx=20, pady=20)

    # Create a separate frame for doctor's information widgets
    doctor_widgets_frame = tk.Frame(doctor_info_frame)
    doctor_widgets_frame.grid(row=0, column=0)

    first_name_label = tk.Label(doctor_widgets_frame, text="First Name")
    first_name_label.grid(row=0, column=0)

    last_name_label = tk.Label(doctor_widgets_frame, text="Last Name")
    last_name_label.grid(row=0, column=1)

    first_name_entry = tk.Entry(doctor_widgets_frame)
    last_name_entry = tk.Entry(doctor_widgets_frame)
    first_name_entry.grid(row=1, column=0)
    last_name_entry.grid(row=1, column=1)

    title_label = tk.Label(doctor_widgets_frame, text="Title")
    title_combobox = ttk.Combobox(doctor_widgets_frame, values=["Mr.", "Mrs.", "Ms.", "Dr.", "Miss"])
    title_label.grid(row=0, column=2)
    title_combobox.grid(row=1, column=2)

    speciality_label = tk.Label(doctor_widgets_frame, text="Speciality")
    speciality_combobox = tk.Combobox(doctor_widgets_frame, values=["Cold Symptoms", "Sports Injury", "Respiratory Issue", "Vaccine", "Skin Disorder", "Cholestrol Issue"])
    speciality_label.grid(row=2, column=0)
    speciality_combobox.grid(row=3, column=0)

    address_label = tk.Label(doctor_widgets_frame, text="Address (Postcode)")
    address_label.grid(row=2, column=1)
    address_entry = tk.Entry(doctor_widgets_frame)
    address_entry.grid(row=3, column=1)

    phoneNum_label = tk.Label(doctor_widgets_frame, text="Mobile Number")
    phoneNum_label.grid(row=2, column=2)
    phoneNum_entry = tk.Entry(doctor_widgets_frame)
    phoneNum_entry.grid(row=3, column=2)

    #Formatting
    for widget in doctor_widgets_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    #Submit Button
    submit = tk.Button(doctor_widgets_frame, text= "Submit Form", command = submit_form)
    submit.grid(row=3, column=0)

    window.mainloop()
