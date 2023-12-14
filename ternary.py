def how_much_to_pay():
    empaty_message = 'Enjoy your movie!'
    age = int(input('Enter your age:')) # get the age from the user
    ticket_price = 5 if age < 10 else 19 if age < 18 else 29 # determine the ticket price => ternary operator (value_if_true if condition else value_if_false)
    print(f'You\'ll pay ${ticket_price} for the ticket. {empaty_message}') # show the ticket price

how_much_to_pay() # call the function