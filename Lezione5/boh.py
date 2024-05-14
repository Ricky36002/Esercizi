class Student:
    def __init__(self, name: str, study_program: str, age: str, gender: str)-> None:
        self.name: str = name
        self.study_p: str = study_program
        self.age: str = age
        self.gender: str = gender
    def print_info(self):

        return  self.name, self.study_p, self.age, self.gender        

persona_1: Student = Student(name = "Riccardo", study_program ="CyberSecurity", age = "21", gender = "Male")
persona_2: Student = Student(name = "Federico", study_program ="CyberSecurity", age = "36", gender = "Male") 
persona_3: Student = Student(name = "Edwin", study_program ="CyberSecurity", age = "21", gender = "Male")      

print(persona_1.print_info())
print(persona_2.print_info())
print(persona_3.print_info())

class Animal:
    def __init__(self, name: str) -> None:
        self.animal: str = name 
        
    def set_legs(self, legs: str):
        self.legs: str = legs
    
    def get_legs(self) -> int:

        return self.legs

    def print_info(self):
        print(f"{self.animal} {self.legs}")


animal_1: Animal = Animal(name = "Cane")
animal_1.legs = "10"
animal_1.print_info()


class Food:
    def __init__(self, name: str, price: int, description: str) -> None:
        self.name = name
        self.price = price
        self.description = description

class Menu:
    def __init__(self, foods: list = []) -> None:
        self.foodlist: list = foods

    def addFood(self, food: Food):
        self.foodlist.append(food)
    
    def remuveFood(self,):
# help me
food1: Food = Food("Pasta", 15, "Ottima")
food2: Food = Food("Carne", 30, "Alla bracie è meglio")
food3: Food = Food("Pizza", 100, "Bonaaaa")
food4: Food = Food()# da rimuovere 
food5: Food = Food()# da aggiungere
foods = [food1,food2,food3]
menu2: Menu = Menu()
menu: Menu = Menu(foods)
print(menu.foods,menu2.foods)
    





#for x in foods:
    #print(x.name)
