number = [123, 56, 89, 23, 451, 789, 121, 6, 9, 3, 44, 78]
sorted_number = sorted(number)
print(sorted_number)

for num in sorted_number:
    if num % 5 == 0:
        print(f"{num} is divisible by 5")
        break   # This will stop the loop when the first number divisible by 5 is found
    else:
        print(f"{num} is not divisible by 5")

else: # This will be executed if the loop is not stopped by the break statement
    print("There is no number divisible by 5") # This will not be printed because of the break statement above