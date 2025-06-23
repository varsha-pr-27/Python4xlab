# Reverse a string without using built in function
def reverse_string(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


# Find duplicates in a list

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = set(my_list)

if len(my_list) != len(unique_elements):
    print("Duplicates found in the list")
else:
    print("No duplicates found in the list")
print(unique_elements)

# Count the frequency of elements in a list
from collections import Counter

my_list = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4]
frequency_counter = Counter(my_list)
print(frequency_counter)  # Output: Counter({4: 4, 3: 3, 2: 2, 1: 1})

