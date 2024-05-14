#22/04/2024
# Funzioni 

#Think of at least three kinds of your favorite pizza. Store these pizza names in a list, 
#and then use a for loop to print the name of each pizza.
#• Modify your for loop to print a sentence using the name of the pizza, instead of printing
#just the name of the pizza. For each pizza, you should have one line of output containing a
# simple statement like I like pepperoni pizza.
#• Add a line at the end of your program, outside the for loop, that states how much you like pizza.
#The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as 
#I really love pizza!

Pizza = ["Diavola", "Margherita", "Cibarium"]
print (f"Le mie pizze prferite sono:")
for Esempio in Pizza:
    print (Esempio)
print ("\nLe mie preferite sono:")
for Esempio in Pizza:
    if Esempio == "Diavola":
        print ("La mia pizza preferita è la Diavola")

    elif Esempio == "Margherita":
        print ("MI piace molto anche la Margherita")

    else:
        print ("Adoro anche la Cibarium")
print ("\nAmo mangiare le pizze")


#Think of at least three different animals that have a common characteristic.  
# Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
#• Modify your program to print a statement about each animal, such as A dog would make a great pet.
#• Add a line at the end of your program, stating what these animals have in common. You could print a sentence, 
#such as Any of these animals would make a great pet!

Animal = ["Gecko", "Cobra", "Alligator"]
print ("All of them are reptil and have scails:")
for animal in Animal:
    print (animal)
print ("\nAll of them are reptil and have scails:")
for animal in Animal:
    if animal == "Gecko":
        print ("Geko are super cute")

    elif animal == "Cobra":
        print ("Cobra are dangerous and poisonus")
    
    else: 
        print ("Alligator can eat u alive")

#Use a for loop to print the numbers from 1 to 20, inclusive.

for i in range(1, 21, 1):
    print (i)

#Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
#(If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)

x: int =1
while (x<1000000):
    x += 1
    #print (x) 

#Make a list of the numbers from one to one million, and then use min() and max() to make sure your
# list actually starts at one and ends at one million. Also, use the sum() function to see how quickly 
#Python can add a million numbers.


x: int =0
num = []
while (x<1000000):
    x += 1
    num.append (x)
print (min(num), max(num), sum(num))

#Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. 
#Use a for loop to print each number.

for i in range(1, 21, 1):
    print (i)

#Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.

x: int =0
while (x<30):
    x += 3
    print (x)

#A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python.
#Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to
#print out the value of each cube.

numbers: list = []
for i in range(1, 11):
    numbers.append (i**3)
for num in numbers:
    print (num)

#Use a list comprehension to generate a list of the first 10 cubes.

numbers: list = [i**3 for i in range(1,11)]
print(numbers)

#Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
# • Print the message The first three items in the list are:. Then use a slice to print the first three items from that 
#program’s list.
# • Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle 
#of the list.
# • Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.


print (numbers[0:3])
print (numbers[len(numbers)//2:len(numbers)//2+3])
print (numbers[len(numbers)-3:])

#4.11
# Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. 
# Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new 
#pizza is stored in the appropriate list.
Pizzas = ["Diavola", "Margherita", "Cibarium", "Boscaiola"]
Friend_Pizzas = ["Diavola", "Margherita", "Cibarium"]
Friend_Pizzas.append ("4 Formaggi")

print (f"My favorite pizzas are:")
for pizza in Pizzas:
    print (pizza)

print (f"My friend's favorite pizzas are:")
for pizzas in Friend_Pizzas:
    print (pizzas)

#4.12
#All versions of foods.py in this section have avoided using for loops when printing, to save space. Choose a version of foods.py, 
#and write two for loops to print each list of foods.

# cibo preferito 
Mio_Cibo = ["Pasta", "Pizza", "Fast Food"]
Altri_Cibo = ["Carne", "Proteine", "Verdure"]

print (f"my favorite foods are:")
for cibo in Mio_Cibo:
    print (cibo)

print ("\n my friend favorite foods are:")
for Cibo in Altri_Cibo:
    print (Cibo)


#5.1
#Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test.
# Your code should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# • Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
# • Create at least 10 tests. Have at least 5 tests evaluate to True and another
# 5 tests evaluate to False.



def buddle_sort(A : list)-> list:
    for i in range(len(A)):
        for j in range(len(A)-1):
            if A[j] > A[j+1]:
                temp: int = A[j]
                A[j]= A[j+1]
                A[j+1] = temp
    return A






            


