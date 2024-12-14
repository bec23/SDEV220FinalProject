#becky rieger
#program for livingston county humane society. enter animal, adopter, and adoption. function to approve adopter
#do not allow adoption if adotper not approved. clear input fields once added. self generate id numbers. make important fields required.
#view what has been added, mark adopted animals with red text in listbox

#import
import tkinter as tk
from tkinter import ttk, messagebox
import datetime

#animal class with fields, adopt status false until adopted to change text color once adopted
class Animal:
    def __init__(self, animal_id, name, animal_type, species, age, description):
        self.animal_id = animal_id
        self.name = name
        self.animal_type = animal_type
        self.species = species
        self.age = age
        self.description = description
        self.adopted = False

#adopter class with fields
class Adopter:
    def __init__(self, adopter_id, first_name, last_name, address, city, state, zip_code, phone, approved):
        self.adopter_id = adopter_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.approved = approved

#adoption class and fields
class Adoption:
    def __init__(self, animal_id, adopter_id, date):
        self.animal_id = animal_id
        self.adopter_id = adopter_id
        self.date = date

#main app
class Humane_Society_App:
    def __init__(self, root):
        self.root = root
        self.root.title("Livingston County Humane Society")
        self.root.configure(bg='grey')
        
        #lists
        self.animals = []
        self.adopters = []
        self.adoptions = []
        
        #widgets
        self.create_widgets()

    #create setions
    def create_widgets(self):
        #title, large blue print bolded, aligned left
        title = tk.Label(self.root, text="Livingston County Humane Society Management System", font=("Helvetica", 20, "bold"), fg="dark blue", bg='grey')
        title.grid(row=0, column=0, columnspan=3, pady=10)

        #animal section, heading large and bolded, aligned left, name input field
        ttk.Label(self.root, text="Animals", font=("Helvetica", 12, "bold"), background='grey').grid(column=0, row=1, sticky="w")
        ttk.Label(self.root, text="Animal Name:", background='grey').grid(column=0, row=2, sticky="w")
        self.animal_name = tk.Entry(self.root)
        self.animal_name.grid(column=1, row=2, sticky="w")

        #animal section, field animal type option box of cat or dog, aligned left
        ttk.Label(self.root, text="Animal Type (Cat/Dog):", background='grey').grid(column=0, row=3, sticky="w")
        self.animal_type = ttk.Combobox(self.root, values=["Cat", "Dog"])
        self.animal_type.grid(column=1, row=3, sticky="w")

        #animal section, field species input, aligned left
        ttk.Label(self.root, text="Species:", background='grey').grid(column=0, row=4, sticky="w")
        self.species = tk.Entry(self.root)
        self.species.grid(column=1, row=4, sticky="w")

        #animal section, field age input, aligned left
        ttk.Label(self.root, text="Age:", background='grey').grid(column=0, row=5, sticky="w")
        self.age = tk.Entry(self.root)
        self.age.grid(column=1, row=5, sticky="w")

        #animal section, field description input, aligned left
        ttk.Label(self.root, text="Description:", background='grey').grid(column=0, row=6, sticky="w")
        self.description = tk.Entry(self.root)
        self.description.grid(column=1, row=6, sticky="w")

        #animal section, add animal button, aligned left
        ttk.Button(self.root, text="Add Animal", command=self.add_animal).grid(column=0, row=7, sticky="w")

        #section break
        ttk.Separator(self.root, orient='horizontal').grid(column=0, row=9, columnspan=3, sticky='ew', pady=10)

        #adopter section, heading large and bolded, first name input field, aligned left
        ttk.Label(self.root, text="Adopters", font=("Helvetica", 12, "bold"), background='grey').grid(column=0, row=10, sticky='w')
        ttk.Label(self.root, text="First Name:", background='grey').grid(column=0, row=11, sticky='w')
        self.first_name = tk.Entry(self.root)
        self.first_name.grid(column=1, row=11, sticky='w')

        #adopter section, last name input field, aligned left
        ttk.Label(self.root, text="Last Name", background='grey').grid(column=0, row=12, sticky='w')
        self.last_name = tk.Entry(self.root)
        self.last_name.grid(column=1, row=12, sticky='w')

        #adopter section, address input field, aligned left
        ttk.Label(self.root, text="Address:", background='grey').grid(column=0, row=13, sticky='w')
        self.address = tk.Entry(self.root)
        self.address.grid(column=1, row=13, sticky='w')

        #adopter section, city input field, aligned left
        ttk.Label(self.root, text="City:", background='grey').grid(column=0, row=14, sticky='w')
        self.city = tk.Entry(self.root)
        self.city.grid(column=1, row=14, sticky='w')

        #adopter section, state input field, aligned left
        ttk.Label(self.root, text="State:", background='grey').grid(column=0, row=15, sticky='w')
        self.state = tk.Entry(self.root)
        self.state.grid(column=1, row=15, sticky='w')

        #adopter section, zip code input field, aligned left
        ttk.Label(self.root, text="Zip Code:", background='grey').grid(column=0, row=16, sticky='w')
        self.zip_code = tk.Entry(self.root)
        self.zip_code.grid(column=1, row=16, sticky='w')

        #adopter section, phone input field, aligned left
        ttk.Label(self.root, text="Phone:", background='grey').grid(column=0, row=17, sticky='w')
        self.phone = tk.Entry(self.root)
        self.phone.grid(column=1, row=17, sticky='w')

        #adopter section, approve field default no with option box yes/no, aligned left
        ttk.Label(self.root, text="Approved:", background='grey').grid(column=0, row=18, sticky='w')
        self.approved_var = tk.StringVar(value="No")
        self.approved = ttk.Combobox(self.root, textvariable=self.approved_var, values=["Yes", "No"])
        self.approved.grid(column=1, row=18, sticky='w')

        #adopter section, add adopter button, aligned left
        ttk.Button(self.root, text="Add Adopter", command=self.add_adopter).grid(column=0, row=19, sticky='w')

        #section break
        ttk.Separator(self.root, orient='horizontal').grid(column=0, row=21, columnspan=3, sticky='ew', pady=10)

        #adoption section, heading large and bolded, animal id input field, aligned left
        ttk.Label(self.root, text="Adoptions", font=("Helvetica", 12, "bold"), background='grey').grid(column=0, row=22, sticky='w')
        ttk.Label(self.root, text="Animal ID:", background='grey').grid(column=0, row=23, sticky='w')
        self.animal_id = tk.Entry(self.root)
        self.animal_id.grid(column=1, row=23, sticky='w')

        #adoption section, adopter id input field, aligned left
        ttk.Label(self.root, text="Adopter ID:", background='grey').grid(column=0, row=24, sticky='w')
        self.adopter_id = tk.Entry(self.root)
        self.adopter_id.grid(column=1, row=24, sticky='w')

        #adoption section, adoption date input field with format, aligned left
        ttk.Label(self.root, text="Adoption Date (YYYY-MM-DD):", background='grey').grid(column=0, row=25, sticky='w')
        self.date = tk.Entry(self.root)
        self.date.grid(column=1, row=25, sticky='w')

        #adoption section, add adoption button, aligned left
        ttk.Button(self.root, text="Add Adoption", command=self.add_adoption).grid(column=0, row=26, sticky='w')

        #section break
        ttk.Separator(self.root, orient='horizontal').grid(column=0, row=27, columnspan=3, sticky='ew', pady=10)

        #view lists section, heading large and bolded, add view animals, view adopters, view adoptions buttons, aligned left
        ttk.Label(self.root, text="View Lists", font=("Helvetica", 12, "bold"), background='grey').grid(column=0, row=28, sticky='w')
        ttk.Button(self.root, text="View Animals", command=self.view_animals).grid(column=0, row=29, sticky='w')
        ttk.Button(self.root, text="View Adopters", command=self.view_adopters).grid(column=1, row=29, sticky='w')
        ttk.Button(self.root, text="View Adoptions", command=self.view_adoptions).grid(column=2, row=29, sticky='w')

    #generate id and increase by one(for animal and adopter id)
    def generate_id(self, collection):
        return len(collection) + 1
     
     #add animal section, name, animal type and species is required, self generate animal id, 
     #add animal to list, clear input fields once added, error message if required fields not filled out     
    def add_animal(self):
        name = self.animal_name.get()
        animal_type = self.animal_type.get()
        species = self.species.get()
        age = self.age.get()
        description = self.description.get()
        if name and animal_type and species:
            animal_id = self.generate_id(self.animals)
            animal = Animal(animal_id, name, animal_type, species, age, description)
            self.animals.append(animal)
            self.animal_name.delete(0, tk.END)
            self.animal_type.set('')
            self.species.delete(0, tk.END)
            self.age.delete(0, tk.END)
            self.description.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill in all required fields (Name, Animal Type, Species).")

    #add adopter section, first name, last name, address, city, state, zip code and phone required, approved default no,
    #generate adopter id, clear input fields once added, zip code and phone digit requirements, error message if zip and phone not formatted correct,add adopter to list, error message if required fields not completed
    def add_adopter(self):
        first_name = self.first_name.get()
        last_name = self.last_name.get()
        address = self.address.get()
        city = self.city.get()
        state = self.state.get()
        zip_code = self.zip_code.get()
        phone = self.phone.get()
        approved = self.approved_var.get()
        if first_name and last_name and address and city and state and zip_code and phone:
            if len(zip_code) == 5 and zip_code.isdigit() and len(phone) == 10 and phone.isdigit():
                adopter_id = self.generate_id(self.adopters)
                adopter = Adopter(adopter_id, first_name, last_name, address, city, state, zip_code, phone, approved)
                self.adopters.append(adopter)
                self.first_name.delete(0, tk.END)
                self.last_name.delete(0, tk.END)
                self.address.delete(0, tk.END)
                self.city.delete(0, tk.END)
                self.state.delete(0, tk.END)
                self.zip_code.delete(0, tk.END)
                self.phone.delete(0, tk.END)
                self.approved_var.set("No")
            else:
                messagebox.showerror("Error", "Please enter a valid 5-digit zip code and a 10-digit phone number.")
        else:
            messagebox.showerror("Error", "Please fill in all required fields.")

    #add adoption section, date format, all fields required, success message, if adopter not approved get error message, mark as adopted
    #if all fields are complete receive error message, clear input fields once added, add adoption to list, error message for date format
    def add_adoption(self):
        animal_id = self.animal_id.get()
        adopter_id = self.adopter_id.get()
        date = self.date.get()
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
            if animal_id and adopter_id and date:
                animal = next((a for a in self.animals if a.animal_id == int(animal_id)), None)
                adopter = next((a for a in self.adopters if a.adopter_id == int(adopter_id)), None)
                if animal and adopter and adopter.approved == "Yes":
                    adoption = Adoption(animal_id, adopter_id, date)
                    self.adoptions.append(adoption)
                    animal.adopted = True
                    self.animal_id.delete(0, tk.END)
                    self.adopter_id.delete(0, tk.END)
                    self.date.delete(0, tk.END)
                    messagebox.showinfo("Success", "Adoption recorded successfully!")
                else:
                    messagebox.showerror("Error", "Adopter must be approved to adopt.")
            else:
                messagebox.showerror("Error", "Please fill in all required fields.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid date in YYYY-MM-DD format.")

    #view animal section, list in new window, change text to red if adopted
    def view_animals(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("Animals List")
        animals_listbox = tk.Listbox(view_window)
        animals_listbox.pack(fill=tk.BOTH, expand=True)
        for animal in self.animals:
            if animal.adopted:
                animals_listbox.insert(tk.END, f"{animal.animal_id}: {animal.name}, ({animal.animal_type}, {animal.species}, {animal.age}, {animal.description})")
                animals_listbox.itemconfig(tk.END, {'fg':'red'})
            else:
                animals_listbox.insert(tk.END, f"{animal.animal_id}: {animal.name}, ({animal.animal_type}, {animal.species}, {animal.age}, {animal.description})")

    #view adopter section, list in new window, shows approved or not approved
    def view_adopters(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("Adopters List")
        adopters_listbox = tk.Listbox(view_window)
        adopters_listbox.pack(fill=tk.BOTH, expand=True)
        for adopter in self.adopters:
            status = "Approved" if adopter.approved == "Yes" else "Not Approved"
            adopters_listbox.insert(tk.END, f"{adopter.adopter_id}: {adopter.first_name} {adopter.last_name} ({adopter.address}, {adopter.city}, {adopter.state}, {adopter.zip_code}, {adopter.phone}, Approved: {status})")

    #view adoption section, list in new window of all animal info and all adopter info
    def view_adoptions(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("Adoptions List")
        adoptions_listbox = tk.Listbox(view_window)
        adoptions_listbox.pack(fill=tk.BOTH, expand=True)
        for adoption in self.adoptions:
            animal = next((a for a in self.animals if a.animal_id == int(adoption.animal_id)), None)
            adopter = next((a for a in self.adopters if a.adopter_id == int(adoption.adopter_id)), None)
            adoptions_listbox.insert(tk.END, f"Animal ID: {adoption.animal_id}, Name: {animal.name}, Type: {animal.animal_type}, Species: {animal.species}, Age: {animal.age}, Description: {animal.description}, Adopter ID: {adoption.adopter_id}, Name: {adopter.first_name} {adopter.last_name}, Address: {adopter.address}, City: {adopter.city}, State: {adopter.state}, Zip Code: {adopter.zip_code}, Phone: {adopter.phone}, Date: {adoption.date}")

#loop
if __name__ == "__main__":
    root = tk.Tk()
    app = Humane_Society_App(root)
    root.mainloop()
