#9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: 
#a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, 
#and a method called open_restaurant() that prints a message indicating that the restaurant is open. Make an instance called 
#restaurant from your class. Print the two attributes individually, and then call both methods.

class Restaurant:
    
    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.restaurant_name: str = restaurant_name
        self.cuisine_type: str =  cuisine_type
    

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant("The Gourmet le Riccardò", "Italian")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

#9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call 
#describe_restaurant() for each instance.
restaurant1 = Restaurant("Alice Pizza", "Pizza")
restaurant2 = Restaurant("Koi", "Japanese")
restaurant3 = Restaurant("Burger King", "American")

restaurant1.describe_restaurant()
print('\n')
restaurant2.describe_restaurant()
print('\n')
restaurant3.describe_restaurant()


#9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other 
#attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s
#information. Make another method called greet_user() that prints a personalized greeting to the user. Create several instances 
#representing different users, and call both methods for each user.

class User:

    def __init__(self, fname: str, lname: str, email:str = None, nick:str = None) -> None:
        self.first_name: str = fname
        self.last_name: str = lname
        self.email: str = email
        self.nickname: str = nick
    
    def describe_user(self) -> None:
        print(f"The user {self.nickname if self.nickname else self.first_name} data:",
              f"First Name: {self.first_name}",
              f"Last Name: {self.last_name}",
              f"Email: {self.email}" if self.email else "",sep="\n",end="\n\n")

    def greet_user(self) -> None:
        print(f"Welcome {self.nickname if self.nickname else self.first_name}!",end="\n\n")

user1: User = User("Giacomo","Giacomo","giacomo@giacomo.com","GiacomoGiacomo")
user2: User = User("Seth","Evergreen","seth_evergreen1978@gmail.com")
user3: User = User("Molly","Smith",nick="cute_drug")

user1.greet_user()
user2.greet_user()
user3.greet_user()

user1.describe_user()
user2.describe_user()
user3.describe_user() 


#9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0.
#Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change
#this value and print it again. Add a method called set_number_served() that lets you set the number of customers that have been
#served. Call this method with a new number and print the value again. Add a method called increment_number_served() that lets 
#you increment the number of customers who’ve been served. Call this method with any number you like that could represent how 
#many customers were served in, say, a day of business. 

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, num):
        self.number_served += num


restaurant = Restaurant("Alice Pizza", "Italian")
print(f"Number of customers served: {restaurant.number_served}")

restaurant.set_number_served(100)
print(f"Number of customers served: {restaurant.number_served}")

restaurant.increment_number_served(50)
print(f"Number of customers served: {restaurant.number_served}")


#9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. Write a method called 
#increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() 
#that resets the value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several
#times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
#Print login_attempts again to make sure it was reset to 0.

class User:

    def __init__(self, fname: str, lname: str, email:str = None, nick:str = None) -> None:
        self.first_name: str = fname
        self.last_name: str = lname
        self.email: str = email
        self.nickname: str = nick
        self.login_attempts: int = 0
    
    def increment_login_attempts(self) -> None:
        self.login_attempts += 1
    
    def reset_login_attempts(self) -> None:
        self.login_attempts = 0

user4: User = User("Mario","Rossi")
for _ in range(4):
    user4.increment_login_attempts()
print(user4.login_attempts)
user4.reset_login_attempts()
print(user4.login_attempts,end="\n\n")

#9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from 
#the Restaurant class you wrote in Exercise 9-1  or Exercise 9-4. Either version of the class will work; just pick the one you 
#like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. 
#Create an instance of IceCreamStand, and call this method. 

class IceCreamStand(Restaurant):
    def __init__(self, name: str, type: str, flavors: list, served: int = 0) -> None:
        super().__init__(name, type, served)
        self.flavors: list = flavors
    
    def get_flavors(self) -> None:
        print(*self.flavors,sep=" | ", end="\n\n")

icecream1: IceCreamStand = IceCreamStand("Brividi","gelato",["strawberry","mango","passion fruit"])
icecream1.get_flavors()
icecream1.describe_restaurant()
icecream1.increment_number_served(50)
print(f"Number of customers served: {icecream1.number_served}")


