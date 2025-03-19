def greet_user(name):
    print(f"Hello, {name}! Welcome aboard.")
    
def add_numbers(num1, num2):
    print(f"The sum of {num1} and {num2} is {num1+num2}")
    
greet_user("Alice")
add_numbers(5, 10)


def describe_pet(pet_name, animal_type):
    print(f"I have a {animal_type} named {pet_name}.")
    
describe_pet("Buddy", "dog")
describe_pet("Whiskers", "cat")


def make_sandwich(*args):
    print("Making a sandwich with the following ingredients: ")
    for ing in args:
        print(f"- {ing}")
    
make_sandwich("Lettuce", "Tomato", "Cheese")


def factorial(n):
    if n == 1:
        return n
    return n * factorial(n-1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
        

val = 5
x = factorial(val)
y = fibonacci(val)
print(f"Factorial of {val} is {x}. The {val}th Fibonacci number is {y}")