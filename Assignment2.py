# Task 1
import time
while True:
    try:
        number = int(input("Counting Down with Loops - Enter the starting number (1 to 20): "))       
        if 1 <= number <= 20:
            break
        else:
            print("Please enter a number between 1 and 20.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        
while number > 0:
    print(number, end=" ")
    time.sleep(1)
    number -= 1
print("Blast off! 🚀")

 #Task 2
num2 = int(input("Multiplication Table with for Loops - Input a number: "))
for x in range(1, 11):
    print(f"{num2} * {x} = {num2 * x}")


# Task 3
num3 = int(input("Find the Factorial - Give me a number: "))
ans = 1
for i in range(1, num3+1):
    ans *= i
print(f"The factorial of {num3} is {ans}")
