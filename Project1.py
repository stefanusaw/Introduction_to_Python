# Project: Eligible Elector
while True:
    try:
        age = int(input("How old are you? "))
        break  # Exit the loop if input is valid, go to the conditional checks
    except ValueError:
        print("That's not a valid number. Please try again.")

if age < 0:
    print("That is impossible, how did you age backward?")
elif age >= 18:
    print("Congratulations! You are eligible to vote. Go make a difference!")
elif age < 18:
    x = 18 - age # count the years left before the user turns 18
    print(f"Oops! You're not eligible yet. But hey, only {x} more years to go!")
