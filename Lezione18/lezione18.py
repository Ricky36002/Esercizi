# 1) Safe Square Root: Write a function safe_sqrt(number) that calculates the square root of a number using math.sqrt(). 
# Handle ValueError if the input is negative by returning an informative message.

import math
def safe_sqrt(number):
    try:
        return math.sqrt(number)
    except ValueError:
        return "Error: Input should be a non-negative number."
    



# 2) Password Validation: Write a function validate_password(password) that checks if a password meets certain criteria 
# (i.e., minimum length of 20 characters, at least three uppercase characters, and at least four special characters). 
#  Raise a custom exception (e.g., InvalidPasswordError) for invalid passwords.
class InvalidPasswordError(Exception):
    pass

def validate_password(password):
    if len(password) < 20:
        raise InvalidPasswordError("Password should be at least 20 characters long.")
    uppercase_count = sum(1 for char in password if char.isupper())
    if uppercase_count < 3:
        raise InvalidPasswordError("Password should have at least three uppercase characters.")
    special_chars = "!@#$%^&*()_+=-{}[]|;:',.<"
    special_count = sum(1 for char in password if char in special_chars)
    if special_count < 4:
        raise InvalidPasswordError("Password should have at least four special characters.")
    return "Password is valid."
    



# 3) Context Managers for File Handling: Use the with statement and context managers to open and close a file. Handle potential 
# IOError within the with block for clean resource management.

def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content
        
# 4) Database of dates:  Write a class that manages a database of dates with the format gg.mm.aaaa implementing methods to add a new date, delete a given date, modify a date, and perform a query on a given date is required.  A query on a given date allows for retrieving a given new date. Note that a date is an object for your database; it must be instantiated from a string.

class Date:
    def __init__(self, date_str):
        self.day, self.month, self.year = map(int, date_str.split('.'))
        

# 5) An interactive calculator: It is required to develop an interactive calculator with at least 10 test cases using UnitTest
# trying to (possibly) cover all execution paths! User input is assumed to be a formula that consists of a number, an operator
# (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check
#  whether the resulting list is valid:
    #     If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
    #     Try to convert the first and third inputs to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError.
    #     If the second input is not '+' or '-', again raise a FormulaError.
    #     If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, until the user enters quit.




# 6) Personalized math library: Create a Python library that provides functions for handling fractions, with built-in error 
# handling. The library must include functions for the following operations:
    #     Create a fraction from the numerator and denominator.
    #     Collect the numerator and denominator of a fraction.
    #     Simplify a fraction.
    #     Add, subtract, multiply and divide fractions.
    #     Check whether one fraction is equivalent to another. 
    #     All library functions must use the try-except block to handle potential errors, such as null denominators, unsupported operations, or division by zero. The library must raise custom exceptions to indicate specific errors to the user.





#  7) Custom Exception for Data Structure Integrity: Define a custom exception class DataStructureIntegrityError.  
# Define the custom data structure linked list use classes with methods to append, remove and access a given element, 
# and write functions that operate on that (i.e., print the list,  reverse the list, and check whether the list is ordered). 
# Raise this exception if the data structure's integrity is compromised (e.g., empty list access, index error).
