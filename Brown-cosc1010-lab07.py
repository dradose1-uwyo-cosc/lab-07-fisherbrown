# Fisher Brown
# UWYO COSC 1010
# Submission Date: 29 Oct 24
# Lab 07
# Lab Section: 10
# Sources, people worked with, help given to: 
# your
# comments
# here


# Prompt the user for an upper bound 
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered
while True:
    upper_bound = input('enter an upper bound to return the factorial: ')
    if upper_bound.isnumeric():
        break
upper_bound = int(upper_bound)
fact = 1
while upper_bound > 0:
    fact *= upper_bound
    upper_bound -= 1

print(f"The result of the factorial based on the given bound is {fact}")

print("*"*75)
# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 
fire = True
num_sum = 0
while fire:
    value = input('enter a number to be totaled up, type exit to end program: ')
    if value.isnumeric():
       value = int(value)
       num_sum += value
    elif '-' in value:
        value = value.replace('-',' ')
        value = int(value)
        num_sum += -1*value
    elif value.lower() == "exit":
        fire = False
    else:
        print('make sure input is a number')

print(f"Your final sum is {num_sum}")

print("*"*75)
# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input 
calc = input('enter a calculation to be made in the form `operand operator operand`, type exit to leave program: ')
calc = calc.replace(' ','')
 
number = []
ghost = True 
while ghost:

    calc = input('enter a calculation to be made in the form `operand operator operand`, type exit to leave program: ')

    calc = calc.replace(' ','')

    if calc.lower() == "exit":

        ghost = False

    if '+' in calc:
        






        
    

        