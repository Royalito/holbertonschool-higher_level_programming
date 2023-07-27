#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Calcula el último dígito del número
last_digit = abs(number) % 10

# Imprime la salida según el último dígito
print(f"Last digit of {number} is {last_digit} and is greater than 5") if last_digit > 5 else \
    print(f"Last digit of {number} is {last_digit} and is 0") if last_digit == 0 else \
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
