import string

user_input = input("Enter a password: ")
score = 10
special_char = "@#$"

warning = "Sorry, your password needs at least"

if len(user_input) < 8:
    warning += " 8 characters"
    score -= 2
if not any(char.isupper() for char in user_input):
    warning += " one uppercase letter"
    score -= 2
if not any(char.islower() for char in user_input):
    warning += " one lowercase letter"
    score -= 2
if not any(char.isdigit() for char in user_input):
    warning += " one digit"
    score -= 2
if not any(char in special_char for char in user_input):
    warning += " one special character"
    score -= 2

if len(warning) > 35:
    print(warning + f". Password strength is {score}")
else:
    print(f"Your password is strong! The strength score is {score}💪")
