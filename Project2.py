import random

number_to_guess = random.randint(1, 100)
x = 1 
y = 10 
success = False

user_guess = int(input("Guess the number (between 1 and 100): "))

while y > 0:
    if user_guess > number_to_guess:
        y -= 1
        print(f"Too high! Try again. You have {y} tries left.")
    elif user_guess < number_to_guess:
        y -= 1
        print(f"Too low! Try again. You have {y} tries left.")
    else:
        print(f"Congratulations, you guessed it in {x} attempts!")
        success = True
        break 
    
    if y > 0:
        user_guess = int(input("Guess again: "))
    
    x += 1

if not success:
    print("Game over! Better luck next time!")
