class Person:
    
    def __init__ (self, name: str, surname: str, ssn: str) -> None:
        self.name: str = name 
        self.surname: str = surname
        self._ssn: str = ssn
    def get_name(self):
    
        return self.name
    
    def get_ssn(self):

        return self._ssn
    
    def set_name(self, name: str):
        self.name = name
        raise Exception("You cannot modify the name!")
    
    def __str__(self)-> str:

        return f"name: {self.name} surname: {self.surname} ssn:{self._ssn}"
    
persona_1: Person =Person(name = "Riccardo", surname = "Russo", ssn = "RSSRCR")
persona_2: Person =Person(name = "Valentino", surname = "Rossi", ssn = "RSSVLT")
#print(persona_1.get_name())
#persona_1.set_name(name= "Simone")
#print(persona_1.get_name())
print(str(persona_1))
print(str(persona_2))

queue : list[Person] = [persona_1, persona_2]

for person in queue:
    
    print(person.get_ssn())