# Creating a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Updating dictionary values
my_dict.update({"age": 32, "city": "Los Angeles"})
print(my_dict)  # Output: {'name': 'John', 'age': 32, 'country': 'USA', 'city': 'Los Angeles'}

# Removing key-value pairs
del my_dict["city"]
print(my_dict)  # Output: {'name': 'John', 'age': 32, 'country': 'USA'}

# Removing all key-value pairs
my_dict.clear()
print(my_dict)  # Output: {}

# Removing and returning the value associated with the key "age"
age = my_dict.pop("age")
print(age)  # Output: 30
print(my_dict)  # Output: {'name': 'John', 'city': 'New York'}



# Accessing dictionary values
print(my_dict["name"])  # Output: John
print(my_dict.get("age"))  # Output: 30
print(my_dict["city"])  # Output: New York
# Modifying dictionary values
my_dict["age"] = 31
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

# Adding new key-value pairs
my_dict["country"] = "USA"
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'country': 'USA'}

# Removing key-value pairs
del my_dict["city"]
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'country': 'USA'}

# Checking if a key exists
if "name" in my_dict:
    print("Key 'name' exists")  # Output: Key 'name' exists

# Getting all keys and values
keys = my_dict.keys()
values = my_dict.values()
print(keys)  # Output: dict_keys(['name', 'age', 'country'])
print(values)  # Output: dict_values(['John', 31, 'USA'])

# Getting the number of key-value pairs
length = len(my_dict)
print(length)  # Output: 3

# Iterating over a dictionary
for key in my_dict:
    print(key, ":", my_dict[key])
