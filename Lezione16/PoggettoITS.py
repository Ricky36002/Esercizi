'''# In questo progetto, dovrai scrivere il codice per un sistema di gestione e creazione dei corsi ITS.
# Il sistema gestisce aule ed edifici (Parte 1), persone -studenti e docenti- in gruppi di studio (parte 2), e corsi (parte 3).
 
# ### Classe Room:
# La classe Room rappresenta un'aula. Ogni aula ha un ID (id), un piano (floor), un numero di posti (seats) e un'area (area). 
#L'area è calcolata come il doppio dei posti.
# - Metodi:
#     - get_id(): Restituisce l'ID dell'aula.
#     - get_floor(): Restituisce il piano dell'aula.
#     - get_seats(): Restituisce il numero di posti dell'aula.
#     - get_area(): Restituisce l'area dell'aula.

# ### Classe Building:
# La classe Building rappresenta un edificio. Ogni edificio ha un nome (name), un indirizzo (address), un intervallo di piani 
#(floors), e una lista di aule (rooms).
# - Metodi:
#     - get_floors(): Restituisce l'intervallo di piani dell'edificio.
#     - get_rooms(): Restituisce la lista delle aule nell'edificio.
#     - add_room(room): Aggiunge un'aula all'edificio, solo se il piano dell'aula è compreso nell'intervallo di piani dell'edificio.
#     - area(): Restituisce l'area totale dell'edificio sommando le aree di tutte le aule.

class Room:
    def __init__(self, id, floor, seats):
        self.id : int = id
        self.floor : int = floor
        self.seats : int = seats
        self.area : int = seats * 2
    
    def get_id(self):
        return self.id
    
    def get_floor(self):
        return self.floor
    
    def get_seats(self):
        return self.seats
    
    def get_area(self):
        return self.area
class Building:
    def __init__(self, name, address, floors):
        self.name = name
        self.address = address
        self.floors = floors
        self.rooms = []
    
    def get_floors(self):
        return self.floors
    
    def get_rooms(self):
        return self.rooms
    
    def add_room(self, room):
        if self.floors[0] <= room.get_floor() <= self.floors[1]:
            if room not in self.rooms:
                self.rooms.append(room)
    
    def area(self):       
        total_area = sum(room.get_area() for room in self.rooms)
        return total_area
    
#     ### Classi Person, Student e Lecturer:
# La classe Person rappresenta una persona con un codice fiscale (cf), un nome (name), un cognome (surname), un'età (age).
# Le classi Student e Lecturer ereditano da Person.
# Uno studente è associato ad un gruppo di studio (group). Quindi, la classe Student ha il seguente metodo:
#     - set_group(group): Associa un gruppo di studio allo studente

# ### Classe Group:
# La classe Group rappresenta un gruppo di studio. Ogni gruppo ha un nome (name), un limite di studenti (limit), una lista di studenti (students) e una lista di docenti (lecturers).
# - Metodi:
#     - get_name(): Restituisce il nome del gruppo
#     - get_limit(): Restituisce il limite di studenti nel gruppo
#     - get_students(): Resituisce la lista di studenti nel gruppo
#     - get_limit_lecturers(): Restituisce il limite di docenti nel gruppo. E' consentito 1 docente ogni 10 studenti. Il gruppo può avere almeno 1 docente, anche se ci sono meno di 10 studenti.
#     - add_student(student): Aggiunge uno studente al gruppo, solo se il limite per gli studenti non è stato raggiunto.
#     - add_lecturer(lecturer): Aggiunge un docente al gruppo, solo se il limite per i docenti non è stato raggiunto.
        
class Person:
    def __init__(self, cf, name, surname, age):
        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age

class Student(Person):
    def __init__(self, cf, name, surname, age, group=None):
        super().__init__(cf, name, surname, age)
        self.group = group
    
    def set_group(self, group):
        self.group = group

class Lecturer(Person):
    pass
class Group:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.students = []
        self.lecturers = []
    
    def get_name(self):
        return self.name
    
    def get_limit(self):
        return self.limit
    
    def get_students(self):
        return self.students
        
    def get_limit_lecturers(self):
        min_lecturers = 1
        max_students_per_lecturer = 10
        num_students = len(self.students)
        num_lecturers = max(min_lecturers, num_students // max_students_per_lecturer)
        return num_lecturers

    def add_student(self, student):
        if len(self.students) < self.limit:
            self.students.append(student)
            return True
        else:
            print("Errore: Limite di studenti nel gruppo raggiunto.")
            return False

    def add_lecturer(self, lecturer):
        if len(self.lecturers) < self.get_limit_lecturers():
            self.lecturers.append(lecturer)
            return True
        else:
            print("Errore: Limite di docenti nel gruppo raggiunto.")
            return False'''


# ### Classe Course:
# La classe Course rappresenta un corso accademico. Ogni corso ha un nome (name) e una lista di gruppi (groups).
# - Metodi:
#     - register(student): Registra uno studente nel primo gruppo disponibile che non ha ancora raggiunto il limite di studenti.
#     - get_groups(): Restituisce la lista dei gruppi nel corso.
#     - add_group(group): Aggiunge un gruppo al corso.
class Room:
    def __init__(self, id, floor, seats):
        self.id : int = id
        self.floor : int = floor
        self.seats : int = seats
        self.area : int = seats * 2
    
    def get_id(self):
        return self.id
    
    def get_floor(self):
        return self.floor
    
    def get_seats(self):
        return self.seats
    
    def get_area(self):
        return self.area
class Building:
    def __init__(self, name, address, floors):
        self.name = name
        self.address = address
        self.floors = floors
        self.rooms = []
    
    def get_floors(self):
        return self.floors
    
    def get_rooms(self):
        return self.rooms
    
    def add_room(self, room):
        if self.floors[0] <= room.get_floor() <= self.floors[1]:
            if room not in self.rooms:
                self.rooms.append(room)
    
    def area(self):       
        total_area = sum(room.get_area() for room in self.rooms)
        return total_area
class Person:
    def __init__(self, cf, name, surname, age):
        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age

class Student(Person):
    def __init__(self, cf, name, surname, age, group=None):
        super().__init__(cf, name, surname, age)
        self.group = group
    
    def set_group(self, group):
        self.group = group

class Lecturer(Person):
    pass
class Group:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.students = []
        self.lecturers = []
    
    def get_name(self):
        return self.name
    
    def get_limit(self):
        return self.limit
    
    def get_students(self):
        return self.students
        
    def get_limit_lecturers(self):
        min_lecturers = 1
        max_students_per_lecturer = 10
        num_students = len(self.students)
        num_lecturers = max(min_lecturers, num_students // max_students_per_lecturer)
        return num_lecturers

    def add_student(self, student):
        if len(self.students) < self.limit:
            self.students.append(student)
            return True
        else:
            print("Errore: Limite di studenti nel gruppo raggiunto.")
            return False

    def add_lecturer(self, lecturer):
        if len(self.lecturers) < self.get_limit_lecturers():
            self.lecturers.append(lecturer)
            return True
        else:
            print("Errore: Limite di docenti nel gruppo raggiunto.")
            return False
class Course:
    def __init__(self, name):
        self.name = name  
        self.groups = []  

    def register(self, student):
        
        for group in self.groups:
            
            if len(group.get_students()) < group.get_limit() and student not in group.get_students():
                group.add_student(student)  
                return  
        print("Errore: Nessun gruppo disponibile o tutti i gruppi hanno raggiunto il limite di studenti.")  
    def get_groups(self):
        return self.groups
    def add_group(self, group):
        self.groups.append(group)
        
        
                
        
        
            
    





                