#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    print("{:d}".format(last_digit))

# Ejemplos de uso
print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
