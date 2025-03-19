# Task 1

string = "Python is amazing!"
first_word = string[:6]
amazing = string[10:17]
reversed = string[::-1]
print(f"First word: {first_word}")
print(f"Amazing part: {amazing}")
print(f"Reversed string: {reversed}")

# Task 2
string2 = " hello, python world! "
string2_stripped = string2.strip()
string2_capitalized = string2.capitalize()
string2_replaced = string2.replace("world", "universe")
string2_uppercased = string2.upper()
print(f"strip(): {string2_stripped}")
print(f"capitalize(): {string2_capitalized}")
print(f"replaced(): {string2_replaced}")
print(f"uppercase(): {string2_uppercased}")


# Task 3
user_input = input("Enter a word: ")
if user_input == user_input[::-1]:
    print(f"Yes, \'{user_input}\' is a palindrome!")
else:
    print(f"No, \'{user_input}\' is not a palindrome!")