#9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote 
#in Exercise 9-3 or Exercise 9-5. Add an attribute, privileges, that stores a list of strings like "can add post", "can delete 
#post", "can ban user", and so on. Write a method called show_privileges() that lists the administrator’s set of privileges. 
#Create an instance of Admin, and call your method. 

class Admin(User):
    
    def __init__(self, fname: str, lname: str, privileges = None, email: str = None, nick: str = None) -> None:
        super().__init__(fname, lname, email, nick)
        if isinstance(privileges, Privileges):
            self.privileges: Privileges = privileges
#9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of 
#strings as described in Exercise 9-7. Move the show_privileges() method to this class. Make a Privileges instance as an 
#attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.

class Privileges:
    
    def __init__(self, privileges: list[str]) -> None:
        self.privileges: list[str] = privileges

    def show_privileges(self) -> None:
        print(*self.privileges,sep=" | ", end="\n\n")

administrator: Admin = Admin("Angelo","Carini",Privileges(["can ban user","can delete post"]))
administrator.privileges.show_privileges()
administrator.describe_user()
administrator.greet_user()
administrator.increment_login_attempts(5)
print(f"Login attempts: {administrator.login_attempts}")
administrator.reset_login_attempts()
print(f"Login attempts: {administrator.login_attempts}")


#9-9. Battery Upgrade: Use the final version of electric_car.py from this section. Add a method to the Battery class called 
#upgrade_battery(). This method should check the battery size and set the capacity to 65 if it isn’t already. Make an electric 
#car with a default battery size, call get_range() once, and then call get_range() a second time after upgrading the battery. 
#You should see an increase in the car’s range.


#9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports 
#Restaurant. Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

from restaurant import Restaurant
restaurant = Restaurant("Bella Italia", "Italian")
restaurant = Restaurant("Alice Pizza", "Pizza")
restaurant.describe_restaurant()

#9-11. Imported Admin: Start with your work from Exercise 9-8. Store the classes User, Privileges, and Admin in one module. 
#Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.


#9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. 
#In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.


#9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die()
#that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times. 
#Make a 10-sided die and a 20-sided die. Roll each die 10 times.
from random import randint

class Dice:
    
    def __init__(self, sides: int = 6) -> None:
        self.sides: int = sides if sides > 0 else 1
    
    def roll_dice(self) -> None:
        print(randint(1,self.sides),end=" ")
    
dice1: Dice = Dice()
dice2: Dice = Dice(10)
dice3: Dice = Dice(20)

print("d6:\t", end=" ")
for _ in range(10):
    dice1.roll_dice()
print("\nd10:\t", end=" ")
for _ in range(10):
    dice2.roll_dice()
print("\nd20:\t", end=" ")
for _ in range(10):
    dice3.roll_dice()
print(end="\n\n")

#9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. Randomly select 4 numbers or letters from 
#the list and print a message saying that any ticket matching these 4 numbers or letters wins a prize.

class Lottery:

    possible_winning: list = [10,4,6,28,49,14,66,48,2,81,'f','h','l','p','s']

    def get_winning_numbers() -> list:
        winning_numbers: list = [Lottery.possible_winning[randint(0,len(Lottery.possible_winning)-1)] for _ in range(4)]
        return winning_numbers
    
    def get_my_ticket() -> list:
        my_ticket: list = [Lottery.possible_winning[randint(0,len(Lottery.possible_winning)-1)] for _ in range(4)]
        return my_ticket
    
    def check_winning(win_ticket: list, ticket_check: list) -> bool:
        return set(ticket_check).issubset(set(win_ticket))

winning: list = Lottery.get_winning_numbers()
print(f"Winning numbers:\n",*winning)

#9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. 
#Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins. Print a message reporting
#how many times the loop had to run to give you a winning ticket.


my_ticket: list = Lottery.get_my_ticket()
i: int = 1
while not Lottery.check_winning(winning, my_ticket):
    my_ticket = Lottery.get_my_ticket()
    i += 1
print(f"\nnumber of tries: {i}",end="\n\n")