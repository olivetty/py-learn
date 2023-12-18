# Example 1: Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry
# Example 2: Iterating over a range of numbers
for num in range(1, 6):
    print(num)

# Output:
# 1
# 2
# 3
# 4
# 5

# Example 3: Iterating over a string
word = "Hello"
for letter in word:
    print(letter)

# Output:
# H
# e
# l
# l
# o

# Example 4: Iterating over a dictionary
person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(key, ":", value)

# Output:
# name : John
# age : 30
# city : New York

# Example 5: Iterating over a set
fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(fruit)

# Output:
# cherry
# apple
# banana
# Example 6: Iterating over a tuple
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry
# Example 7: Iterating over a string using range()
word = "Hello"
for i in range(len(word)):
    print(word[i])

# Output:
# H
# e
# l
# l
# o
# Example 8: Iterating over a list using range()
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(fruits[i])

# Output:
# apple
# banana
# cherry
# Example 9: Iterating over a range of numbers using range()
for i in range(1, 6):
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5
# Example 10: Iterating over a dictionary using range()
person = {"name": "John", "age": 30, "city": "New York"}
for i in range(len(person)):
    print(list(person.items())[i])

# Output:
# ('name', 'John')
# ('age', 30)
# ('city', 'New York')
    
# Example 11: Iterating over a set using range()
fruits = {"apple", "banana", "cherry"}
for i in range(len(fruits)):
    print(list(fruits)[i])

# Output:
# cherry
# apple
# banana
# Example 12: Iterating over a tuple using range()
fruits = ("apple", "banana", "cherry")
for i in range(len(fruits)):
    print(fruits[i])

# Output:
# apple
# banana
# cherry
# Example 13: Iterating over a list using enumerate()
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, ":", fruit)

# Output:
# 0 : apple
# 1 : banana
# 2 : cherry
# Example 14: Iterating over a range of numbers using enumerate()
for i, num in enumerate(range(1, 6)):
    print(i, ":", num)

# Output:
# 0 : 1
# 1 : 2
# 2 : 3
# 3 : 4
# 4 : 5
# Example 15: Iterating over a dictionary using enumerate()
person = {"name": "John", "age": 30, "city": "New York"}
for i, key in enumerate(person):
    print(i, ":", person[key])

# Output:
# 0 : John
# 1 : 30
# 2 : New York
# Example 16: Iterating over a set using enumerate()
fruits = {"apple", "banana", "cherry"}
for i, fruit in enumerate(fruits):
    print(i, ":", fruit)

# Output:
# 0 : cherry
# 1 : apple
# 2 : banana
    
# Example 17: Iterating over a tuple using enumerate()
fruits = ("apple", "banana", "cherry")
for i, fruit in enumerate(fruits):
    print(i, ":", fruit)

# Output:
# 0 : apple
# 1 : banana
# 2 : cherry
# Example 18: Iterating over a list using reversed()
    
fruits = ["apple", "banana", "cherry"]
for fruit in reversed(fruits):
    print(fruit)

# Output:
# cherry
# banana
# apple
    
# Example 19: Iterating over a range of numbers using reversed()
for num in reversed(range(1, 6)):
    print(num)

# Output:
# 5
# 4
# 3
# 2
# 1
    
# Example 20: Iterating over a string using reversed()
word = "Hello"
for letter in reversed(word):
    print(letter)

# Output:
# o
# l
# l
# e
    
# Example 21: Iterating over a dictionary using reversed()
person = {"name": "John", "age": 30, "city": "New York"}
for key in reversed(person):
    print(key, ":", person[key])

# Output:
# city : New York
# age : 30
# name : John
    
# Example 22: Iterating over a set using reversed()
fruits = {"apple", "banana", "cherry"}
for fruit in reversed(fruits):
    print(fruit)

# Output:
# cherry
# apple
# banana
    
# Example 23: Iterating over a tuple using reversed()
fruits = ("apple", "banana", "cherry")
for fruit in reversed(fruits):
    print(fruit)

# Output:
# cherry
# banana
# apple
    
# Example 24: Iterating over a list using sorted()
fruits = ["apple", "banana", "cherry"]
for fruit in sorted(fruits):
    print(fruit)

# Output:
# apple
# banana
# cherry
    
# Example 25: Iterating over a range of numbers using sorted()
for num in sorted(range(1, 6)):
    print(num)

# Output:
# 1
# 2
# 3
# 4
# 5
    
# Example 26: Iterating over a string using sorted()
word = "Hello"
for letter in sorted(word):
    print(letter)

# Output:
# H
# e
# l
# l
# o
    
