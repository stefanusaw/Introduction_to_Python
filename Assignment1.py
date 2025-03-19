# Task 1 - Variables: Your first python intro
name = "Stefanus"
age = 24
height = 5.9

print(f"Hey there, my name is {name}! I'm {age} years old and {height} tall!")

# Task 2- Operators: Playing with Numbers
num1 = 12
num2 = 27
print(f"The sum of {num1} and {num2} is", num1+num2, ". Did you know? 1+2=3, and 2+7=9, making them 39. This is why 39 is considered a beautiful number")


# Task 3 - Conditional Statements: The Number Checker
print("Welcome to the number checker, please give me a number: ")
number = int(input())

if number > 0:
    print("This number is positive. Awesome!")
elif number < 0:
    print("This number is negative. Better luck next time!")
else:
    print("Zero it is. A perfect balance!")
