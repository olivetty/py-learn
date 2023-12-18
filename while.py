count = 0
while count < 5:
  print("Count:", count)
  count += 1

# Output:
# Count: 0
# Count: 1
# Count: 2
# Count: 3
# Count: 4
  
# Example 1: Iterating over a list using while loop
fruits = ["apple", "banana", "cherry"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# Output:
# apple
# banana
# cherry
    
# Example 2: Iterating over a dictionary using while loop
person = {"name": "John", "age": 30, "city": "New York"}
i = 0
keys = list(person.keys()) # Converting dictionary keys to list

while i < len(person):  # Iterating over a list
    value = person[keys[i]] # Getting value from key
    print(keys[i], ":", value) # Printing key and value
    i += 1 # Incrementing counter by 1

# Output:
# name : John
# age : 30
# city : New York
    





#Example 2
exit = "no"
while exit == "no":
  user_request = input('What animal do you want to hear? ').lower()
  if  user_request == "cow":
    print("Moo.🐮")
  elif user_request == "dog":
    print("Whoff.🐶")
  elif user_request == "cat":
    print("Miau.🐱")
  else:
    print("I don't know what that is.")
    
  exit = input("Do you want to exit? ").lower()
  if exit.lower() == "yes":
    print("Goodbye.")


    count = 0
    while count < 5:
      print("Count:", count)
      if count == 3:
        break  # Exit the loop when count is 3
      count += 1

    # Output:
    # Count: 0
    # Count: 1
    # Count: 2
    # Count: 3
      
    # Example 1: Using break in a for loop
    for val in "string":
        if val == "i":
            break
        print(val)

    print("The end")

    # Output:
    # s
    # t
    # r
    # The end

    # Example 2: Using break in a while loop
    ''' while condition:
          # some code
          if condition:
          break
    '''
    i = 0
    while i < 5:
        print(i)
        i += 1
        if i == 3:
            break
            
    # Output:
    # 0
    # 1
    # 2
        
    # Example 3: 
        
print('-- Help: type quit to exit --')
while True:
    color = input('Enter your favorite color:')
    if color.lower() == 'quit':
        break
        

