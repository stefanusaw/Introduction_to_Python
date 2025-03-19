# Task 1
fav_fruits = ["apple", "watermelon", "lemon", "strawberry", "orange"]
print(f"Original list: {fav_fruits}")
fav_fruits.append("grape")
print(f"After adding a fruit: {fav_fruits}")
fav_fruits.remove("lemon")
print(f"After removing a fruit: {fav_fruits}")
print(f"Reversed list: {fav_fruits[::-1]}")

# Task 2
my_info = {"name": "Stefanus", "age": 22, "city": "Toronto"}
print(my_info)
my_info["favorite color"] = "red"
print(f"Added fav color: {my_info}")
my_info["city"] = "New York"
keys = "Keys: "
for key in my_info.keys():
    keys += f"{key} | "
print(keys)
vals = "Values: "
for val in my_info.values():
    vals += f"{val} | "
print(vals)

# Task 3
my_tuple = ("avengers", "stay the same", "atomic habits")
print(f"Favorite things: {my_tuple}")
try:
    my_tuple[0] = "catch me if you can"
except:
    print("Oops! Tuples cannot be mutated")
print(f"Length of tuple: {len(my_tuple)}")