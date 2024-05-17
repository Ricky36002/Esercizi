#Write a function to find all numbers divisible by 7, not a multiple of 5, between 2000 and 3200 (both included). The numbers should be stored in a list and returned as output.

'''
def find_numbers():
    numbers = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:

            numbers.append(i)

    return numbers
Result = find_numbers()
print(Result)
'''

#Write a function to calculate the factorial of a number given as input. The number should be returned as output. For example:

#    Input: 8
#    Output: 40320

'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))
'''




#Use the function implemented in Exercise 2 to compute all factorial numbers of a list of numbers. The list is given as input to the function. All factorials should be returned as output. For example:

#    Input: [2, 5, 8, 10]
#    Output: [2, 120, 40320, 3628800]

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def compute_factorials(numbers):
    return [factorial(num) for num in numbers]

numbers = [3, 6, 11, 17]
print("Factorials of", numbers, "are", compute_factorials(numbers))

#Given an integer n as input, write a function to generate a dictionary that contains (i, i*i) as (key, value) pairs such that
#i is an integer between 1 and n (both included). The function should return the dictionary as output. For example:

#    Input: 8
#    Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def dictionary_numbers(n):
    return{i: i*i for i in range(1, n+1)}

n= 11
print(dictionary_numbers(n))







#Write a function that accepts a string with a comma-separated sequence of words as input and prints the words as a comma-separated sequence after sorting them alphabetically. For example:

#    Input: without,hello,bag,world
#    Output: bag,hello,without,world
























































