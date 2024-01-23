import tkinter as tk
from tkinter import ttk
import csv

def update_doc():
    class DoctorApp:
        def __init__(self):
            self.root = tk.Tk()
            self.root.title("Doctors Information")

            #Creating treeview table in tkinter to show all the doctor data
            self.tree = ttk.Treeview(self.root, columns=(
            'First Name', 'Last Name', 'Title', 'Age', 'Address', 'Phone Number', 'Speciality'), show='headings')
            self.tree.heading('First Name', text='First Name')
            self.tree.heading('Last Name', text='Last Name')
            self.tree.heading('Title', text='Title')
            self.tree.heading('Age', text='Age')
            self.tree.heading('Address', text='Address')
            self.tree.heading('Phone Number', text='Phone Number')
            self.tree.heading('Speciality', text='Speciality')
            self.tree.pack()

            self.load_data()
            self.populate_tree()

            #Loads and populates the csv data into the tree

            update_button = tk.Button(self.root, text="Update Information", command=self.update_information)
            update_button.pack(pady=10)

            self.root.mainloop()

        #Loads data from Doctors.csv and storesit in the doctor_data attribute of the class
        def load_data(self):
            self.doctor_data = []
            with open('Doctors.csv', 'r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    self.doctor_data.append(row)

        def save_data(self):
            with open('Doctors.csv', 'w', newline='') as file:
                fieldnames = self.doctor_data[0].keys()
                csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
                csv_writer.writeheader()
                csv_writer.writerows(self.doctor_data)

        def update_information(self):
            selected_item = self.tree.focus()
            if selected_item:
                selected_data = self.tree.item(selected_item)['values']
                self.update_window(selected_data, selected_item)

        def update_window(self, data, selected_item):
            update_window = tk.Toplevel(self.root)
            update_window.title("Update Information")

            labels = ['First Name', 'Last Name', 'Title', 'Age', 'Address', 'Phone Number', 'Speciality']
            entries = []

            for i, label in enumerate(labels):
                tk.Label(update_window, text=label).grid(row=i, column=0, padx=10, pady=10)
                entry = tk.Entry(update_window)
                entry.insert(0, data[i])
                entry.grid(row=i, column=1, padx=10, pady=10)
                entries.append(entry)

            #Creates labels and entry widgets for each attribute of the doctor who is selected allowing their info to be updated

            def save_changes():
                for i, label in enumerate(labels):
                    self.doctor_data[int(selected_item) - 1][label] = entries[i].get()
                self.save_data()
                update_window.destroy()
                self.refresh_data()

            tk.Button(update_window, text="Save Changes", command=save_changes).grid(row=len(labels), column=0,
                                                                                  columnspan=2, pady=10)

        def refresh_data(self):
            for row in self.tree.get_children():
                self.tree.delete(row)
            self.load_data()
            self.populate_tree()

        def populate_tree(self):
            for i, doctor in enumerate(self.doctor_data, start=1):
                self.tree.insert('', 'end', iid=i, values=list(doctor.values()))

    DoctorApp()

