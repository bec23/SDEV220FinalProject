import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class HumaneSocietyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Livingston County Humane Society")
        self.center = AdoptionCenter()

        self.create_widgets()

    def create_widgets(self):
        # Animal Section
        tk.Label(self.root, text="Animal Name:").grid(row=0, column=0)
        self.animal_name_entry = tk.Entry(self.root)
        self.animal_name_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Species:").grid(row=1, column=0)
        self.species_entry = tk.Entry(self.root)
        self.species_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Age:").grid(row=2, column=0)
        self.age_entry = tk.Entry(self.root)
        self.age_entry.grid(row=2, column=1)

        tk.Button(self.root, text="Add Animal", command=self.add_animal).grid(row=3, column=0, columnspan=2)

        # Adopter Section
        tk.Label(self.root, text="Adopter Name:").grid(row=4, column=0)
        self.adopter_name_entry = tk.Entry(self.root)
        self.adopter_name_entry.grid(row=4, column=1)

        tk.Label(self.root, text="Contact Info:").grid(row=5, column=0)
        self.contact_info_entry = tk.Entry(self.root)
        self.contact_info_entry.grid(row=5, column=1)

        tk.Button(self.root, text="Add Adopter", command=self.add_adopter).grid(row=6, column=0, columnspan=2)

        tk.Label(self.root, text="Approve Adopter:").grid(row=7, column=0)
        self.approve_adopter_entry = tk.Entry(self.root)
        self.approve_adopter_entry.grid(row=7, column=1)

        tk.Button(self.root, text="Approve", command=self.approve_adopter).grid(row=8, column=0, columnspan=2)

        # Adoption Section
        tk.Label(self.root, text="Animal to Adopt:").grid(row=9, column=0)
        self.adopt_animal_entry = tk.Entry(self.root)
        self.adopt_animal_entry.grid(row=9, column=1)

        tk.Label(self.root, text="Adopter Name:").grid(row=10, column=0)
        self.adopt_adopter_entry = tk.Entry(self.root)
        self.adopt_adopter_entry.grid(row=10, column=1)

        tk.Label(self.root, text="Adoption Date (YYYY-MM-DD):").grid(row=11, column=0)
        self.adoption_date_entry = tk.Entry(self.root)
        self.adoption_date_entry.grid(row=11, column=1)

        tk.Button(self.root, text="Adopt Animal", command=self.adopt_animal).grid(row=12, column=0, columnspan=2)

    def add_animal(self):
        name = self.animal_name_entry.get()
        species = self.species_entry.get()
        age = self.age_entry.get()
        animal = Animal(name, species, age)
        self.center.add_animal(animal)
        messagebox.showinfo("Success", f"Added {name} the {species}.")

    def add_adopter(self):
        name = self.adopter_name_entry.get()
        contact_info = self.contact_info_entry.get()
        adopter = Adopter(name, contact_info)
        self.center.add_adopter(adopter)
        messagebox.showinfo("Success", f"Added adopter {name}.")

    def approve_adopter(self):
        adopter_name = self.approve_adopter_entry.get()
        result = self.center.approve_adopter(adopter_name)
        messagebox.showinfo("Approval Result", result)

    def adopt_animal(self):
        animal_name = self.adopt_animal_entry.get()
        adopter_name = self.adopt_adopter_entry.get()
        adoption_date = self.adoption_date_entry.get()
        try:
            datetime.strptime(adoption_date, "%Y-%m-%d")
            result = self.center.record_adoption(animal_name, adopter_name, adoption_date)
            messagebox.showinfo("Adoption Result", result)
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")

if __name__ == "__main__":
    root = tk.Tk()
    app = HumaneSocietyApp(root)
    root.mainloop()