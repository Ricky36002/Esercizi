from persona import Persona

class Dottore(Persona):
    def __init__(self, first_name, last_name, specialization, parcel):
        super().__init__(first_name, last_name)
        if isinstance(specialization, str):
            self.__specialization = specialization
        else:
            self.__specialization = None
            print("La specializzazione inserita non è una stringa!")

        if isinstance(parcel, float):
            self.__parcel = parcel
        else:
            self.__parcel = None
            print("La parcella inserita non è un float!")

    def setSpecialization(self, specialization):
        if isinstance(specialization, str):
            self.__specialization = specialization
        else:
            print("La specializzazione inserita non è una stringa!")

    def setParcel(self, parcel):
        if isinstance(parcel, float):
            self.__parcel = parcel
        else:
            print("La parcella inserita non è un float!")

    def getSpecialization(self):
        return self.__specialization

    def getParcel(self):
        return self.__parcel

    def isAValidDoctor(self):
        if self.getAge() > 30:
            print(f"Doctor {self.getName()} {self.getLastname()} is valid!")
            return True
        else:
            print(f"Doctor {self.getName()} {self.getLastname()} is not valid!")
            return False

    def doctorGreet(self):
        return self.greet() + f" Sono un medico {self.__specialization}"