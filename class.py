#animal class
class Animal:
    def __init__(self, id, name, species, age, health):
        self.id = id
        self.name = name
        self.species = species
        self.age = age
        self.health = health

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'species': self.species,
            'age': self.age,
            'health': self.health
        }
#adopter class
class Adopter:
    def __init__(self, id, name, contact, approved):
        self.id = id
        self.name = name
        self.contact = contact
        self.approved = approved

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'contact': self.contact
            'approved': self.approved
        }
#adpotion record class
class AdoptionRecord:
    def __init__(self, record_id, animal_id, adopter_id, adoption_date):
        self.record_id = record_id
        self.animal_id = animal_id
        self.adopter_id = adopter_id
        self.adoption_date = adoption_date

    def to_dict(self):
        return {
            'record_id': self.record_id,
            'animal_id': self.animal_id,
            'adopter_id': self.adopter_id,
            'adoption_date': self.adoption_date
        }
