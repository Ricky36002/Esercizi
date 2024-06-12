from persona import Persona

class Paziente(Persona):
    def __init__(self, first_name, last_name, id_code):
        super().__init__(first_name, last_name)
        if isinstance(id_code, str):
            self.__id_code = id_code
        else:
            self.__id_code = None
            print("Il codice identificativo inserito non è una stringa!")

    def setIdCode(self, id_code):
        if isinstance(id_code, str):
            self.__id_code = id_code
        else:
            print("Il codice identificativo inserito non è una stringa!")

    def getIdCode(self):
        return self.__id_code

    def patientInfo(self):
        return f"Paziente: {self.getName()} {self.getLastname()}\nID: {self.__id_code}"