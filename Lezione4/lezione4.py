#8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in 
# this chapter. Call the function, and make sure the message displays correctly.
print("# Exercise 8-1:\n")

def display_message():
    print("I'm learning about functions!\n")

display_message()


# 8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. 
# The function should print a message, such as "One of my favorite books is Alice in Wonderland". 
# Call the function, making sure to include a book title as an argument in the function call.
print("# Exercise 8-2:\n")

def favorite_book(title: str):
    print(f"My favorite book is {title}.\n")

favorite_book(title = "One punch man")


# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it. 
# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
print("# Exercise 8-3:\n")

def make_shirt(size: str = 'large', message: str = 'I hate Python.'):
    print(f"The shirt will be {size} in size with \"{message}\" as a message\n")

make_shirt("small","I love Python!")
make_shirt(size = "medium", message = "One punchhh!")


# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
print("# Exercise 8-4:\n")

make_shirt()
make_shirt('medium')
make_shirt('small','QT3.14')

# 8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. 
# The function should print a simple sentence, such as Reykjavik is in Iceland. 
# Give the parameter for the country a default value. 
# Call your function for three different cities, at least one of which is not in the default country.
print("# Exercise 8-5:\n")

def describe_city(city: str,country: str = 'Italy'):
    print(f"{city.capitalize()} is in {country.capitalize()}.\n")

describe_city('rome')
describe_city('milan')
describe_city('moscow','russia')

# 8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. 
# The function should return a string formatted like this: "Santiago, Chile". 
# Call your function with at least three city-country pairs, and print the values that are returned.
print("# Exercise 8-6:\n")

def city_country(city: str,country: str) -> str:
    message: str = city + ', ' + country + '.'
    return message

print(city_country('Santiago','Chile'))
print(city_country('Rome','Italy'))
print(city_country('Tokyo','Japan'))

print()

# 8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. 
# The function should take in an artist name and an album title, and it should return a dictionary containing 
# these two pieces of information. Use the function to make three dictionaries representing different albums. 
# Print each return value to show that the  dictionaries are storing the album information correctly. 
# Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
# If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
# Make at least one new function call that includes the number of songs on an album.
print("# Exercise 8-7:\n")

def make_album(artist_name: str, album_title: str, songs_number: int = None) -> dict:
    album: dict = {}
    if songs_number is None:
        album = {artist_name:album_title}
    else:
        album = {artist_name:album_title, album_title:songs_number}
    return album

print(make_album('Imagine Dragons','Origins'))
print(make_album('The Beatles','White Album'))
print(make_album('Prince','Purple Rain'))
print(make_album('Pink Floyd','The Dark Side of the Moon',9))

print()
# 8-8. User Albums: Start with your program from Exercise 8-7. 
# Write a while loop that allows users to enter an album’s artist and title. 
# Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
# Be sure to include a quit value in the while loop.
print("# Exercise 8-8:\n")

check: bool = True
user_input1: str; user_input2: str; user_input3: str

while check:
    user_input1 = input("Insert Artist's name: ")
    user_input2 = input("Insert Album's name: ")
    print(f"\nArtist's name is: {user_input1}; Album's name is: {user_input2}\n")
    user_input3 = input("Do you want to continue? (s): ")
    if user_input3.lower() == 's':
        check = False

print(f"\n{make_album(user_input1,user_input2)}\n")

# 8-9. Messages: Make a list containing a series of short text messages. 
# Pass the list to a function called show_messages(), which prints each text message.
print("# Exercise 8-9:\n")

messages_list1: list = ['I love Python','The abyss stared back','101001001011','cool guy']

def show_messages(messages: list):
    for message in messages:
        print(f"{message}")
    print()

show_messages(messages_list1)

# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
# Write a function called send_messages() that prints each text message and moves each message to a new list
# called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages
# were moved correctly.
print("# Exercise 8-10:\n")

def send_messages(messages: list) -> list:
    sent_messages: list = []
    for message in messages:
        print(f"{message}")
        sent_messages.append(message)
    print()
    return sent_messages

messages_list2: list = send_messages(messages_list1)

print(f"{messages_list1}\n{messages_list2}")

print()

# 8-11. Archived Messages: Start with your work from Exercise 8-10.
# Call the function send_messages() with a copy of the list of messages.
# After calling the function, print both of your lists to show that the original list has retained its messages.
print("# Exercise 8-11:\n")

messages_list3: list = send_messages(messages_list2)

print(f"{messages_list1}\n{messages_list3}")

print()


# 8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function call provides, 
# and it should print a summary of the sandwich that’s being ordered. 
# Call the function three times, using a different number of arguments each time.
print("# Exercise 8-12:\n")

def order_sandwich(*items):
    sandwich: list = items
    print(f"Summary: {sandwich}\n")

order_sandwich('Tomato','Salad','Avocado')
order_sandwich('Cheese','Prosciutto')
order_sandwich('BBQ Sauce','Pulled Pork','Bacon','Cheese')


# 8-13. User Profile:  Build a profile of yourself by calling build_profile(), 
# using your first and last names and three other key-value pairs that describe you.
# All the values must be passed to the function as parameters.
# The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"
print("# Exercise 8-13:\n")

def build_profile(first_name: str, last_name: str, **kwargs) -> str:
    message = f"{first_name} {last_name}"
    if kwargs:
        for item in kwargs.items():
            message += f", {item[0]} {item[1]}"
    return message

print(f"{build_profile('Riccardo','Russo',age = 21,hair = 'dark brown',weight = 90)}\n")


# 8-14. Cars: Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name.
# It should then accept an arbitrary number of keyword arguments.
# Call the function with the required information and two other name-value pairs,
# such as a color or an optional feature.
# Your function should work for a call like this one: 
# car = make_car('subaru', 'outback', color='blue', tow_package=True) Print the dictionary that’s returned to make 
# sure all the information was stored correctly. 
print("# Exercise 8-14:\n")

def make_car(manufacturer: str,model_name: str, **kwargs) -> dict:
    dictionary: dict = {'manufacturer':manufacturer,'model name':model_name}
    if kwargs:
        dictionary = dictionary | kwargs
    return dictionary

print(f"{make_car('subaru','outback',color='blue',tow_package=True)}\n")


# 8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py.
# Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.

# Non so come fare =(

# 8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file.
# Import the function into your main program file, and call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

