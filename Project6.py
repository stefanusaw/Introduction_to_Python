import logging

# Set up logging configuration
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, 
                    format='%(levelname)s:%(asctime)s:%(message)s')

def menu():
    while True:
        try:
            n = int(input("Welcome to Error-Free Calculator! Choose an operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit\n"))
            if n == 5:
                print("Exiting the calculator. Goodbye!\n")
                break 
        except ValueError as e:
            logging.error(f"ValueError occurred: {e}")
            print(f"Error: {e}\n")
            continue 
        
        while True:
            try:
                num1 = int(input("Enter the first number: "))
                break
            except ValueError as e:
                logging.error(f"ValueError occurred: {e}")
                print(f"Error: {e}\n")
        
        while True:
            try:
                num2 = int(input("Enter the second number: "))
                break
            except ValueError as e:
                logging.error(f"ValueError occurred: {e}")
                print(f"Error: {e}\n")
            except ZeroDivisionError as e:
                logging.error(f"ZeroDivisionError occurred: {e}")
                print(f"Error: {e}\n")
            
        if n == 1:
            print(addition(num1, num2))
        elif n == 2:
            print(subtraction(num1, num2))
        elif n == 3:
            print(multiplication(num1, num2))
        elif n == 4:
            print(division(num1, num2))
    
        
        
def addition(num1, num2):
    return num1+num2


def subtraction(num1, num2):
    return num1-num2


def multiplication(num1, num2):
    return num1*num2


def division(num1, num2):
    if num2 == 0:
        logging.error(f"ZeroDivisionError occurred: Division by zero")
        return "Error: Cannot divide by zero."
    return num1 / num2


menu()