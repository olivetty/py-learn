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