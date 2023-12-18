# List
fruits_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(fruits_list)  # Output: ['apple', 'banana', 'cherry', 'date', 'elderberry']
# [] - ordered and changeable. Duplicates OK

# Tuple
fruits_tuple = ('apple', 'banana', 'cherry', 'date', 'elderberry')
print(fruits_tuple)  # Output: ('apple', 'banana', 'cherry', 'date', 'elderberry')
# () - ordered and unchangeable. Duplicates OK

# Set
fruits_set = {'apple', 'banana', 'cherry', 'date', 'elderberry'}
print(fruits_set)  # Output: {'date', 'elderberry', 'cherry', 'apple', 'banana'}
# {} - unordered and unindexed. No duplicates

###########
my_list = [1, 2, 3, 4, 5]
my_other_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

my_list.append(my_other_list[1])

print(my_list)
print(len(my_list))