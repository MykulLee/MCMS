def PatientDataEntryFunction():
    import tkinter as tk
    from tkinter import ttk  # Themed Tkinter
    from tkinter import messagebox
    import csv

    def submit_form():
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        # Checking if firstname and last name are entered and not left blank
        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            address = address_entry.get()
            phone = phoneNum_entry.get()
            username = username_entry.get()
            password = password_entry.get()

            # Save user information to a CSV file

            # Opens a CSV file named 'patient_data.csv' in append mode or creates it if it doesn't exist and defines the field names
            with open('patient_data.csv', 'a', newline='') as csvfile:
                fieldnames = ['First Name', 'Last Name', 'Title', 'Age', 'Address', 'Phone Number', 'Username',
                              'Password']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                # Checks if the file is empty and write headers if needed
                if csvfile.tell() == 0:
                    writer.writeheader()

                # Write user data to the CSV file
                writer.writerow({'First Name': firstname, 'Last Name': lastname, 'Title': title,
                                 'Age': age, 'Address': address, 'Phone Number': phone,
                                 'Username': username, 'Password': password})

            with open('Patient Logins.csv', 'a', newline='') as loginfile:
                loginfieldnames = ['Username', 'Password']
                loginwriter = csv.DictWriter(loginfile, fieldnames=loginfieldnames)

                # Checks if the file is empty and write headers if needed
                if loginfile.tell() == 0:
                    loginwriter.writeheader()

                # Write login data to the CSV file
                loginwriter.writerow({'Username': username, 'Password': password})

            tk.messagebox.showinfo(title="Form Submitted", message="User information saved successfully.")
        else:
            tk.messagebox.showwarning(title="Invalid entry", message="First name and last name are required")

    window = tk.Tk()
    window.title("Patient Data Entry")

    # Parent is window
    frame = tk.Frame(window)
    frame.pack()

    # Saving User Info
    user_info_frame = tk.LabelFrame(frame, text="User Information")
    user_info_frame.grid(row=0, column=0, padx=30, pady=20)

    # Existing code...
    first_name_label = tk.Label(user_info_frame, text="First Name")
    first_name_label.grid(row=0, column=0)
    last_name_label = tk.Label(user_info_frame, text="Last Name")
    last_name_label.grid(row=0, column=1)

    first_name_entry = tk.Entry(user_info_frame)
    last_name_entry = tk.Entry(user_info_frame)
    first_name_entry.grid(row=1, column=0)
    last_name_entry.grid(row=1, column=1)

    title_label = tk.Label(user_info_frame, text="Title")
    title_combobox = ttk.Combobox(user_info_frame, values=["Mr.", "Mrs.", "Ms.", "Dr.", "Miss"])
    title_label.grid(row=0, column=2)
    title_combobox.grid(row=1, column=2)

    age_label = tk.Label(user_info_frame, text="Age")
    age_spinbox = tk.Spinbox(user_info_frame, from_=0, to=110)
    age_label.grid(row=2, column=0)
    age_spinbox.grid(row=3, column=0)

    address_label = tk.Label(user_info_frame, text="Address (Postcode)")
    address_label.grid(row=2, column=1)
    address_entry = tk.Entry(user_info_frame)
    address_entry.grid(row=3, column=1)

    phoneNum_label = tk.Label(user_info_frame, text="Mobile Number")
    phoneNum_label.grid(row=2, column=2)
    phoneNum_entry = tk.Entry(user_info_frame)
    phoneNum_entry.grid(row=3, column=2)

    username_label = tk.Label(user_info_frame, text="Username")
    password_label = tk.Label(user_info_frame, text="Password")
    username_entry = tk.Entry(user_info_frame)
    password_entry = tk.Entry(user_info_frame, show="*")

    username_label.grid(row=4, column=0)
    password_label.grid(row=4, column=1)
    username_entry.grid(row=5, column=0)
    password_entry.grid(row=5, column=1)

    # Formatting
    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    # Submit Button
    submit = tk.Button(frame, text="Submit Form", command=submit_form)
    submit.grid(row=3, column=0)

    window.mainloop()
