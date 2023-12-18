# Simple function
####################
#Example 1
my_list = [10, 20, 30, 40, 50]

def days_to_hours(days):
    hours_in_month = days * 24
    print(f"There are {hours_in_month} hours in {days} days")

for days_in_list in my_list:
    days_to_hours(days_in_list)


# Recursion  - function calling itself from within itself
####################
#Example 1
    
def walk(steps):
    if steps == 0:
        return
    walk(steps - 1)
    print(f"You made step {steps}.")

walk(50)

# Lambda Expressions
####################
# Single line expresions, anonymous functions, no name, you can assign to a variable

#Example 1
def add(a, b):
    return a + b

print(add(5, 7))

add = lambda a, b: a + b

print(add(5, 7))

#Example 2
givename = lambda first_name, last_name: f"Firsf name: {last_name}, Last name: {first_name}";
print(givename("Oliver", "Smith"))

# Function Docstrings
####################
#Example 1
def add(a, b):
    """This function adds two numbers
    param1: a: This is the first number
    param2: b: This is the second number
    return: The result of the addition of a and b
    """    
    return a + b

print(add(5, 10))
