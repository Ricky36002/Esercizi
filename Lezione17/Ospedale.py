from dottore import Dottore
from paziente import Paziente
from fattura import Fattura


dottore_1 = Dottore("Mario", "Rossi", "Pediatra", 50.0)
dottore_1.setAge(29)  

dottore_2 = Dottore("Luca", "Bianchi", "Ostetrico", 75.0)
dottore_2.setAge(50)  


dottore_1.doctorGreet()
print("\n")
dottore_2.doctorGreet()
print("\n")


paziente_1 = Paziente("Giulia", "Verdi", "P001")
paziente_2 = Paziente("Marco", "Neri", "P002")
paziente_3 = Paziente("Anna", "Gialli", "P003")
lista_pazienti_1 = [paziente_1, paziente_2, paziente_3]  

paziente_4 = Paziente("Elena", "Blu", "P004")
lista_pazienti_2 = [paziente_4]  


fattura_1 = Fattura(lista_pazienti_1, dottore_1)
fattura_2 = Fattura(lista_pazienti_2, dottore_2)


print(f"Salario Dottore1: {fattura_1.getSalary()} euro!")
print(f"Salario Dottore2: {fattura_2.getSalary()} euro!")


fattura_1.removePatient("P001")
fattura_2.addPatient(paziente_1)


print(f"Salario Dottore1: {fattura_1.getSalary()} euro!")
print(f"Salario Dottore2: {fattura_2.getSalary()} euro!")


guadagno_totale = fattura_1.getSalary() + fattura_2.getSalary()
print(f"In totale, l'ospedale ha incassato: {guadagno_totale} euro!")