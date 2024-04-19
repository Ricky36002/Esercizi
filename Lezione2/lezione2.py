#Riccardo Russo
# 17/04/2024

#Use a variable to represent a person's name,
#and print a message to that person.
#Your message should be simple, such as,
#"Hello eric, would you like to lear some python today?"
print ("Hello!")

name: str = "Giggio"
message: str = f"Ciao {name} ti va di mangiare un boccone?"
print (message)

#Use a variable to represent a person’s name, 
#and then print that person’s name in lowercase, 
#uppercase, and title case.

Name: str = "Alex"
print (Name.upper())
print (Name.lower())
print (Name.title())

#Find a quote from a famous person you admire. 
#Print the quote and the name of its author. 
#Your output should look something like the following, 
#including the quotation marks:Albert Einstein once said,
# “A person who never made a mistake never tried anything new.”

NAme: str = "Madara Uchiha"
Message: str = "\" Wake up to reality! Nothing ever goes as planned in this accursed world. The longer you live, the more you realize that the only things that truly exist in this reality are merely pain. suffering and futility. Listen, everywhere you look in this world, wherever there is light, there will always be shadows to be found as well. As long as there is a concept of victors, the vanquished will also exist. The selfish intent of wanting to preserve peace, initiates war. and hatred is born in order to protect love. There are nexuses causal relationships that cannot be separated - Madara Uchiha, \""
print (f"{NAme} once said: {Message}")

#Repeat Exercise 2-5, but this time, represent the famous person’s 
#name using a variable called famous_person. Then compose your message 
#and represent it with a new variable called message.
# Print your message.

famus_person = ({NAme})
Message: str ="\" Wake up to reality! Nothing ever goes as planned in this accursed world. The longer you live, the more you realize that the only things that truly exist in this reality are merely pain. suffering and futility. Listen, everywhere you look in this world, wherever there is light, there will always be shadows to be found as well. As long as there is a concept of victors, the vanquished will also exist. The selfish intent of wanting to preserve peace, initiates war. and hatred is born in order to protect love. There are nexuses causal relationships that cannot be separated - Madara Uchiha,\""
print (f"{famus_person} once said:{Message}")

#Python has a removesuffix() method that works exactly like removeprefix().
#Assign the value 'python_notes.txt' to a variable called filename.
#Then use the removesuffix() method to display the filename without
#the file extension, like some file browsers do.

filename: str = "python_note.txt"
print (f"nome senza suffisso {filename.removesuffix('.txt')}")

#Store the names of a few of your friends in a list called names. 
#Print each person’s name by accessing each element in the list,
#one at a time.
Names = ["Simo", "Ema", "Ste", "Ale", "Carlo"]
first_name = Names [0]
secon_name = Names [1]
third_name = Names [2]
fourth_name = Names [3]
last_name = Names [4]

print (first_name)
print (secon_name)
print (third_name)
print (fourth_name)
print (last_name)

#Start with the list you used in Exercise 3-1, but instead of just
#printing each person’s name, print a message to them. 
#The text of each message should be the same, but each message 
#should be personalized with the person’s name.

print (f"hi {first_name}, how are you?")
print (f"hi {secon_name}, how are you?")
print (f"hi {third_name}, how are you?")
print (f"hi {fourth_name}, how are you?")
print (f"hi {last_name}, how are you?")

#Think of your favorite mode of transportation,such as a motorcycle 
#or a car, and make a list that stores several examples. Use your list 
#to print a series of statements about these items, such as 
#“I would like to own a Honda motorcycle.”

Transportation = ["auto", "bus", "train"]

Motivation_one = "confort, fast and cheap"
Motivation_two = "slow, never on time, cheap"
Motivation_three = "convinient for long trips"

Tra_one = Transportation [0]
Tra_two = Transportation [1]
Tra_three = Transportation [2]

print (f"i prefer {Tra_one} becouse {Motivation_one}")
print (f"i hate {Tra_two}becouse {Motivation_two}")
print (f"i prefer {Tra_three} becouse {Motivation_three}")

#If you could invite anyone, living or deceased, to dinner, who 
#would you invite? Make a list that includes at least three people
#you’d like to invite to dinner. Then use your list to print a 
#message to each person, inviting them to dinner.

Invited_person = ["Giorgio", "Robert", "Giggio"]
first_invite = Invited_person [0]
second_invite = Invited_person [1]
third_invite = Invited_person [2]
MEssage: str = f"Hi, i would like to invita you to a dinner Mr."
print (f"{MEssage}{first_invite}")
print (f"{MEssage}{second_invite}")
print (f"{MEssage}{third_invite}")

#You just heard that one of your guests can’t make the dinner,
#so you need to send out a new set of invitations.
#You’ll have to think of someone else to invite.
# -Start with your program from Exercise 3-4. Add a print() call 
#at the end of your program, stating the name of the guest who can’t make it.
# -Modify your list, replacing the name of the guest who can’t 
#make it with the name of the new person you are inviting.
# -Print a second set of invitation messages, one for each person 
#who is still in your list.

Invited_person.remove ("Giggio")
Invited_person.append ("Gino")
Invited_person.append ("Saverio")
fourth_invite = Invited_person [2]
fifth_invite = Invited_person [3]
print (f"{MEssage}{first_invite} i also want to worn you that {third_invite} will not make it")
print (f"{MEssage}{second_invite} i also want to worn  you that {third_invite} will not make it")
print (f"{MEssage}{fourth_invite} i also want to worn  you that {third_invite} will not make it")
print (f"{MEssage}{fifth_invite} i also want to worn  you that {third_invite} will not make it")

