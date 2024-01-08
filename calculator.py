# Author: Sreelakshmi Odatt Venu
# Date Created: 20/12/2023

# Function to add two numbers
def add_number(a, b):
    return a + b

# Function to subtract two numbers
def subtract_number(a, b):
    return a - b

# Function to multiply two numbers
def multiply_number(a, b):
    return a * b

# Function to divide numbers, handling division by zero
def divide_number(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"

# Get user input for the first number , check if the user input the valid first digit and handle the exception
while True:
    try:
        number_1 = float(input("Enter the first number: "))
        break
    # if worng input or invalid input display error 
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Get user input for the operator , check if the user input the valid operator and if not , handle the exception
while True:
    operator = input("Enter the operator (+, -, *, /): ")
    if operator in ('+', '-', '*', '/'):
        break
      # if worng input or invalid input display error 
    else:
        
        print("Please enter a valid operator.")

# Get user input for the second number check if the user input the valid second number and if not , handle the exception
while True:
    try:
        number_2 = float(input("Enter the second number: "))
        break
    except ValueError:
        print("Please enter a valid number.")

# Perform calculation based on the operator and user input 
if operator == '+':
    result = add_number(number_1, number_2)
elif operator == '-':
    result = subtract_number(number_1, number_2)
elif operator == '*':
    result = multiply_number(number_1, number_2)
elif operator == '/':
    result = divide_number(number_1, number_2)
else:
    result = "Error ! "

# Display the calculated result 

print(f"Result: {result}")
