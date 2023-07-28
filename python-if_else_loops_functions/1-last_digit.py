#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Calcula el último dígito del número
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit

# Imprime la salida según el último dígito
output = f"Last digit of {number} is {last_digit}"
if last_digit > 5:
    print(output + " and is greater than 5")
elif last_digit == 0:
    print(output + " and is 0")
else:
    print(output + " and is less than 6 and not 0")
