import tkinter as tk
from tkinter import ttk #Themed Tkinter
from tkinter import messagebox
import csv

def RegisterDoctorFunction():

    def submit_booking():
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        #Checking if firstname and last name are entered and not left blank
        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            address = address_entry.get()
            phone = phoneNum_entry.get()
            speciality = speciality_combobox.get()

            #Save user information to a CSV file

            #Opens a CSV file named 'patient_bookings.csv' in append mode or creates it if it doesn't exist and defines the field names
            with open('Doctors.csv', 'a', newline='') as csvfile:
                fieldnames = ['First Name', 'Last Name', 'Title', 'Age', 'Address', 'Phone Number', 'speciality']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                #Checks if the file is empty and write headers if needed
                if csvfile.tell() == 0:
                    writer.writeheader()

                #Write user data to the CSV file
                writer.writerow({'First Name': firstname, 'Last Name': lastname, 'Title': title,
                                'Age': age, 'Address': address, 'Phone Number': phone, 'speciality' : speciality})

            tk.messagebox.showinfo(title="Registered", message="You have registered a doctor successfully")
        else:
            tk.messagebox.showwarning(title="Invalid entry", message="First name and last name are required")

    booking = tk.Tk()
    booking.title("Register a doctor")

    user_info_booking = tk.Label(booking, text="")
    user_info_booking.grid(row=0, column=0, padx=10, pady=10)

    first_name_label = tk.Label(user_info_booking, text="First Name")
    first_name_label.grid(row=0, column=0)
    last_name_label = tk.Label(user_info_booking, text="Last Name")
    last_name_label.grid(row=0, column=1)

    first_name_entry = tk.Entry(user_info_booking)
    last_name_entry = tk.Entry(user_info_booking)
    first_name_entry.grid(row=1, column=0)
    last_name_entry.grid(row=1, column=1)

    title_label = tk.Label(user_info_booking, text="Title")
    title_combobox = ttk.Combobox(user_info_booking, values=["Mr.", "Mrs.", "Ms.", "Dr.", "Miss"])
    title_label.grid(row=0, column=2)
    title_combobox.grid(row=1, column=2)

    age_label = tk.Label(user_info_booking, text="Age")
    age_spinbox = tk.Spinbox(user_info_booking, from_=0, to=110)
    age_label.grid(row=2, column=0)
    age_spinbox.grid(row=3, column=0)

    address_label = tk.Label(user_info_booking, text="Address (Postcode)")
    address_label.grid(row=2, column=1)
    address_entry = tk.Entry(user_info_booking)
    address_entry.grid(row=3, column=1)

    phoneNum_label = tk.Label(user_info_booking, text="Mobile Number")
    phoneNum_label.grid(row=2, column=2)
    phoneNum_entry = tk.Entry(user_info_booking)
    phoneNum_entry.grid(row=3, column=2)

    speciality_label = tk.Label(user_info_booking, text="Speciality")
    speciality_combobox = ttk.Combobox(user_info_booking, values=["Cold Symptoms", "Sports Injury", "Respiratory Issue", "Vaccine", "Skin Disorder", "Cholestrol Issue"])
    speciality_label.grid(row=4, column=1)
    speciality_combobox.grid(row=5, column=1)

    #Formatting
    for widget in user_info_booking.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    #Submit Button
    submit = tk.Button(booking, text= "Register", command = submit_booking)
    submit.grid(row=3, column=0)

    booking.mainloop()
