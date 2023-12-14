# --- Example with a single condition
x = 10
if x > 5:
    print("x is greater than 5")

# --- Example with multiple conditions using 'and'
y = 7
if 5 < y < 10 and y!= 7: # this is forced by i want to showcase the 'and' operator
    print("y is between 5 and 10")
elif y > 10 or y < 5: # witch comes first true
    print("y is greater or than 10 or smaller tham 5")
else:
    print("y is 7")

# --- Example with multiple conditions using 'or'
z = 5
if z < 5 or z > 10:
    print("z is either less than 5 or greater than 10")

# --- The following example illustrates how to use the backslash (\) character to continue a statement in the second line:
a, b, c = True, False, True
if (a == True) and (b == False) and \
   (c == True):
    print("Continuation of statements")

# --- Example of price based by age
age = input('Enter your age:') # get the age from the user
your_age = int(age) # convert the string to int

if your_age < 5: # determine the ticket price
    ticket_price = 5
elif your_age < 16:
    ticket_price = 10
else:
    ticket_price = 18

print(f'You\'ll pay ${ticket_price} for the ticket') # show the ticket price