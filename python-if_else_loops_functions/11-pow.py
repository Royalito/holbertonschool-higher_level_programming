#!/usr/bin/python3
def power(a, b):
    result = 1
    for _ in range(abs(b)):
        result *= a
    if b < 0:
        result = 1 / result
    return result

# Test cases
print("Correct output - case: 98 with return:", power(7, 2))
print("Correct output - case: 98:", power(-7, 2))
print("Correct output - case: -98 with return:", power(7, -2))
print("Correct output - case: 0:", power(0, 5))
