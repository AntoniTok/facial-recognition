import json
    
def save_persons(persons, filename):
    with open(filename, 'w') as file:
        json.dump(persons, file)

def load_persons(filename):
    with open(filename, 'r') as file:
        persons = json.load(file)
    return persons
