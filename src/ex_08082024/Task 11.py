# Reverse a string

string = "hello"
reversed_string = string[::-1]
print(reversed_string)  # Output: "olleh"


# Factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))  # Output: 120


# Palindrome of a string
def is_palindrome(s):
    return s == s[::-1]


print(is_palindrome("level"))  # True
print(is_palindrome("hello"))  # False


def is_palindrome(s):
    return s == s[::-1]


print(is_palindrome("racecar"))

# Binary search

import bisect


def binary_search(arr, target):
    index = bisect.bisect_left(arr, target)
    if index < len(arr) and arr[index] == target:
        return index
    return -1


# Example usage
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
print(f"Element found at index: {binary_search(arr, target)}")

# Find the max element in an array in Python

arr = [3, 5, 7, 2, 8, 10, 6]
print("Maximum element:", max(arr))  # Output: 10


# Calculate the Fibonacci sequence upto a number in Python

def fibonacci_upto(n):
    fib_sequence = [0, 1]
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > n:
            break
        fib_sequence.append(next_fib)
    return fib_sequence


print(fibonacci_upto(50))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Remove duplicates from a list in Python

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(unique_numbers)  # Output: [1, 2, 3, 4, 5]


# Print the sum of the digits of a number

def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10  # Get the last digit
        n //= 10  # Remove the last digit
    return total


print(sum_of_digits(12345))  # Output: 15


# Count of repeated words in Python

def count_words(sentence):
    words = sentence.lower().split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


sentence = "apple banana apple orange banana apple"
print(count_words(sentence))


# Count of repeated letters in Python

def count_letters(string):
    letter_count = {}
    for char in string:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count


string = "hello world"
print(count_letters(string))


# Write a program to find the HCF of two numbers without using recursion in Python

def find_hcf(a, b):
    while b != 0:
        a, b = b, a % b  # Keep swapping values until b becomes 0
    return abs(a)


# Example usage
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("HCF of", num1, "and", num2, "is:", find_hcf(num1, num2))


# Given a string of characters followed by their frequency, compress it into a proper format. in python

def decompress_string(s):
    result = []
    i = 0
    while i < len(s):
        char = s[i]
        i += 1
        freq = ""

        # Collect all digits for multi-digit frequencies
        while i < len(s) and s[i].isdigit():
            freq += s[i]
            i += 1

        result.append(char * int(freq))

    return ''.join(result)


# Example usage
compressed = "a2b3c1"
print(decompress_string(compressed))  # Output: "aabbbc"

# Write a C program to convert the Decimal to a Binary number

# Convert decimal to binary using bin()
decimal = int(input("Enter a decimal number: "))
binary = bin(decimal)[2:]  # Remove the '0b' prefix
print("Binary representation:", binary)


# Given an array of prefix XOR values, reconstruct the original array.

def reconstruct_array(prefix):
    n = len(prefix)
    arr = [0] * n
    arr[0] = prefix[0]  # First element is the same

    # arr[i] = prefix[i] ^ prefix[i - 1]
    for i in range(1, n):
        arr[i] = prefix[i] ^ prefix[i - 1]

    return arr


# Example usage
prefix = [5, 2, 7, 3]
print("Original array:", reconstruct_array(prefix))

# Write a program to check if a number is prime.
import math


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


# Example usage
num = int(input("Enter a number: "))
print(f"{num} is prime: {is_prime(num)}")


# Write a program to count the number of vowels in a given string
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count


# Example usage
string = input("Enter a string: ")
print("Number of vowels:", count_vowels(string))

#