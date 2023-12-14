""" This is a multi line comment
    We need to be very carefull about the indentation
    This is a multi line comment
"""

FILE_SIZE_LIMIT = 2000 # this is a constant

# --- Integer variable
integer_var = 10
count = 10_000_000_000 # you can use the underscore (_) character to make numbers more readable

# --- Float variable
float_var = 3,14

# --- String variable
string_var = "Hello, World!"
string_multiline = '''This is a multiline string
We need to be very carefull about the indentation'''

message = 'It\'s also a valid string' #To escape the quotes, you use the backslash (\) character
greeting = 'Good ' 'Morning!' # When you place the string literals next to each other, Python automatically concatenates them into one string.

# --- Boolean variable
boolean_var = True

# --- List variable
list_var = [1, 2, 3, 4, 5]

# --- Tuple variable
tuple_var = (1, 2, 3, 4, 5)

# --- Set variable
set_var = {1, 2, 3, 4, 5}

# --- Dictionary variable
dict_var = {"name": "John", "age": 30}

# --- None variable
none_var = None

# --- example of a function
def my_function():
    i = 1
    max=10
    name = "Alice"
    age = 25
    while i <= max:
        print(f"{i} - My name is {name} and I am {age} years old.")         
        i += 1       

my_function() # call the function

str_val = '2'
val = 0
int(str_val) # convert a string to a integer number.
float(str_val) # convert a string to a floating-point number.
bool(val) # convert a value to a boolean value, either True or False.
str(val) # return the string representation of a value.
type(str_val) # return the type of a value.

# --- print variables
print(int(integer_var/2))
print(float_var)
print(string_multiline)
print(type(str_val))