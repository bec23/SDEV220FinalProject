class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

class Adopter:
    def __init__(self, name, contact_info, approved=False):
        self.name = name
        self.contact_info = contact_info
        self.approved = approved

class AdoptionRecord:
    def __init__(self, animal, adopter, date):
        self.animal = animal
        self.adopter = adopter
        self.date = date

class AdoptionCenter:
    def __init__(self):
        self.animals = []
        self.adopters = []
        self.adoption_records = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_adopter(self, adopter):
        self.adopters.append(adopter)

    def approve_adopter(self, adopter_name):
        adopter = next((a for a in self.adopters if a.name == adopter_name), None)
        if adopter:
            adopter.approved = True
            return f"{adopter.name} has been approved."
        return "Adopter not found."

    def record_adoption(self, animal_name, adopter_name, date):
        animal = next((a for a in self.animals if a.name == animal_name), None)
        adopter = next((a for a in self.adopters if a.name == adopter_name), None)
        if animal and adopter and adopter.approved:
            self.animals.remove(animal)
            record = AdoptionRecord(animal, adopter, date)
            self.adoption_records.append(record)
            return f"{adopter.name} has adopted {animal.name} on {date}."
        return "Adoption failed. Animal or adopter not found, or adopter not approved."