# Example 27: Iterating over a dictionary using sorted()
person = {"name": "John", "age": 30, "city": "New York"}
for key in sorted(person):
    print(key, ":", person[key])

# Output:
# age : 30
# city : New York
# name : John
    
# Example 28: Iterating over a set using sorted()
fruits = {"apple", "banana", "cherry"}
for fruit in sorted(fruits):
    print(fruit)

# Output:
# apple
# banana
# cherry
    
# Example 29: Iterating over a tuple using sorted()
fruits = ("apple", "banana", "cherry")
for fruit in sorted(fruits):
    print(fruit)

# Output:
# apple
# banana
# cherry
    
# Example 30: Iterating over a list using zip()
fruits = ["apple", "banana", "cherry"]
prices = [1.2, 3.3, 4.5]
for fruit, price in zip(fruits, prices):
    print(fruit, ":", price)

# Output:
# apple : 1.2
# banana : 3.3
# cherry : 4.5
    
# Example 31: Iterating over a range of numbers using zip()
for num1, num2 in zip(range(1, 6), range(6, 11)):
    print(num1, ":", num2)

# Output:
# 1 : 6
# 2 : 7
# 3 : 8
# 4 : 9
# 5 : 10
    
# Example 32: Iterating over a string using zip()
word1 = "Hello"
word2 = "World"
for letter1, letter2 in zip(word1, word2):
    print(letter1, ":", letter2)

# Output:
# H : W
# e : o
# l : r
# l : l
# o : d
    
# Example 33: Iterating over a dictionary using zip()
person = {"name": "John", "age": 30, "city": "New York"}
for key, value in zip(person.keys(), person.values()):
    print(key, ":", value)

# Output:
# name : John
# age : 30
# city : New York
    
# Example 34: Iterating over a set using zip()
fruits = {"apple", "banana", "cherry"}
prices = {1.2, 3.3, 4.5}
for fruit, price in zip(fruits, prices):
    print(fruit, ":", price)

# Output:
# cherry : 1.2
# apple : 3.3
# banana : 4.5
    
# Example 35: Iterating over a tuple using zip()
fruits = ("apple", "banana", "cherry")
prices = (1.2, 3.3, 4.5)
for fruit, price in zip(fruits, prices):
    print(fruit, ":", price)

# Output:
# apple : 1.2
# banana : 3.3
# cherry : 4.5
    
# Example 36: Iterating over a list using reversed() and enumerate()
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(reversed(fruits)):
    print(i, ":", fruit)

# Output:
# 0 : cherry
# 1 : banana
# 2 : apple
    
# Example 37: Iterating over a range of numbers using reversed() and enumerate()
for i, num in enumerate(reversed(range(1, 6))):
    print(i, ":", num)

# Output:
# 0 : 5
# 1 : 4
# 2 : 3
    
# Example 38: Iterating over a string using reversed() and enumerate()
word = "Hello"
for i, letter in enumerate(reversed(word)):
    print(i, ":", letter)

# Output:
# 0 : o
# 1 : l
# 2 : l
# 3 : e
    
# Example 39: Iterating over a dictionary using reversed() and enumerate()
person = {"name": "John", "age": 30, "city": "New York"}
for i, key in enumerate(reversed(person)):
    print(i, ":", person[key])

# Output:
# 0 : New York
# 1 : 30
# 2 : John
    
# Example 40: Iterating over a set using reversed() and enumerate()
fruits = {"apple", "banana", "cherry"}
for i, fruit in enumerate(reversed(fruits)):
    print(i, ":", fruit)

# Output:
# 0 : cherry
# 1 : apple
# 2 : banana
    
# Example 41: Iterating over a tuple using reversed() and enumerate()
fruits = ("apple", "banana", "cherry")
for i, fruit in enumerate(reversed(fruits)):
    print(i, ":", fruit)

# Output:
# 0 : cherry
# 1 : banana
# 2 : apple
    
# Example 42: Iterating over a list using sorted() and enumerate()
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(sorted(fruits)):
    print(i, ":", fruit)

# Output:
# 0 : apple
# 1 : banana
# 2 : cherry
    
# Example 43: Iterating over a range of numbers using sorted() and enumerate()
for i, num in enumerate(sorted(range(1, 6))):
    print(i, ":", num)

# Output:
# 0 : 1
# 1 : 2
# 2 : 3
# 3 : 4
# 4 : 5
    
# Example 44: Iterating over a string using sorted() and enumerate()
word = "Hello"
for i, letter in enumerate(sorted(word)):
    print(i, ":", letter)

# Output:
# 0 : H
# 1 : e
# 2 : l
# 3 : l
# 4 : o
    
