import time

class Person:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
        
    def __repr__(self):
        return f"Person(name={self.name}, id={self.id})"
    
    @property    
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, identity):
        if not isinstance(identity, str):
            raise ValueError("String Expected")
        self.__name = identity
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError("Int Expected")
        self.__id = value
    
def create_person(name):
    timestamp = int(time.time())
    person = Person(name=name, id=timestamp)
    return person

def get_person_id(name, persons):
    for person in persons.keys():
        if person.lower() == name.lower():
            # print(f'{name} found, ID: {persons[person]}')
            return persons[person]
    return 

def person_exists(name, persons):
    for person in persons.keys():
        if person.lower() == name.lower():
            return True
    return False

def rename_person(name, new_name, persons):
    for person in persons.keys():
        if person.lower() == name.lower():
            person = new_name
            return person
    return 
