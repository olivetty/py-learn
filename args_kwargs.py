def sum(*args): # args is a tuple can be any name like *numbers
    total = 0
    for args in args:
        total += args
    return total

print(sum(1, 2, 3, 4, 5))

##########################

def address(**kwargs): # kwargs is a dictionary can be any name like **address
    for key, value in kwargs.items():
        print(f"{key} : {value}")

address(STR="5th Avenue", NO=12, CITY="New York")