#You just found a bigger dinner table, so now more space is available. 
#Think of three more guests to invite to dinner.
#• Start with your program from Exercise 3-4 or 3-5. Add a print() 
#call to the end of your program, informing people that you found a bigger table.
#• Use insert() to add one new guest to the beginning of your list.
#• Use insert() to add one new guest to the middle of your list.
#• Use append() to add one new guest to the end of your list.
#• Print a new set of invitation messages, one for each person in your list.


MEssage2: str = f"and also i found a bigger table so i invited more people"
Invited_person.append ("Teemo")
Invited_person.append ("Roket")
Invited_person.append ("Simus")
sixth_invite = Invited_person [4]
seventh_invite = Invited_person [5]
eighth_invite = Invited_person [6]

print (f"{MEssage}{first_invite} i also want to worn you that {third_invite} will not make it {MEssage2}")
print (f"{MEssage}{second_invite} i also want to worn you that {third_invite} will not make it {MEssage2}")
print (f"{MEssage}{fourth_invite} i also want to worn you that {third_invite} will not make it {MEssage2}")
print (f"{MEssage}{fifth_invite} i also want to worn you that {third_invite} will not make it {MEssage2}")
print (f"{MEssage}{sixth_invite} i also want to worn you that {third_invite} will not make it {MEssage2}")
print (f"{MEssage}{seventh_invite} i also want to worn you that {third_invite} will not make it {MEssage2}")
print (f"{MEssage}{eighth_invite} i also want to worn you that {third_invite} will not make it {MEssage2}")

#You just found out that your new dinner table won’t arrive in time for 
#the dinner, and now you have space for only two guests.
#• Start with your program from Exercise 3-6. Add a new line that prints
# a message saying that you can invite only two people for dinner.
#• Use pop() to remove guests from your list one at a time until only 
#two names remain in your list. Each time you pop a name from your list,
#print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#• Print a message to each of the two people still on your list, letting them know they’re still invited.
#• Use del to remove the last two names from your list, so you have an 
#empty list. Print your list to make sure you actually have an empty list at the end of your program.

Message3: str = f"i have to inform you that i can invite only two people for dinner."

print (Invited_person)

print (f"Hello {Invited_person.pop(0)} we have to pospone the dinner for some problem.")
print (f"Hello {Invited_person.pop(0)} we have to pospone the dinner for some problem.")
print (f"Hello {Invited_person.pop(0)} we have to pospone the dinner for some problem.")
print (f"Hello {Invited_person.pop(0)} we have to pospone the dinner for some problem.")
print (f"Hello {Invited_person.pop(0)} we have to pospone the dinner for some problem.")

print (Invited_person)

print (f"Hi,{seventh_invite} for some problem {Message3} I choose you.")
print (f"Hi,{eighth_invite} for some problem {Message3} I choose you.")

del Invited_person [0]
del Invited_person [0]
print (Invited_person)

#Think of at least five places in the world you’d like to visit.
#• Store the locations in a list. Make sure the list is not in alphabetical order.
#• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
#• Use sorted() to print your list in alphabetical order without modifying the actual list.
#• Show that your list is still in its original order by printing it.
#• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
#• Show that your list is still in its original order by printing it again.
#• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
#• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#• Use sort() to change your list so it’s stored in reverse-alphabetical order.
#Print the list to show that its order has changed.

Places: str = ["Home", "Haven", "Hell", "Canada", "Otario"]

print (Places)
Places.sort ()
print (Places)
Places.sort (reverse = True)
print (Places)
Places.reverse ()
print (Places)
Places.reverse ()
print (Places)
Places.sort ()
print (Places)
Places.sort (reverse = True)
print (Places)

#Working with one of the programs from Exercises 3,
# use len() to print a message indicating the number 
#of people you’re inviting to dinner.

print (Names)

print (f"The list {Names} is long {len(Names)}")

#Think of things you could store in a list. For example, you could make
#a list of mountains, rivers, countries, cities, languages, or anything 
#else you’d like. Write a program that creates a list containing these 
#items and then uses each function introduced in this chapter at least once.

List1: str = ["Hero", "Legend", "Weapon", "Story", "Adventure"]
last_message: str ="\" This list is what i serch in a D&D adventure:\""

print (f"{last_message} {List1}")

First_List = List1 [0]
Last_List = List1 [4]
print (First_List)
print (Last_List)

print (First_List.upper())
print (First_List.lower())
print (First_List.title())

List1.append ("Luck")
print (List1)

print (List1)
List1.sort ()
print (List1)
List1.reverse ()
print (List1)

List1.remove ("Legend")
List1.pop (0)
del List1 [2]
print (List1)

#Use a dictionary to store information about a person you know. 
#Store their first name, last name, age, and the city in which they live. 
#You should have keys such as first_name, last_name, age, and city. 
#Print each piece of information stored in your dictionary.

First_Name = {"Percy": "Percy"}
Last_Name = {"Percy": "Minter"}
Age1 = {"Percy": "22"}
City = {"Percy": "Brabber"}

Percy = First_Name ["Percy"], Last_Name ["Percy"], Age1 ["Percy"], City ["Percy"]
print (Percy)

#Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary.
#Think of a favorite number for each person, and store each as a value in your dictionary. 
#Print each person’s name and their favorite number. For even more fun, poll a few friends
#and get some actual data for your program.

Numbers_p = {"Riccardo": "11", "Edwin": "17", "Federico": "5", "Mikolaj": "4", "Edoardo": "7"}
numbers = Numbers_p ["Riccardo"], Numbers_p ["Edwin"], Numbers_p ["Federico"], Numbers_p ["Mikolaj"], Numbers_p ["Edoardo"]
print (numbers)

#A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#• Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your
# glossary, and store their meanings as values.
#• Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then 
#its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline 
#character (\n) to insert a blank line between each word-meaning pair in your output.














