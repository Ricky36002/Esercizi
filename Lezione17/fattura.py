import paziente, dottore

class Fattura:
    def __init__(self, patients, doctor):
        self.__patients = patients
        self.__doctor = doctor

        if doctor.isAValidDoctor():
            self.__fatture = len(patients)
            self.__salary = 0
        else:
            self.__fatture = None
            self.__salary = None
            print("Non è possibile creare la classe fattura poiché il dottore non è valido!")

    def getSalary(self):
        self.__salary = self.__doctor.getParcel() * len(self.__patients)
        return self.__salary

    def getFatture(self):
        self.__fatture = len(self.__patients)
        return self.__fatture

    def addPatient(self, new_patient):
        self.__patients.append(new_patient)
        self.__fatture = self.getFatture()
        self.__salary = self.__doctor.getParcel() * self.__fatture
        print(f"Alla lista del Dottor {self.__doctor.getLastname()} è stato aggiunto il paziente {new_patient.getIdCode()}")

    def removePatient(self, id_code):
        for patient in self.__patients:
            if patient.getIdCode() == id_code:
                self.__patients.remove(patient)
                self.__fatture = self.getFatture()
                self.__salary = self.__doctor.getParcel() * self.__fatture
                print(f"Alla lista del Dottor {self.__doctor.getLastname()} è stato rimosso il paziente {id_code}")
                return
        print(f"Nessun paziente con ID {id_code} trovato.")