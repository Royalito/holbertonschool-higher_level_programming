#!/usr/bin/python3
import random

number = random.randint(-10, 10)

# Print the number
print("The number:", number)

# Check if the number is positive, zero, or negative, and print the corresponding message
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
