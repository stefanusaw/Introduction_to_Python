def numberException(): 
    while True:
        try:
            n = int(input("Enter a number: "))
            print(f"100 divided by {n} is {100/n}")
            break
        except ZeroDivisionError:
            print("Oops! You cannot divide by zero.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        
numberException()
# Task 2 - Types of Exceptions

def raise_and_handle_exceptions():
    try:
        # A list with 3 elements has index 0, 1, and 2
        my_list = [10, 20, 30]
        # Accessing an index that is out of range (index 5 doesn't exist)
        print(my_list[5])
    except IndexError:
        # This block is executed when an IndexError is raised
        print("IndexError occurred! List index out of range.")
    
    try:
        # A dictionary with two key-value pairs, keys are name and age
        my_dict = {"name": "Alice", "age": 25}
        # Trying to access a non-existent key 'address'
        print(my_dict["address"])
    except KeyError:
        # This block is executed when a KeyError is raised
        print("KeyError occurred! Key not found in the dictionary.")
    
    try:
        # Attempting to add a string and an integer, which causes a TypeError
        result = "Age: " + 25  # String + integer will cause TypeError
        print(result)
    except TypeError:
        # This block is executed when a TypeError is raised
        print("TypeError occurred! Unsupported operand types.")

raise_and_handle_exceptions()

# Task 3 - Using try except else finally
def try_except_else_finally():
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    result = 0
    try:
        result = x / y
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    else:
        print(f"The result is {result}.")
    finally:
        print("Thank you for testing this function! Cheers")

try_except_else_finally()
